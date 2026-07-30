from ipaddress import IPv4Address, IPv6Address
from typing import Optional

from pydantic import ConfigDict, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class AuthenticationEvidence(Evidence):
    """
    Represents an authentication event observed during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.AUTHENTICATION,
        frozen=True,
    )

    identity_id: str

    success: bool

    source_ip: Optional[IPv4Address | IPv6Address] = None

    authentication_method: Optional[str] = None

    mfa_used: Optional[bool] = None

    failure_reason: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )