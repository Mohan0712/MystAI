from app.models.evidence.evidence import Evidence
from app.models.enums import AlertSeverity


class AnalysisService:
    """
    Performs analysis on investigation evidence.
    """

    def correlate(
        self,
        evidence_list: list[Evidence],
    ) -> list[Evidence]:
        """
        Correlate collected evidence.

        Currently returns the evidence unchanged.
        Future versions will correlate evidence
        using timelines, identities, processes,
        and network activity.
        """

        return evidence_list

    def calculate_risk(
        self,
        evidence_list: list[Evidence],
    ) -> float:
        """
        Calculate a risk score for the investigation.

        Current implementation is a simple heuristic.
        """

        score = 0.0

        for evidence in evidence_list:
            if evidence.confidence >= 0.9:
                score += 10

            elif evidence.confidence >= 0.7:
                score += 5

            else:
                score += 2

        return min(score, 100.0)

    def determine_severity(
        self,
        risk_score: float,
    ) -> AlertSeverity:
        """
        Determine alert severity based on risk score.
        """

        if risk_score >= 90:
            return AlertSeverity.CRITICAL

        if risk_score >= 70:
            return AlertSeverity.HIGH

        if risk_score >= 40:
            return AlertSeverity.MEDIUM

        if risk_score >= 20:
            return AlertSeverity.LOW

        return AlertSeverity.INFORMATIONAL

    def summarize(
        self,
        evidence_list: list[Evidence],
    ) -> str:
        """
        Generate a simple investigation summary.

        Future versions will use an LLM.
        """

        return (
            f"Collected "
            f"{len(evidence_list)} "
            f"evidence item(s)."
        )