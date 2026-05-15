import subprocess

from rich import print

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

print("[bold green]Docker AI Agent Started[/bold green]")
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
def list_containers() -> str:
    """Tool 1: List all Docker containers (running and stopped)."""
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def get_logs(container_name: str) -> str:
    """Tool 2: Get the last 50 lines of logs from a Docker container."""
    result = subprocess.run(["docker", "logs", "--tail", "50", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@tool
def inspect_container(container_name: str) -> str:
    """Tool 3: Get detailed info about a Docker container (state, config, network)."""
    result = subprocess.run(["docker", "inspect", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

llm_model = ChatOllama(
    model="gemma4",  
    temperature=0.8,
    system=SYSTEM_PROMPT
    ) 

tools = [list_containers,get_logs,inspect_container]

docker_agent = create_agent(llm_model,tools)

while True:
    user_input = input(f"\nAsk agent:\n")

    if user_input.lower() == "exit":
        break

    response = docker_agent.invoke(
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
