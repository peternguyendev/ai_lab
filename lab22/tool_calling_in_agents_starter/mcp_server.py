#!/usr/bin/env python3
"""
MCP Server for Tool Calling Demo - STARTER VERSION

This server exposes tools for AI coding assistants via the Model Context Protocol.
Complete the TODO sections to implement the full functionality.

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
    # TODO: Implement the comparison logic
    # Hint: Use if/elif/else to compare a and b
    # Return a string describing which number is greater
    # Fill in the implementation below
    pass


@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """Add two numbers and return the sum."""
    # TODO: Implement addition
    # Calculate a + b and return a formatted string
    # Example format: "a + b = result"
    # Fill in the implementation below
    pass


@mcp.tool()
def multiply_numbers(a: float, b: float) -> str:
    """Multiply two numbers and return the product."""
    # TODO: Implement multiplication
    # Calculate a × b and return a formatted string
    # Example format: "a × b = result"
    # Fill in the implementation below
    pass


@mcp.tool()
def get_current_date() -> str:
    """Get the current date."""
    # TODO: Get today's date and format it nicely
    # Hint: Use datetime.now().strftime() with a format like '%A, %B %d, %Y'
    # Return a string like "Today's date is Monday, February 03, 2026."
    # Fill in the implementation below
    pass


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
