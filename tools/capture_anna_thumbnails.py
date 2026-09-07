from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright


OUTPUT_DIR = Path("anna/generated")

TARGETS = [
    {
        "url": "https://en.wikipedia.org/wiki/Asha_Bhosle",
        "output": OUTPUT_DIR / "Asha-Bhosle-Wikipedia.png",
    },
]


def capture(url: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        page.goto(url, wait_until="networkidle", timeout=60_000)
        page.screenshot(path=str(output), full_page=False)
        browser.close()


if __name__ == "__main__":
    for target in TARGETS:
        capture(target["url"], target["output"])
        print(f"Captured {target['url']} -> {target['output']}")
