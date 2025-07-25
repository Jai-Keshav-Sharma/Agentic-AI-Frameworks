import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from dotenv import load_dotenv

load_dotenv(override=True)

async def main():
    # Step 1: Fetch tool setup
    fetch_mcp_server = StdioServerParams(command='uvx', args=['mcp-server-fetch'], read_timeout_seconds=30)
    fetcher = await mcp_server_tools(fetch_mcp_server)

    # Step 2: Model client
    model_client = OpenAIChatCompletionClient(model='gpt-4o-mini')

    # Step 3: Agent with tools
    agent = AssistantAgent(
        name="fetcher",
        model_client=model_client,
        tools=fetcher,
        reflect_on_tool_use=True
    )

    # Step 4: Run task
    result = await agent.run(task="Review 'https://www.vlr.gg/' and tell me about the upcoming valorant matches. Reply in Markdown.")

    # Step 5: Print the result
    print(result.messages[-1].content)

# Run the async main
if __name__ == "__main__":
    asyncio.run(main())
