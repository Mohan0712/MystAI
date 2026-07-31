from typing import Optional

from pydantic import ConfigDict, Field

from app.models.base import BaseEntity
from app.models.enums import AlertSeverity


class Analysis(BaseEntity):
    """
    Represents the AI-generated analysis of an investigation.

    It contains the AI's findings, reasoning, risk assessment,
    MITRE mappings, indicators of compromise (IOCs),
    and recommended remediation actions.
    """

    investigation_id: str = Field(
        description="Associated investigation."
    )

    executive_summary: str = Field(
        description="High-level summary of the investigation."
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Important observations made during analysis.",
    )

    reasoning: str = Field(
        description="Explanation supporting the AI's conclusions."
    )

    risk_score: float = Field(
        ge=0.0,
        le=100.0,
        description="Overall investigation risk score.",
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="AI confidence in its conclusions.",
    )

    severity: AlertSeverity = Field(
        description="Predicted severity of the incident."
    )

    mitre_techniques: list[str] = Field(
        default_factory=list,
        description="Mapped MITRE ATT&CK techniques.",
    )

    iocs: list[str] = Field(
        default_factory=list,
        description="Indicators of Compromise identified.",
    )

    recommendations: list[str] = Field(
        default_factory=list,
        description="Recommended remediation actions.",
    )

    analyst_notes: Optional[str] = Field(
        default=None,
        description="Optional notes added by the analyst.",
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )