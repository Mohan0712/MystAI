from enum import Enum


class EvidenceType(str, Enum):
    PROCESS = "PROCESS"
    NETWORK = "NETWORK"
    FILE = "FILE"
    REGISTRY = "REGISTRY"
    DNS = "DNS"
    EMAIL = "EMAIL"
    AUTHENTICATION = "AUTHENTICATION"