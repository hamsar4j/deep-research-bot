import argparse
import asyncio
from deep_research_bot.deep_research import run_research


def parse_args():
    parser = argparse.ArgumentParser(description="Deep Research Bot")
    parser.add_argument("task", nargs="*", help="The research task to investigate")
    return parser.parse_args()


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
