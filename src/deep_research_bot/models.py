from typing import Literal
from pydantic import BaseModel


class ClarifierResponse(BaseModel):
    need_clarification: Literal["__FALSE__", "__TRUE__"]
    """Whether the agent must ask the user for more information."""

    question: str
    """Clarifying question to present when more detail is required."""

    verification: str
    """Acknowledgement that research can begin once requirements are met."""

    clarified_task: str
    """Concise task statement summarizing the agreed scope."""


class WebSearchItem(BaseModel):
    reason: str
    """Your reasoning for why this search is important to the query."""

    query: str
    """The search term to use for the web search."""


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """The list of web searches to perform to best answer the query."""


class ReportData(BaseModel):
    short_summary: str
    """A short 2-3 sentence summary of the findings."""

    markdown_report: str
    """The final report"""

    follow_up_questions: list[str]
    """Suggested topics to research further"""


class ReviewIssue(BaseModel):
    category: str
    """Category of the issue (factual_accuracy, structure, clarity, sourcing, bias, completeness, style)."""

    severity: str
    """One of: minor, moderate, major, critical."""

    location: str | None = None
    """Optional section / heading / line reference if identifiable."""

    description: str
    """Clear explanation of the problem."""

    suggested_fix: str
    """Concise actionable recommendation to resolve it."""


class ReviewFeedback(BaseModel):
    overall_rating: int
    """Integer 1-5 (5 = excellent, publishable with minimal/no edits)."""

    strengths: list[str]
    """List of notable positives (clarity, depth, balance, synthesis quality, etc.)."""

    issues: list[ReviewIssue]
    """List of identified issues with recommended fixes."""

    priority_actions: list[str]
    """Ordered list (highest priority first) of 3-7 actions that would most improve the report."""

    risk_flags: list[str]
    """Potential high-risk concerns (e.g., hallucination risk, outdated data, unsupported causal claim)."""

    summary: str
    """1 short paragraph (<= 80 words) summarizing review stance and next-step focus."""

    approval_token: str | None = None
    """Optional approval signal. Include value "__APPROVE__" only if publishable with minimal/no edits."""
