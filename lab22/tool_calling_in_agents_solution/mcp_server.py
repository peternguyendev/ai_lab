#!/usr/bin/env python3
"""
MCP Server for Tool Calling Demo

This server exposes tools for AI coding assistants via the Model Context Protocol.
It can be used with VS Code, Claude Code, Cursor, or other MCP-compatible clients.

To install with VS Code:
1. Install the MCP extension in VS Code
2. Add this server to your MCP settings (see notebook for details)
3. The tools will be available to GitHub Copilot or other AI assistants
"""

from datetime import datetime
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("tool-calling-demo")


@mcp.tool()
def compare_numbers(a: float, b: float) -> str:
    """Compare two numbers and return which is greater."""
    if a > b:
        return f"{a} > {b} is TRUE. {a} is greater than {b}."
    elif a < b:
        return f"{a} > {b} is FALSE. {a} is less than {b}."
    else:
        return f"{a} and {b} are equal."


@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """Add two numbers and return the sum."""
    return f"{a} + {b} = {a + b}"


@mcp.tool()
def multiply_numbers(a: float, b: float) -> str:
    """Multiply two numbers and return the product."""
    return f"{a} × {b} = {a * b}"


@mcp.tool()
def get_current_date() -> str:
    """Get the current date."""
    return f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}."


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
