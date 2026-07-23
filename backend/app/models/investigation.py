from typing import Optional

from pydantic import Field

from app.models.base import BaseEntity
from app.models.enums import InvestigationStatus


class Investigation(BaseEntity):
    """
    Represents the investigation of a security alert.
    """

    alert_id: str

    status: InvestigationStatus = InvestigationStatus.OPEN

    analyst_id: Optional[str] = None

    risk_score: float = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
    )

    summary: Optional[str] = None