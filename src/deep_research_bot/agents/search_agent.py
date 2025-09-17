from autogen_agentchat.agents import AssistantAgent
from autogen_ext.tools.langchain import LangChainToolAdapter
from langchain_tavily import TavilySearch
from langchain_community.tools import DuckDuckGoSearchResults

from deep_research_bot.config import settings
from deep_research_bot.model_client import client
from deep_research_bot.prompts import SEARCH_PROMPT


def _build_search_tool() -> LangChainToolAdapter:
    provider = settings.search_provider

    if provider == "tavily":
        return LangChainToolAdapter(TavilySearch(max_results=5))

    if provider == "duckduckgo":
        return LangChainToolAdapter(DuckDuckGoSearchResults())

    raise RuntimeError(f"Unsupported search provider: {provider}")


web_search_tool = _build_search_tool()

search_agent = AssistantAgent(
    name="search_agent",
    model_client=client,
    tools=[web_search_tool],
    system_message=SEARCH_PROMPT,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
