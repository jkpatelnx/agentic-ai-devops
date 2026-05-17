# Docker AI Agent

A local CLI AI assistant for Docker management built with Python, Ollama, and LangChain.

This project includes two ways to use the agent:

- A direct Docker tool agent
- An MCP-based Docker agent

## Features

- List Docker containers
- View container logs
- Inspect container details
- Interactive CLI chat
- Colored terminal output

## Tech Stack

- Python
- Docker
- Ollama
- LangChain
- FastMCP
- Rich

## Model

- gemma4

## Tools

- `docker ps -a`
- `docker logs --tail 50 <container>`
- `docker inspect <container>`

## Project Structure

```text
03_docker_agent/
├── docker_agent.py
├── docker_agent_With_mcp.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Docker installed and running
- Ollama installed
- Python 3.10+ recommended

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
pip install langchain langchain-ollama langchain-mcp-adapters fastmcp rich
```

## Run

Direct Docker agent:

```bash
python3 docker_agent.py
```

MCP-based Docker agent:

```bash
python3 docker_agent_With_mcp.py
```

## Example

```text
Ask agent:
list all containers

Ask agent:
show logs for my-container

Ask agent:
inspect my-container
```

## Notes

- The MCP-based agent starts the MCP server through the client configuration in `docker_agent_With_mcp.py`.
- The direct agent runs Docker commands locally through Python's `subprocess` module.
