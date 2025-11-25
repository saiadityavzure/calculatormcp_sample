from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Arithmetic MCP Server")

# Tool: Addition
@mcp.tool
def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    """
    return a + b

# Tool: Subtraction
@mcp.tool
def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    """
    return a - b

# Tool: Multiplication
@mcp.tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    """
    return a * b

# Tool: Division
@mcp.tool
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
