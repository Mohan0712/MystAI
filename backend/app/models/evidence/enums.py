
from enum import Enum


class DnsResponseCode(str, Enum):
    NOERROR = "NOERROR"
    NXDOMAIN = "NXDOMAIN"
    SERVFAIL = "SERVFAIL"
    REFUSED = "REFUSED"

class AuthenticationMethod(str, Enum):
    PASSWORD = "Password"
    KERBEROS = "Kerberos"
    NTLM = "NTLM"
    OAUTH = "OAuth"
    SAML = "SAML"