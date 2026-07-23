from datetime import datetime, timezone

from pydantic import ConfigDict, Field

from app.models.base import BaseEntity
from backend.app.models.evidence.types import EvidenceType


class Evidence(BaseEntity):
    """
    Base class for all evidence collected during an investigation.
    """

    investigation_id: str

    evidence_type: EvidenceType

    source: str = Field(
    description="Origin of the evidence (e.g. Sysmon, CrowdStrike, VirusTotal)"
)

    collected_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )