class InvestigationError(Exception):
    """Base exception for investigation-related errors."""


class InvalidStatusTransitionError(InvestigationError):
    """Raised when an invalid investigation status transition is attempted."""