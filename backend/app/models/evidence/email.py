from typing import Optional
from pydantic import ConfigDict, EmailStr, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class EmailEvidence(Evidence):
    """
    Represents an email observed during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.EMAIL,
        frozen=True,
    )

    sender: str

    recipient: str

    subject: str

    message_id: str

    attachment_name: Optional[str] = None

    attachment_hash: Optional[str] = None

    reply_to: Optional[EmailStr] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )