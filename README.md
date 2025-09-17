# Deep Research Bot

A research bot that uses AutoGen agents to automatically research topics, gather information from the web, and generate comprehensive reports.

## Features

- **Automated Research**: Automatically breaks down complex queries into targeted web searches
- **Intelligent Information Gathering**: Uses AI to extract and synthesize relevant information from search results
- **Structured Reporting**: Generates well-organized markdown reports with key insights
- **Follow-up Suggestions**: Provides thoughtful questions for further research

## How It Works

The Deep Research Bot uses a short clarification phase followed by four specialized AI agents:

0. **Clarification (User Proxy + Clarifier Agent)**: Runs as a separate short team to refine your request. Once the clarifier returns a structured `clarified_task`, it automatically becomes the input for the main research flow.
1. **Planner Agent**: Analyzes your query and creates a research plan with targeted search terms
2. **Search Agent**: Executes web searches and extracts relevant information
3. **Writer Agent**: Synthesizes all findings into a cohesive, well-structured report
4. **Review Agent**: Critically evaluates the report for accuracy, completeness, sourcing, and clarity, returning structured feedback

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
MODEL_FAMILY=LLAMA_4_SCOUT
SEARCH_PROVIDER=tavily
TAVILY_API_KEY=your_tavily_key_here
```

### Environment Variables

- `OPENAI_API_KEY`: Your API key for the LLM provider
- `LLM`: The model identifier (default: meta-llama/Llama-4-Scout-17B-16E-Instruct)
- `BASE_URL`: The API endpoint URL (default: <https://api.together.xyz/v1>)
- `MODEL_FAMILY`: The model family identifier (default: LLAMA_4_SCOUT)
- `SEARCH_PROVIDER`: Optional. Set to `tavily` (default) or `duckduckgo` to choose the web search adapter.
- `TAVILY_API_KEY`: Required when `SEARCH_PROVIDER=tavily`; used by the Tavily web search integration.

### Search Providers

By default the bot uses the Tavily API via LangChain. Supply `SEARCH_PROVIDER=tavily` (default) and `TAVILY_API_KEY` to enable it. If you'd prefer a no-key option, set `SEARCH_PROVIDER=duckduckgo` to switch to the DuckDuckGo search tool without changing the agent code.

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
│   ├── clarifier_agent.py  # Clarifies the initial task with the user
│   ├── planner_agent.py    # Creates research plans
│   ├── search_agent.py     # Executes web searches
│   ├── writer_agent.py     # Generates reports
│   └── review_agent.py     # Reviews reports and outputs structured feedback
├── config.py              # Configuration management
├── model_client.py        # LLM client setup
├── models.py              # Data models (plans, report data, review feedback)
├── prompts.py             # Agent prompt templates
└── main.py                # Main entry point
```

## Review Stage

- The Review Agent outputs structured JSON with an overall rating, strengths, issues with severities, priority actions, risk flags, and a short summary.
- Termination: The chat stops when either the message cap is reached or a unique token is detected.
  - The reviewer optionally includes `"approval_token": "__APPROVE__"` in the JSON only when the output is publishable with minimal/no edits (rating >= 4 and no major/critical issues).
  - Otherwise the field is omitted. The special token triggers the termination condition without breaking the JSON-only contract.

## Clarification Stage

- The Clarifier Agent asks only necessary questions; answer as needed to resolve ambiguities quickly.
- Each clarifier reply is structured as a `ClarifierResponse` JSON object that includes a `clarified_task` field.
- When the agent signals `need_clarification = "__FALSE__"`, the latest `clarified_task` is automatically promoted to the research task.
- No manual copy/paste step is required—the clarified task flows directly into the planner/search/writer/review team.

## Dependencies

- [AutoGen AgentChat](https://microsoft.github.io/autogen/): Multi-agent conversation framework
- [LangChain](https://github.com/langchain-ai/langchain): LLM application framework
- [Tavily Search](https://docs.tavily.com/): Web search integration via LangChain
- [Pydantic](https://docs.pydantic.dev/): Data validation and settings management

## License

This project is licensed under the MIT License - see the LICENSE file for details.
