from typing import Optional

from pydantic import ConfigDict, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class RegistryEvidence(Evidence):
    """
    Represents a Windows Registry artifact collected during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.REGISTRY,
        frozen=True,
    )

    registry_key: str

    value_name: str

    value_data: str

    value_type: Optional[str] = None

    process_id: Optional[int] = Field(
        default=None,
        gt=0,
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )