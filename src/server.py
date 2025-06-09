from mcp.server.fastmcp import FastMCP
from datetime import datetime
import pytz

# Create a basic server instance with custom settings
mcp = FastMCP(
    name="Date and time",
    instructions="This server provides date and time tools.",
    host="127.0.0.1",  # Set the host
    port=8001,         # Set the port
    log_level="DEBUG"  # Set the log level
)


@mcp.tool()
def current_datetime(timezone: str) -> str:
    """Get the current date and time in a specific timezone"""
    try:
        tz = pytz.timezone(timezone)
        return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Unknown timezone: {timezone}"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    # The {user_id} in the URI is extracted and passed to this function
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

    
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # mcp.run()  # local
    mcp.run(transport="streamable-http")  # remote
