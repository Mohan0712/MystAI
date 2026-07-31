from app.models.analysis import Analysis
from app.models.evidence.evidence import Evidence
from app.models.enums import AlertSeverity
from app.models.investigation import Investigation


class AnalysisService:
    """
    Performs AI-driven analysis of an investigation.
    """

    def analyze(
        self,
        investigation: Investigation,
        evidence_list: list[Evidence],
    ) -> Analysis:
        """
        Analyze collected evidence and produce
        a structured Analysis object.
        """

        findings = self._extract_findings(
            evidence_list
        )

        risk_score = self._calculate_risk(
            evidence_list
        )

        severity = self._determine_severity(
            risk_score
        )

        recommendations = self._generate_recommendations(
            risk_score
        )

        return Analysis(
            investigation_id=investigation.id,
            executive_summary=self._generate_summary(
                findings
            ),
            findings=findings,
            reasoning=self._generate_reasoning(
                findings
            ),
            risk_score=risk_score,
            confidence=0.95,
            severity=severity,
            mitre_techniques=[],
            iocs=[],
            recommendations=recommendations,
        )

    def _extract_findings(
        self,
        evidence_list: list[Evidence],
    ) -> list[str]:
        """
        Extract findings from collected evidence.
        """

        return [
            f"{evidence.evidence_type.value} evidence collected."
            for evidence in evidence_list
        ]

    def _calculate_risk(
        self,
        evidence_list: list[Evidence],
    ) -> float:
        """
        Calculate investigation risk score.
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

    def _determine_severity(
        self,
        risk_score: float,
    ) -> AlertSeverity:
        """
        Convert risk score into severity.
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

    def _generate_summary(
        self,
        findings: list[str],
    ) -> str:
        """
        Generate executive summary.
        """

        return (
            f"The investigation produced "
            f"{len(findings)} finding(s)."
        )

    def _generate_reasoning(
        self,
        findings: list[str],
    ) -> str:
        """
        Generate reasoning behind conclusions.
        """

        return (
            "The analysis is based on "
            f"{len(findings)} correlated finding(s)."
        )

    def _generate_recommendations(
        self,
        risk_score: float,
    ) -> list[str]:
        """
        Generate remediation recommendations.
        """

        if risk_score >= 70:
            return [
                "Isolate the affected endpoint.",
                "Reset compromised credentials.",
                "Block identified IOCs.",
            ]

        return [
            "Continue monitoring the investigation."
        ]