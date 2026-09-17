"""Compatibility launcher for the prototype browser.

The browser home page is now domain-aware directly, so this module simply
preserves the installed ``villagelink-browser`` entry point.
"""

from . import browser


def main() -> int:
    return browser.main()


if __name__ == "__main__":
    raise SystemExit(main())
