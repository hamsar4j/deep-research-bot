from autogen_agentchat.agents import AssistantAgent
from deep_research_bot.model_client import client
from deep_research_bot.prompts import SEARCH_PROMPT
from langchain_community.tools import DuckDuckGoSearchResults
from autogen_ext.tools.langchain import LangChainToolAdapter

web_search_tool = LangChainToolAdapter(DuckDuckGoSearchResults())

search_agent = AssistantAgent(
    name="search_agent",
    model_client=client,
    tools=[web_search_tool],
    system_message=SEARCH_PROMPT,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
