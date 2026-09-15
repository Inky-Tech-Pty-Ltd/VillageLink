"""Draft Village Link serialization codec.

Endpoint URIs are UTF-8 percent-encoded with only RFC 3986 unreserved
characters left literal, then separated by a single literal ``!``.  The
publishing domain is part of the serialized form; ``village.link`` is only
the reference default.
"""

import re
from urllib.parse import quote, unquote, urlparse

DEFAULT_DOMAIN = "village.link"
_UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
_BAD_PERCENT_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")


def encode_endpoint(uri: str) -> str:
    """Encode one endpoint URI for embedding in a Village Link."""
    return quote(uri, safe=_UNRESERVED, encoding="utf-8", errors="strict")


def decode_endpoint(encoded: str) -> str:
    """Recover an endpoint URI, decoding exactly one percent-encoding layer."""
    if _BAD_PERCENT_ESCAPE.search(encoded):
        raise ValueError("endpoint contains malformed percent-encoding")
    try:
        return unquote(encoded, encoding="utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("endpoint contains invalid UTF-8 percent-encoding") from exc


def _normalise_domain(domain: str) -> str:
    """Validate and normalise a bare DNS domain used beneath the ``wab`` label."""
    domain = domain.strip().lower().rstrip(".")
    if not domain:
        raise ValueError("domain must be a bare DNS domain such as village.link")

    labels = domain.split(".")
    if any(not label for label in labels):
        raise ValueError("domain must not contain empty DNS labels")

    try:
        ascii_labels = [label.encode("idna").decode("ascii") for label in labels]
    except UnicodeError as exc:
        raise ValueError("domain contains an invalid internationalised DNS label") from exc

    for label in ascii_labels:
        if len(label) > 63:
            raise ValueError("domain contains a DNS label longer than 63 octets")
        if label.startswith("-") or label.endswith("-"):
            raise ValueError("DNS labels must not start or end with a hyphen")
        if not re.fullmatch(r"[a-z0-9-]+", label, flags=re.IGNORECASE):
            raise ValueError("domain contains characters not permitted in a DNS label")

    if len(".".join(ascii_labels)) > 253:
        raise ValueError("domain is longer than the DNS limit")

    return domain


def marker_for(domain: str = DEFAULT_DOMAIN) -> str:
    """Return the HTTPS ``wab`` marker for a publishing domain."""
    return f"https://wab.{_normalise_domain(domain)}/"


def make(a: str, b: str, domain: str = DEFAULT_DOMAIN) -> str:
    """Compose a Village Link from publishing domain and endpoint URIs A and B."""
    return f"{marker_for(domain)}{encode_endpoint(a)}!{encode_endpoint(b)}"


def parse_with_domain(link: str) -> tuple[str, str, str]:
    """Parse a Village Link and return ``(domain, A, B)``."""
    parsed = urlparse(link)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or not host.startswith("wab.") or len(host) <= 4:
        raise ValueError("not a Village Link marker")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Village Link marker must not contain userinfo")
    try:
        port = parsed.port
    except ValueError as exc:
        raise ValueError("Village Link marker contains an invalid port") from exc
    if port is not None:
        raise ValueError("Village Link marker must not contain a port")
    if parsed.params or parsed.query or parsed.fragment:
        raise ValueError("Village Link marker must not contain params, query or fragment")
    if not parsed.path.startswith("/") or parsed.path.startswith("//"):
        raise ValueError("Village Link payload must begin with exactly one path slash")

    domain = _normalise_domain(host[4:])
    payload = parsed.path[1:]
    if payload.count("!") != 1:
        raise ValueError("Village Link payload must contain exactly one literal ! separator")

    encoded_a, encoded_b = payload.split("!", 1)
    if not encoded_a or not encoded_b:
        raise ValueError("Village Link endpoints must not be empty")

    return domain, decode_endpoint(encoded_a), decode_endpoint(encoded_b)


def parse(link: str) -> tuple[str, str]:
    """Parse a Village Link and return the original endpoint URI pair."""
    _, a, b = parse_with_domain(link)
    return a, b
