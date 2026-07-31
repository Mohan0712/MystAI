from datetime import datetime, timezone

from pydantic import ConfigDict, Field

from app.models.base import BaseEntity


class Report(BaseEntity):
    """
    Represents a generated investigation report.

    A report is a formatted representation of an Analysis
    that can be exported as PDF, JSON, HTML, Markdown,
    or displayed in the MystAI dashboard.
    """

    analysis_id: str = Field(
        description="Associated analysis."
    )

    content: str = Field(
        description="Formatted report content."
    )

    report_format: str = Field(
        description="Output format (PDF, JSON, HTML, Markdown)."
    )

    generated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when the report was generated.",
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )