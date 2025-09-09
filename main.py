from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from deep_research_bot.agents import planner_agent, search_agent, writer_agent
from deep_research_bot.model_client import client
import asyncio

team = RoundRobinGroupChat([planner_agent, search_agent, writer_agent], max_turns=3)


# Run the agent and stream the messages to the console.
async def main() -> None:
    await Console(
        team.run_stream(
            task="Write a report on the impact of climate change on marine life."
        ),
        output_stats=True,
    )
    # Close the connection to the model client.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
