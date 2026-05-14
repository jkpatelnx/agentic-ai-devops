import subprocess

from rich import print

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

print("[bold green]Linux AI Agent Started[/bold green]")
print("[yellow]Type 'exit' to quit[/yellow]")

SYSTEM_PROMPT = """
You are a helpful CLI AI assistant.
Rules:
- Keep responses concise
- Avoid unnecessary explanations
- Format outputs clearly
- Respond directly
"""

@tool
def get_disk_usage():
    """Tool 1: Get disk usage and filesystem information."""
    result = subprocess.run(["df","-Th"], capture_output=True, text=True)
    return result.stdout

@tool
def get_memory_usage():
    """Tool 2: Get total, used, and free system memory."""
    result = subprocess.run(["free","-h"], capture_output=True, text=True)
    return result.stdout

@tool
def get_cpu_load():
    """Tool 3: Get CPU load and system uptime."""
    uptime_result = subprocess.run(["uptime"], capture_output=True, text=True)
    core_result = subprocess.run(["nproc"], capture_output=True, text=True)

    return (
        f"CPU Cores:\n{core_result.stdout}\n"
        f"System Load:\n{uptime_result.stdout}"
    )

llm_model = ChatOllama(
    model="gemma4",  
    temperature=0.8,
    system=SYSTEM_PROMPT
    ) 

tools = [get_disk_usage,get_memory_usage,get_cpu_load]

linux_agent = create_agent(llm_model,tools)

while True:
    user_input = input(f"\nAsk agent:\n")

    if user_input.lower() == "exit":
        break

    response = linux_agent.invoke(
        {
            "messages": [
                {
                    'role': 'user',
                    'content': user_input
                }
            ]
        }
    )


    print("\n[bold cyan]Agent:[/bold cyan]")
    print(response['messages'][-1].content)
