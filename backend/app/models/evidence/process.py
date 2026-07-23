from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class ProcessEvidence(Evidence):
    """
    Represents a process observed during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.PROCESS,
        frozen=True,
    )

    process_id: int = Field(gt=0)

    parent_process_id: Optional[int] = Field(
        default=None,
        gt=0,
    )

    process_name: str

    executable_path: str

    command_line: str

    process_start_time: datetime

    identity_id: Optional[str] = None

    sha256_hash: Optional[str] = None

    is_signed: bool = False

    signer: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )