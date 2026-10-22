# Tool Calling in Agents - Starter Assignment

## Overview

This assignment explores different approaches to enabling AI agents to use tools for solving problems that LLMs struggle with alone, such as arithmetic, comparisons, and accessing current information.

## What You'll Learn

1. **Baseline LLM** - Understanding LLM limitations without tools
2. **ReAct Prompting** - Manual implementation of thought-action-observation loops
3. **LangChain with Local Models** - Using frameworks with local LLMs
4. **LangChain with API Models** - Using frameworks with API-based models (optional)
5. **MCP Servers** - Model Context Protocol for tool calling

## Files to Complete

### 1. `starter.ipynb`
The main notebook with TODO sections to complete:

**Part 2: ReAct Prompting**
- Implement three tool functions: `compare_numbers()`, `add_numbers()`, `get_current_date()`
- Complete the `execute_action()` function to parse the `finish[answer]` action
- Fill in action descriptions in the ReAct prompt
- Add logic to update the prompt with each step in the ReAct loop

**Part 3: LangChain with Local Models**
- Re-implement the three tool functions using LangChain's `@tool` decorator
- Complete the `parse_tool_call()` function to extract tool calls from text
- Add logic to append tool results to the conversation

### 2. `mcp_server.py`
Complete the MCP server file by implementing:
- `compare_numbers()` - Compare two numbers
- `add_numbers()` - Add two numbers
- `multiply_numbers()` - Multiply two numbers
- `get_current_date()` - Get today's date

## Getting Started

1. Open `starter.ipynb` in Jupyter or VS Code
2. Run the setup cells to install dependencies
3. Follow the TODO comments throughout the notebook
4. Test your implementations by running the test cells
5. Complete `mcp_server.py` for the MCP section

## Testing Your Work

Each section has test cells that demonstrate the functionality:
- Run the baseline LLM test to see its limitations
- Test your ReAct agent implementation
- Test your LangChain local agent
- (Optional) Test with API models if you have an API key
- Test your MCP tools directly before setting up the server

## Hints

- Look at the solution notebook if you get stuck (but try on your own first!)
- The same tool logic is used across different sections - you can reuse implementations
- Use `datetime.now().strftime()` for formatting dates
- Regular expressions (regex) are helpful for parsing action strings
- JSON parsing is needed for LangChain tool calls

## Bonus Challenges

After completing the basic TODOs:
1. Add a `multiply_numbers` tool to the ReAct and LangChain agents
2. Test complex multi-step questions
3. Add error handling for invalid inputs
4. Try different prompt variations to improve performance
5. Experiment with different local models (Phi-3, Llama, etc.)

## Resources

- ReAct Paper: https://arxiv.org/abs/2210.03629
- LangChain Documentation: https://python.langchain.com/docs/
- MCP Documentation: https://modelcontextprotocol.io/

## Getting Help

- Review the markdown explanations in each notebook section
- Check the solution notebook for reference
- Look at the demo files in `../solution/demos/` for examples

Good luck! 🚀
