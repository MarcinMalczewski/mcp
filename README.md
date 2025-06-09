# Date and Time MCP Server

A simple Model Context Protocol (MCP) server that provides date and time functionality, along with example user profile and greeting resources.

## Features

- Get current date and time in any timezone
- Access user profiles by ID
- Get personalized greetings

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Start the server with:
```bash
python src/server.py
```

The server will start on `http://127.0.0.1:8001` with the following endpoints:

- Tools:
  - `current_datetime(timezone: str)`: Get current date and time in a specific timezone
- Resources:
  - `users://{user_id}/profile`: Get a user's profile by ID
  - `greeting://{name}`: Get a personalized greeting

### Running the Client

Run the example client with:
```bash
python src/client.py
```

The client will:
1. List all available tools
2. List all available resources
3. Call the `current_datetime` tool with "America/New_York" timezone

## Cursor Configuration

To use this server with Cursor IDE, you need to configure it in your Cursor settings. Create or update the `mcp.json` file in your Cursor configuration directory with the following:

```json
{
  "mcpServers": {
    "my-mcp-local-server": {
      "command": "path/to/your/python.exe",
      "args": [
        "path/to/your/server.py"
      ],
      "description": "MCP local server"
    },
    "my-mcp-remote-server": {
      "url": "http://127.0.0.1:8001/mcp",
      "description": "MCP remote server"
    }
  }
}
```

This configuration provides two ways to connect to the server:
1. `my-mcp-local-server`: Runs the server locally through Python
2. `my-mcp-remote-server`: Connects to the server running on port 8001

Make sure to replace the paths with your actual Python and server script paths.

## Example API Usage

### Get Current Time
```python
result = await client.call_tool("current_datetime", {"timezone": "America/New_York"})
```

### Get User Profile
```python
profile = await client.read_resource("users://123/profile")
```

### Get Greeting
```python
greeting = await client.read_resource("greeting://John")
```

## Development

The server is built using FastMCP, which provides a simple way to create MCP-compatible servers. The main components are:

- `server.py`: Contains the server implementation with tools and resources
- `client.py`: Example client that demonstrates how to interact with the server

## License

MIT 