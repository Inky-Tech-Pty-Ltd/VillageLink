"""Draft codec for a self-contained, two-ended ``vl:`` URI.

Endpoint URIs are opaque strings encoded as UTF-8 percent escapes, leaving
only RFC 3986 unreserved characters literal. One literal ``!`` separates
the endpoints; the publisher is not part of the Village Link URI.
"""

import re
from urllib.parse import quote, unquote

_UNRESERVED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
_BAD_PERCENT_ESCAPE = re.compile(r"%(?![0-9A-Fa-f]{2})")


def encode_endpoint(uri: str) -> str:
    """Encode an endpoint URI without interpreting its contents."""
    return quote(uri, safe=_UNRESERVED, encoding="utf-8", errors="strict")


def decode_endpoint(encoded: str) -> str:
    """Decode exactly one percent-encoding layer."""
    if _BAD_PERCENT_ESCAPE.search(encoded):
        raise ValueError("endpoint contains malformed percent-encoding")
    try:
        return unquote(encoded, encoding="utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ValueError("endpoint contains invalid UTF-8 percent-encoding") from exc


def make(a: str, b: str) -> str:
    """Compose a Village Link from two endpoint URIs."""
    if not a or not b:
        raise ValueError("Village Link endpoints must not be empty")
    return f"vl:{encode_endpoint(a)}!{encode_endpoint(b)}"


def parse(link: str) -> tuple[str, str]:
    """Recover the ordered pair of endpoint URIs from a Village Link."""
    if not link.startswith("vl:"):
        raise ValueError("not a Village Link URI")
    payload = link[3:]
    if payload.count("!") != 1:
        raise ValueError("Village Link payload must contain exactly one literal ! separator")
    encoded_a, encoded_b = payload.split("!", 1)
    if not encoded_a or not encoded_b:
        raise ValueError("Village Link endpoints must not be empty")
    return decode_endpoint(encoded_a), decode_endpoint(encoded_b)
