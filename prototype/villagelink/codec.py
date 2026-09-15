"""Draft Village Link serialization codec.

Endpoint URIs are UTF-8 percent-encoded with only RFC 3986 unreserved
characters left literal, then separated by a single literal ``!``.  The
publishing domain is part of the serialized form; ``village.link`` is only
the reference default.
"""

from urllib.parse import quote, unquote, urlparse

DEFAULT_DOMAIN = "village.link"
_UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"


def encode_endpoint(uri: str) -> str:
    """Encode one endpoint URI for embedding in a Village Link."""
    return quote(uri, safe=_UNRESERVED, encoding="utf-8", errors="strict")


def decode_endpoint(encoded: str) -> str:
    """Recover an endpoint URI, decoding exactly one percent-encoding layer."""
    return unquote(encoded, encoding="utf-8", errors="strict")


def marker_for(domain: str = DEFAULT_DOMAIN) -> str:
    """Return the HTTPS ``wab`` marker for a publishing domain."""
    domain = domain.strip().lower().rstrip(".")
    if not domain or "/" in domain or ":" in domain or " " in domain:
        raise ValueError("domain must be a bare DNS domain such as village.link")
    return f"https://wab.{domain}/"


def make(a: str, b: str, domain: str = DEFAULT_DOMAIN) -> str:
    """Compose a Village Link from publishing domain and endpoint URIs A and B."""
    return f"{marker_for(domain)}{encode_endpoint(a)}!{encode_endpoint(b)}"


def parse_with_domain(link: str) -> tuple[str, str, str]:
    """Parse a Village Link and return ``(domain, A, B)``."""
    parsed = urlparse(link)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or not host.startswith("wab.") or len(host) <= 4:
        raise ValueError("not a Village Link marker")
    if parsed.params or parsed.query or parsed.fragment:
        raise ValueError("Village Link marker must not contain params, query or fragment")

    payload = parsed.path.lstrip("/")
    if payload.count("!") != 1:
        raise ValueError("Village Link payload must contain exactly one literal ! separator")

    encoded_a, encoded_b = payload.split("!", 1)
    if not encoded_a or not encoded_b:
        raise ValueError("Village Link endpoints must not be empty")

    return host[4:], decode_endpoint(encoded_a), decode_endpoint(encoded_b)


def parse(link: str) -> tuple[str, str]:
    """Parse a Village Link and return the original endpoint URI pair."""
    _, a, b = parse_with_domain(link)
    return a, b
