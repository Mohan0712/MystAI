from uuid import uuid4

from app.models.alert import Alert
from app.models.enums import InvestigationStatus
from app.models.investigation import Investigation


class InvestigationService:
    """
    Handles investigation lifecycle operations.
    """

    VALID_STATUS_TRANSITIONS = {
        InvestigationStatus.OPEN: {
            InvestigationStatus.IN_PROGRESS,
        },
        InvestigationStatus.IN_PROGRESS: {
            InvestigationStatus.UNDER_REVIEW,
        },
        InvestigationStatus.UNDER_REVIEW: {
            InvestigationStatus.CLOSED,
        },
        InvestigationStatus.CLOSED: set(),
    }

    def create(self, alert: Alert) -> Investigation:
        """
        Create a new investigation from an alert.
        """
        return Investigation(
            id=str(uuid4()),
            alert_id=alert.id,
            status=InvestigationStatus.OPEN,
            analyst_id=None,
            risk_score=0.0,
            summary=None,
        )

    def assign_analyst(
        self,
        investigation: Investigation,
        analyst_id: str,
    ) -> None:
        """
        Assign an analyst to the investigation.
        """
        investigation.analyst_id = analyst_id

    def update_status(
        self,
        investigation: Investigation,
        new_status: InvestigationStatus,
    ) -> None:
        """
        Update the investigation status if the transition is valid.
        """
        allowed_transitions = self.VALID_STATUS_TRANSITIONS[
            investigation.status
        ]

        if new_status not in allowed_transitions:
            raise ValueError(
                f"Cannot transition from "
                f"{investigation.status.value} "
                f"to {new_status.value}."
            )

        investigation.status = new_status

    def update_risk_score(
        self,
        investigation: Investigation,
        score: float,
    ) -> None:
        """
        Update the investigation risk score.
        """
        investigation.risk_score = score

    def add_summary(
        self,
        investigation: Investigation,
        summary: str,
    ) -> None:
        """
        Add or update the investigation summary.
        """
        investigation.summary = summary