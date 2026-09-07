"""Draft Village Link serialization codec.

This implements the conservative candidate encoding described in ADR-006:
endpoint URIs are UTF-8 percent-encoded with only RFC 3986 unreserved
characters left literal, then separated by a single literal ``!``.
"""

from urllib.parse import quote, unquote

DEFAULT_MARKER = "https://wab.village.link/"
_UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"


def encode_endpoint(uri: str) -> str:
    """Encode one endpoint URI for embedding in a Village Link."""
    return quote(uri, safe=_UNRESERVED, encoding="utf-8", errors="strict")


def decode_endpoint(encoded: str) -> str:
    """Recover an endpoint URI, decoding exactly one percent-encoding layer."""
    return unquote(encoded, encoding="utf-8", errors="strict")


def make(a: str, b: str, marker: str = DEFAULT_MARKER) -> str:
    """Compose a Village Link from endpoint URIs A and B."""
    return f"{marker}{encode_endpoint(a)}!{encode_endpoint(b)}"


def parse(link: str, marker: str = DEFAULT_MARKER) -> tuple[str, str]:
    """Parse a Village Link and return the original endpoint URI pair."""
    if not link.startswith(marker):
        raise ValueError("not a Village Link for the expected marker")

    payload = link[len(marker) :]
    if payload.count("!") != 1:
        raise ValueError("Village Link payload must contain exactly one literal ! separator")

    encoded_a, encoded_b = payload.split("!", 1)
    if not encoded_a or not encoded_b:
        raise ValueError("Village Link endpoints must not be empty")

    return decode_endpoint(encoded_a), decode_endpoint(encoded_b)
