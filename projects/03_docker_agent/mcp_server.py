
from fastmcp import FastMCP
import subprocess

mcp = FastMCP("Docker MCP Server")

@mcp.tool
def list_containers() -> str:
    """Tool 1: Listimport subprocess all Docker containers (running and stopped)."""
    result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool
def get_logs(container_name: str) -> str:
    """Tool 2: Get the last 40 lines of logs from a Docker container."""
    result = subprocess.run(["docker", "logs", "--tail", "50", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

@mcp.tool
def inspect_container(container_name: str) -> str:
    """Tool 3: Get detailed info about a Docker container (state, config, network)."""
    result = subprocess.run(["docker", "inspect", container_name], capture_output=True, text=True)
    return result.stdout or result.stderr

if __name__ == "__main__":
    mcp.run()