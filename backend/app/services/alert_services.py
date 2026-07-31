from uuid import uuid4
from typing import Optional
from app.exceptions.alert import (
    InvalidAlertStatusTransitionError,
)
from app.models.alert import Alert
from app.models.enums import (
    AlertSeverity,
    AlertStatus,
)
from backend.app.models import alert

class AlertService:
    """
    Handles the lifecycle of security alerts.
    """
    VALID_STATUS_TRANSITIONS = {
    AlertStatus.NEW: {
        AlertStatus.ACKNOWLEDGED,
    },
    AlertStatus.ACKNOWLEDGED: {
        AlertStatus.INVESTIGATION_CREATED,
    },
    AlertStatus.INVESTIGATION_CREATED: {
        AlertStatus.CLOSED,
    },
    AlertStatus.CLOSED: set(),
}
    def create(
    self,
    title: str,
    description: str,
    severity: AlertSeverity,
    asset_id: str,
    confidence_score: Optional[float] = None
) -> Alert:
       return Alert(
        id=str(uuid4()),
        title=title,
        description=description,
        severity=severity,
        status=AlertStatus.NEW,
        asset_id=asset_id,
        investigation_id=None,
        confidence_score=confidence_score,
    )

    def acknowledge(
    self,
    alert: Alert,
) -> None:

        self._update_status(
        alert,
        AlertStatus.ACKNOWLEDGED,
    )

    def mark_investigation_created(
    self,
    alert: Alert,
    investigation_id: str,
) -> None: 
        alert.investigation_id = investigation_id

        self._update_status(
        alert,
        AlertStatus.INVESTIGATION_CREATED,
    )

    def close(
    self,
    alert: Alert,
) -> None:
        self._update_status(
        alert,
        AlertStatus.CLOSED,
    )

    def _update_status(
    self,
    alert: Alert,
    new_status: AlertStatus,
) -> None:

        self._validate_transition(
        alert.status,
        new_status,
    )

    alert.status = new_status

    def _validate_transition(
    self,
    current_status: AlertStatus,
    new_status: AlertStatus,
) -> None:

        allowed = self.VALID_STATUS_TRANSITIONS[current_status]

        if new_status not in allowed:
            raise InvalidAlertStatusTransitionError(
            f"Cannot transition from "
            f"{current_status.value} "
            f"to {new_status.value}."
        )