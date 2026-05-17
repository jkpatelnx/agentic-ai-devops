# Agentic AI DevOps

A comprehensive collection of AI-powered agents for DevOps automation, system management, containerization, and Kubernetes operations using local LLMs (Ollama), LangChain, and tool calling.

## Overview

This project demonstrates building autonomous agents that can interact with infrastructure, containers, and orchestration platforms. Each project showcases different aspects of AI-driven DevOps workflows.

## Projects

### 1. [Chatbot Agent](./projects/01_chatbot_agent/) – Simple CLI Chatbot

A foundational AI chatbot built with Python and Ollama. Perfect starting point for understanding local LLM integration.

- **Features:** Interactive CLI, colored output, system prompt support
- **Tech:** Python, Ollama, Rich
- **Model:** gemma4
- **Use Case:** Learning AI agent basics

### 2. [Linux Agent](./projects/02_linux_agent/) – System Monitoring & Troubleshooting

An intelligent Linux system assistant with tool calling capabilities for real-time monitoring and diagnostics.

- **Features:** Disk/memory/CPU monitoring, tool calling with LangChain, CLI chat
- **Tech:** Python, Ollama, LangChain, Rich
- **Model:** gemma4
- **Tools:** Disk usage, Memory usage, CPU load
- **Use Case:** Automated system troubleshooting

### 3. [Docker Agent](./projects/03_docker_agent/) – Container Management

A Docker management assistant with direct and MCP-based implementations for container inspection, log viewing, and resource management.

- **Features:** List containers, view logs, inspect details, interactive chat
- **Tech:** Python, Docker, Ollama, LangChain, FastMCP, Rich
- **Model:** gemma4
- **Tools:** Docker ps, Docker logs, Docker inspect
- **Use Case:** Containerized environment management
- **Variants:** Direct agent and MCP-based agent

### 4. [Kubernetes AIOps Agent](./projects/04_k8s_aiops_agent/) – Kubernetes Operations & Troubleshooting

A production-grade AI assistant for Kubernetes cluster operations, diagnostics, and automated remediation.

- **Features:** Pod inspection, log aggregation, deployment scaling, troubleshooting hints, interactive chat
- **Tech:** Python, Kubernetes, Ollama, LangChain, FastMCP, Rich
- **Model:** gemma4
- **Tools:** kubectl get pods, kubectl logs, kubectl describe, kubectl scale
- **Use Case:** Kubernetes cluster management and AIOps
- **Variants:** Direct agent and MCP-based agent

## Quick Start

### Prerequisites

- Python 3.10+
- Ollama installed ([install](https://ollama.com))
- macOS, Linux, or WSL2 on Windows

Optional for specific projects:
- Docker (for Docker Agent)
- Kubernetes cluster + kubectl (for K8s Agent)

### Setup Any Project

```bash
# Navigate to project directory
cd projects/01_chatbot_agent  # or other projects

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama server (separate terminal)
ollama serve

# Pull the required model
ollama pull gemma4

# Run the agent
python3 chatbot_agent.py  # or appropriate agent script
```

## Project Structure

```text
agentic-ai-devops/
├── README.md
├── LICENSE
│
└── projects/
    │
    ├── 01_chatbot_agent/
    │   ├── chatbot_agent.py
    │   ├── requirements.txt
    │   └── README.md
    │
    ├── 02_linux_agent/
    │   ├── linux_agent.py
    │   ├── requirements.txt
    │   └── README.md
    │
    ├── 03_docker_agent/
    │   ├── docker_agent.py
    │   ├── docker_agent_with_mcp.py
    │   ├── mcp_server.py
    │   ├── requirements.txt
    │   └── README.md
    │
    └── 04_k8s_aiops_agent/
        ├── k8s_aiops_agent.py
        ├── k8s_aiops_agent_with_mcp.py
        ├── mcp_server.py
        ├── requirements.txt
        └── README.md
```

## Common Tech Stack

All projects leverage:

- **Python** – Core language
- **Ollama** – Local LLM runtime
- **LangChain** – Agent orchestration and tool calling
- **Rich** – Beautiful terminal output
- **FastMCP** (Docker & K8s agents) – Model Context Protocol for MCP-based variants

## Running Examples

### Chatbot Agent

```bash
cd projects/01_chatbot_agent
python3 chatbot_agent.py
# Type: hello
# Get: Interactive AI responses
```

### Linux Agent

```bash
cd projects/02_linux_agent
python3 linux_agent.py
# Type: show disk usage
# Get: Disk usage metrics and analysis
```

### Docker Agent

```bash
cd projects/03_docker_agent
python3 docker_agent.py
# Type: list all containers
# Get: Container list with intelligent analysis
```

### Kubernetes Agent

```bash
cd projects/04_k8s_aiops_agent
python3 k8s_aiops_agent.py
# Type: list pods in namespace default
# Get: Pod list with recommendations
```

## Learning Path

1. **Start with:** [01_chatbot_agent](./projects/01_chatbot_agent/) – Understand basic LLM + Python integration
2. **Progress to:** [02_linux_agent](./projects/02_linux_agent/) – Learn tool calling and system interaction
3. **Explore:** [03_docker_agent](./projects/03_docker_agent/) – See MCP patterns and container management
4. **Master:** [04_k8s_aiops_agent](./projects/04_k8s_aiops_agent/) – Build production-grade AIOps solutions

## Key Concepts

- **Local LLMs** – Using Ollama for on-premise, privacy-first AI
- **Tool Calling** – Enabling agents to interact with real systems
- **Agent Pattern** – Autonomous decision-making and task execution
- **MCP (Model Context Protocol)** – Standardized agent-to-tool communication
- **AIOps** – AI-driven operations and troubleshooting

## Notes

- All agents are designed to run locally without cloud dependencies
- Models are downloaded to local storage by Ollama
- Each project is independently runnable
- MCP-based variants provide extensible tool integration

## Getting Started

For detailed setup and usage of each project, refer to the individual README files:

- [Chatbot Agent Setup](./projects/01_chatbot_agent/README.md)
- [Linux Agent Setup](./projects/02_linux_agent/README.md)
- [Docker Agent Setup](./projects/03_docker_agent/README.md)
- [Kubernetes Agent Setup](./projects/04_k8s_aiops_agent/README.md)
