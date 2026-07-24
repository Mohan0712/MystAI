from ipaddress import IPv4Address, IPv6Address
from typing import Optional

from pydantic import ConfigDict, Field

from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class NetworkEvidence(Evidence):
    """
    Represents a network connection observed during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.NETWORK,
        frozen=True,
    )

    source_ip: IPv4Address | IPv6Address

    destination_ip: IPv4Address | IPv6Address

    source_port: Optional[int] = Field(
        default=None,
        ge=1,
        le=65535,
    )

    destination_port: int = Field(
        ge=1,
        le=65535,
    )

    protocol: str

    process_id: Optional[int] = Field(
        default=None,
        gt=0,
    )

    domain_name: Optional[str] = None

    bytes_sent: Optional[int] = Field(
        default=None,
        ge=0,
    )

    bytes_received: Optional[int] = Field(
        default=None,
        ge=0,
    )

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )