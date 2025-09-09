# Deep Research Bot

A research bot that uses AutoGen agents to automatically research topics, gather information from the web, and generate comprehensive reports.

## Features

- **Automated Research**: Automatically breaks down complex queries into targeted web searches
- **Intelligent Information Gathering**: Uses AI to extract and synthesize relevant information from search results
- **Structured Reporting**: Generates well-organized markdown reports with key insights
- **Follow-up Suggestions**: Provides thoughtful questions for further research

## How It Works

The Deep Research Bot uses three specialized AI agents working in sequence:

1. **Planner Agent**: Analyzes your query and creates a research plan with targeted search terms
2. **Search Agent**: Executes web searches and extracts relevant information
3. **Writer Agent**: Synthesizes all findings into a cohesive, well-structured report

## Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- API key from a supported LLM provider (Together AI, OpenAI, etc.)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd deep-research-bot
   ```

2. Install dependencies using uv:

   ```bash
   uv pip install -e .
   ```

## Configuration

Create a `.env` file in the project root with your API credentials:

```env
OPENAI_API_KEY=your_api_key_here
LLM=meta-llama/Llama-4-Scout-17B-16E-Instruct
BASE_URL=https://api.together.xyz/v1
MODEL_FAMILY=llama_4_scout
```

### Environment Variables

- `OPENAI_API_KEY`: Your API key for the LLM provider
- `LLM`: The model identifier (default: meta-llama/Llama-4-Scout-17B-16E-Instruct)
- `BASE_URL`: The API endpoint URL (default: <https://api.together.xyz/v1>)
- `MODEL_FAMILY`: The model family identifier (default: LLAMA_4_SCOUT)

## Usage

After installation, you can run the research bot with:

```bash
deep-research-bot "Your research query here"
```

### Examples

```bash
# Investigate technology trends
deep-research-bot "How is artificial intelligence transforming the healthcare industry?"
```

## Project Structure

```md
src/deep_research_bot/
├── agents/                 # AI agent implementations
│   ├── planner_agent.py    # Creates research plans
│   ├── search_agent.py     # Executes web searches
│   └── writer_agent.py     # Generates reports
├── config.py              # Configuration management
├── model_client.py        # LLM client setup
├── models.py              # Data models
├── prompts.py             # Agent prompt templates
└── main.py                # Main entry point
```

## Dependencies

- [AutoGen AgentChat](https://microsoft.github.io/autogen/): Multi-agent conversation framework
- [LangChain](https://github.com/langchain-ai/langchain): LLM application framework
- [DuckDuckGo Search](https://github.com/deedy5/ddgs): Web search integration
- [Pydantic](https://docs.pydantic.dev/): Data validation and settings management

## License

This project is licensed under the MIT License - see the LICENSE file for details.
