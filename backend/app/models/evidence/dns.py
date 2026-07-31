from ipaddress import IPv4Address, IPv6Address
from typing import Optional

from pydantic import ConfigDict, Field
from app.models.evidence.enums import DnsResponseCode
from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class DnsEvidence(Evidence):
    """
    Represents a DNS query observed during an investigation.
    """

    evidence_type: EvidenceType = Field(
        default=EvidenceType.DNS,
        frozen=True,
    )

    query_name: str

    resolved_ip: IPv4Address | IPv6Address

    process_id: Optional[int] = Field(
        default=None,
        gt=0,
    )

    dns_server: Optional[IPv4Address | IPv6Address] = None

    response_code: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
    )