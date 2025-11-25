from fastmcp import FastMCP, tool

# Create MCP server
mcp = FastMCP("Arithmetic MCP Server")

# Tool: Addition
@tool
def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    """
    return a + b

# Tool: Subtraction
@tool
def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    """
    return a - b

# Tool: Multiplication
@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    """
    return a * b

# Tool: Division
@tool
def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    Raises an error if b=0.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
