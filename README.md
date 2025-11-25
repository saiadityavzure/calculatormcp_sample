# Arithmetic FastMCP Server

This is a sample MCP server built using FastMCP, providing simple math tools:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

## Running locally

1. Install dependencies:
   pip install -r requirements.txt

2. Start server:
   python server.py

The server runs on port 8000.

## Running with Docker

docker build -t arithmetic-mcp .
docker run -p 9000:8000 arithmetic-mcp

