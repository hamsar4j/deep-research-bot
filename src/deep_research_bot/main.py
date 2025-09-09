import argparse
import asyncio
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from deep_research_bot.agents import planner_agent, search_agent, writer_agent
from deep_research_bot.model_client import client


def parse_args():
    parser = argparse.ArgumentParser(description="Deep Research Bot")
    parser.add_argument("task", nargs="*", help="The research task to investigate")
    return parser.parse_args()


async def run_research(task: str) -> None:
    team = RoundRobinGroupChat([planner_agent, search_agent, writer_agent], max_turns=3)
    await Console(
        team.run_stream(task=task),
        output_stats=True,
    )
    # Close the connection to the model client.
    await client.close()


def main() -> None:
    args = parse_args()
    if not args.task:
        print("Error: Please provide a research task.")
        print("Usage: deep-research-bot 'Your research query here'")
        return

    task = " ".join(args.task)
    asyncio.run(run_research(task))


if __name__ == "__main__":
    main()
