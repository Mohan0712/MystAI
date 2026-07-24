from pathlib import Path
from typing import Optional

from pydantic import ConfigDict, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class FileEvidence(Evidence):
    """
    Represents a file collected during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.FILE,
        frozen=True,
    )

    file_name: str

    file_path: Path

    sha256_hash: str

    file_size: Optional[int] = Field(
        default=None,
        ge=0,
    )

    process_id: Optional[int] = Field(
        default=None,
        gt=0,
    )

    is_signed: bool = False

    signer: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )