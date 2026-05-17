import subprocess

from rich import print

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

SYSTEM_PROMPT = """
You are a helpful CLI AI assistant.
Rules:
- Keep responses concise
- Avoid unnecessary explanations
- Format outputs clearly
- Respond directly
"""

# --- Docker tools ---

@tool
def list_containers() -> str:
    """List all Docker containers (running and stopped)."""
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout or result.stderr


@tool
def get_logs(container_name: str) -> str:
    """Get the last 50 lines of logs from a Docker container."""
    result = subprocess.run(
        ["docker", "logs", "--tail", "50", container_name],
        capture_output=True, text=True,
    )
    return result.stdout + result.stderr


@tool
def inspect_container(container_name: str) -> str:
    """Get detailed info about a Docker container (state, config, network)."""
    result = subprocess.run(
        ["docker", "inspect", container_name],
        capture_output=True, text=True,
    )
    return result.stdout or result.stderr


# --- Kubernetes tools ---

@tool
def list_pods(namespace: str = "default") -> str:
    """List all pods in a Kubernetes namespace with their status."""
    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace],
        capture_output=True, text=True,
    )
    return result.stdout or result.stderr


@tool
def describe_pod(pod_name: str, namespace: str = "default") -> str:
    """Get detailed info about a Kubernetes pod including events and conditions."""
    result = subprocess.run(
        ["kubectl", "describe", "pod", pod_name, "-n", namespace],
        capture_output=True, text=True,
    )
    return result.stdout or result.stderr


@tool
def get_events(namespace: str = "default") -> str:
    """Get recent Kubernetes events in a namespace (useful for troubleshooting)."""
    result = subprocess.run(
        ["kubectl", "get", "events", "-n", namespace, "--sort-by=.lastTimestamp"],
        capture_output=True, text=True,
    )
    return result.stdout or result.stderr


llm_model = ChatOllama(
    model="gemma4",  
    temperature=0.8,
    system=SYSTEM_PROMPT
    ) 

tools = [
    list_containers, get_logs, inspect_container,
    list_pods, describe_pod, get_events,
]

k8s_aiops_agent = create_react_agent(llm_model, tools)

while True:
    user_input = input(f"\nAsk agent:\n")

    if user_input.lower() == "exit":
        break

    response = k8s_aiops_agent.invoke(
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

