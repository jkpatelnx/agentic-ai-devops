from rich import print

from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


SYSTEM_PROMPT = """
You are a helpful CLI AI assistant.
Rules:
- Keep responses concise
- Avoid unnecessary explanations
- Format outputs clearly
- Respond directly
"""

async def main():
    # 1. Initialize the MCP Client (Do this OUTSIDE the loop to avoid reconnecting every time)
    client = MultiServerMCPClient(
        {
            "docker-mcp" : {
                "transport": "stdio",
                "command":"python",
                "args": ["mcp_server.py"]
            }
        }
    )
    
    # Get the tools from the MCP server
    tools = await client.get_tools()

     # 2. Initialize the LLM
    llm_model = ChatOllama(
        model="gemma4",  
        temperature=0.8,
        system=SYSTEM_PROMPT
        ) 

    # 3. Create the agent
    docker_agent_with_mcp = create_agent(llm_model,tools)

    # 4. Maintain a conversation history
    # This allows the agent to remember previous parts of the conversation

    chat_history = []

    print("[bold green]Docker AI Agent with MCP Started[/bold green]")
    print("[yellow]--- Agent Ready! Type 'exit' or 'quit' to stop ---[/yellow]")

    while True:
        user_input = input(f"\nAsk agent:\n")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        if not user_input.strip():
            continue

        # Add user message to history
        chat_history.append(
            {
                "role": "user", 
                "content": user_input
            }
        )


        try:
            # 5. Invoke the agent with the full history
            response = await docker_agent_with_mcp.ainvoke(
                {
                    "messages": chat_history
                }
            )

            # Extract the last message from the agent's response
            agent_message = response['messages'][-1]

             # Print the response
            print("\n[bold cyan]Agent:[/bold cyan]")
            print(agent_message.content)

            # Add the agent's response to history so it remembers for the next turn
            chat_history.append(agent_message)
         
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSession ended by user.")

