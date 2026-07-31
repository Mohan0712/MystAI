class AlertError(Exception):
    """Base exception for alert-related errors."""


class InvalidAlertStatusTransitionError(AlertError):
    """Raised when an invalid alert status transition is attempted."""