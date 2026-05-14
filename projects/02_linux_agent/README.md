# Linux AI Agent

A simple Linux AI assistant built using Python, Ollama, and LangChain.

Developed and tested on Linux.

## Features

- Local AI agent
- Linux system monitoring
- Tool calling with LangChain
- Interactive CLI chat
- Colored terminal output

## Tech Stack

- Python
- Ollama
- LangChain
- Rich

## Model

- gemma4

## Tools

- Disk usage
- Memory usage
- CPU load

## Project Structure

```text
02_linux_agent/
│
├── app.py
├── requirements.txt
└── README.md
```

## Ollama Setup

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama Server
ollama serve

# Pull Model
ollama pull gemma4
```

## Setup

```bash
# Create Virtual Environment
python -m venv .venv

# Activate Virtual Environment
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

## Example

```text
Ask agent:
show memory usage

Ask agent:
show disk usage

Ask agent:
show cpu load
```