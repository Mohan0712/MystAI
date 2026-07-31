class EvidenceError(Exception):
    """Base exception for evidence-related errors."""


class EvidenceAlreadyExistsError(EvidenceError):
    """Raised when duplicate evidence is added."""


class EvidenceNotFoundError(EvidenceError):
    """Raised when evidence cannot be found."""