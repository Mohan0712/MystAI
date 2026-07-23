from enum import Enum


class Severity(str, Enum):
    """Represents the severity of a security event."""

    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class InvestigationStatus(str, Enum):
    """Represents the lifecycle of an investigation."""

    OPEN = "OPEN"
    ENRICHING = "ENRICHING"
    ANALYZING = "ANALYZING"
    REPORT_GENERATED = "REPORT_GENERATED"
    UNDER_REVIEW = "UNDER_REVIEW"
    CLOSED = "CLOSED"


class EventSource(str, Enum):
    """Represents the origin of a security event."""

    EDR = "EDR"
    SIEM = "SIEM"
    IDS = "IDS"
    FIREWALL = "FIREWALL"
    CLOUD = "CLOUD"
    EMAIL = "EMAIL"
    API = "API"
    MANUAL = "MANUAL"


class IOCType(str, Enum):
    """Represents supported Indicator of Compromise types."""

    IP = "IP"
    DOMAIN = "DOMAIN"
    URL = "URL"
    SHA256 = "SHA256"
    MD5 = "MD5"
    EMAIL = "EMAIL"
    CVE = "CVE"


class Priority(str, Enum):
    """Represents investigation priority."""

    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"

class OperatingSystem(str, Enum):

    WINDOWS = "WINDOWS"

    LINUX = "LINUX"

    MACOS = "MACOS"

    ANDROID = "ANDROID"

    IOS = "IOS"

    UNKNOWN = "UNKNOWN"

class AssetType(str, Enum):

    ENDPOINT = "ENDPOINT"

    SERVER = "SERVER"

    VM = "VM"

    CONTAINER = "CONTAINER"

    NETWORK_DEVICE = "NETWORK_DEVICE"

    DATABASE = "DATABASE"

    APPLICATION = "APPLICATION"

    UNKNOWN = "UNKNOWN"

from enum import Enum


class InvestigationStatus(str, Enum):
    OPEN = "OPEN"
    TRIAGE = "TRIAGE"
    UNDER_INVESTIGATION = "UNDER_INVESTIGATION"
    CONTAINED = "CONTAINED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"