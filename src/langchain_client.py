# Use server from examples/servers/streamable-http-stateless/

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools
import asyncio

load_dotenv()

async def main():
    async with streamablehttp_client("http://127.0.0.1:8001/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)
            agent = create_react_agent("openai:gpt-4.1", tools)
            math_response = await agent.ainvoke({"messages": "what time is in San Francisco?"})
            
            # Extract and print the AI's response
            for message in math_response['messages']:
                if hasattr(message, 'content'):
                    print("\nResponse:")
                    print(message.content)

if __name__ == "__main__":
    asyncio.run(main())