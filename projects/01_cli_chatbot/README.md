# CLI Chatbot

A simple local AI CLI chatbot built using Python and Ollama.

Developed and tested on Linux.

## Features

- Local LLM chatbot
- Interactive CLI chat
- Colored terminal output
- System prompt support

## Tech Stack

- Python
- Ollama
- Rich

## Model

- gemma4

## Project Structure

```text
01_cli_chatbot/
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

# Verify Model
ollama list
```

## Setup

```bash
# Create Virtual Environment
python -m venv .venv

# Activate Virtual Environment
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Run
python3 app.py
```

## Example

```text
Ask agent:
hello

Agent:
Hello! How can I help you today?
```