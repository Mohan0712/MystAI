"""
Base domain models for MystAI.

This module contains the foundational models shared across the
entire domain layer.
"""

from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, ConfigDict

class Metadata(BaseModel):
    """
    Metadata associated with every domain entity.
    """

    created_at: datetime = datetime.now(timezone.utc)
    updated_at: datetime = datetime.now(timezone.utc)
    version: int = 1

    source: Optional[str] = None
    vendor: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True
    )

class BaseEntity(BaseModel):
    """
    Base class for every business entity in MystAI.
Represents the common foundation for all business entities
within the MystAI domain.

Every domain entity has a unique identifier and associated
metadata used for auditing, versioning, and lifecycle tracking.
    """

    id: str

    metadata: Metadata

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True
    )