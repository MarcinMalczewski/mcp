from fastmcp import Client
import asyncio

# The Client automatically uses StreamableHttpTransport for HTTP URLs
client = Client("http://localhost:8001/mcp")

async def main():
    async with client:
        tools = await client.list_tools()
        print("=============================")
        print(f"Available tools: {tools}")

        resources = await client.list_resource_templates()
        print("=============================")
        print(f"Available resources: {resources}")

        result = await client.call_tool("current_datetime", {"timezone": "America/New_York"})
        print("=============================")
        print(f"Result: {result}")

asyncio.run(main())