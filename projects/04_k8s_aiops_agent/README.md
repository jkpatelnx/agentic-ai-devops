# Kubernetes AIOps Agent

A local CLI AI assistant for Kubernetes operations and troubleshooting built with Python, Ollama, and LangChain.

Developed and tested on Linux.

## Features

- Inspect cluster resources (pods, deployments, services)
- View pod logs and describe resources
- Scale deployments
- Basic automated troubleshooting hints
- Interactive CLI chat with tool calling
- Colored terminal output

## Tech Stack

- Python
- Kubernetes (kubectl)
- Ollama
- LangChain
- FastMCP
- Rich

## Model

- gemma4

## Tools

- `kubectl get pods -A`
- `kubectl logs --tail 100 <pod>`
- `kubectl describe pod <pod>`
- `kubectl scale deployment <name> --replicas=<n>`

## Project Structure

```text
04_k8s_aiops_agent/
├── k8s_aiops_agent.py
├── k8s_aiops_agent_with_mcp.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

## Prerequisites

- A Kubernetes cluster and a working `kubectl` configuration
- Python 3.10+
- Ollama installed and running

Optional: `kind` or `minikube` for local testing

## Ollama Setup

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
ollama serve

# Pull the model used by the project
ollama pull gemma4
```

## Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Run

Direct Kubernetes agent:

```bash
python3 k8s_aiops_agent.py
```

MCP-based Kubernetes agent:

```bash
python3 k8s_aiops_agent_with_mcp.py
```

## Example

```text
Ask agent:
list pods in namespace default

Ask agent:
show logs for pod my-app-abc123

Ask agent:
scale deployment webapp to 3
```

## Notes

- The MCP-based agent can start a local MCP server (`mcp_server.py`) and communicate through the MCP adapters.
- Ensure your `KUBECONFIG` is set to the target cluster before running the agent.
