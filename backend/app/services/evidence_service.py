from app.exceptions.evidence import (
    EvidenceAlreadyExistsError,
    EvidenceNotFoundError,
)
from app.models.evidence.evidence import Evidence
from app.models.evidence.types import EvidenceType


class EvidenceService:
    """
    Handles evidence associated with an investigation.
    """

    def add(
        self,
        evidence_list: list[Evidence],
        evidence: Evidence,
    ) -> None:
        """
        Add evidence to an investigation.
        """

        if any(item.id == evidence.id for item in evidence_list):
            raise EvidenceAlreadyExistsError(
                f"Evidence '{evidence.id}' already exists."
            )

        evidence_list.append(evidence)

    def remove(
        self,
        evidence_list: list[Evidence],
        evidence_id: str,
    ) -> None:
        """
        Remove evidence from an investigation.
        """

        for evidence in evidence_list:
            if evidence.id == evidence_id:
                evidence_list.remove(evidence)
                return

        raise EvidenceNotFoundError(
            f"Evidence '{evidence_id}' was not found."
        )

    def find(
        self,
        evidence_list: list[Evidence],
        evidence_id: str,
    ) -> Evidence:
        """
        Find evidence by ID.
        """

        for evidence in evidence_list:
            if evidence.id == evidence_id:
                return evidence

        raise EvidenceNotFoundError(
            f"Evidence '{evidence_id}' was not found."
        )

    def list(
        self,
        evidence_list: list[Evidence],
    ) -> list[Evidence]:
        """
        Return all evidence.
        """

        return evidence_list

    def find_by_type(
        self,
        evidence_list: list[Evidence],
        evidence_type: EvidenceType,
    ) -> list[Evidence]:
        """
        Return evidence of a specific type.
        """

        return [
            evidence
            for evidence in evidence_list
            if evidence.evidence_type == evidence_type
        ]

    def count(
        self,
        evidence_list: list[Evidence],
    ) -> int:
        """
        Return the number of evidence items.
        """

        return len(evidence_list)