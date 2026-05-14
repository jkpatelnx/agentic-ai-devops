from ollama import chat
from rich import print

print("[bold green]CLI Chatbot Started[/bold green]")
print("[yellow]Type 'exit' to quit[/yellow]")

SYSTEM_PROMPT = """
You are a helpful CLI AI assistant.
Rules:
- Keep responses concise
- Avoid unnecessary explanations
- Format outputs clearly
- Respond directly
"""


while True:
    user_input = input(f"\nAsk agent:\n")

    if user_input.lower() == "exit":
        break

    response = chat(model='gemma4', messages=[
        {
            'role': 'systemc',
            'content': SYSTEM_PROMPT
        },
        {
            'role': 'user',
            'content': user_input
        },
    ])

    print("\n[bold cyan]Agent:[/bold cyan]")
    print(response['message']['content'])
    # or access fields directly from the response object
    #print(response.message.content)