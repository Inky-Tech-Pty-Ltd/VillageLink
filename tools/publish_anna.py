from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API_URL = os.environ.get("ANNA_API_URL", "https://village.link/wiki/api.php")
ACCESS_TOKEN = os.environ.get("ANNA_OAUTH_ACCESS_TOKEN")
MANIFEST = Path(os.environ.get("ANNA_MANIFEST", "anna/manifest.json"))
USER_AGENT = "Puck-GPT VillageLink/1.0 (puck.gpt@village.link)"


def api(params: dict[str, str], *, post: bool = False) -> dict:
    if not ACCESS_TOKEN:
        raise RuntimeError("ANNA_OAUTH_ACCESS_TOKEN is not set")

    params = {**params, "format": "json", "formatversion": "2"}
    encoded = urllib.parse.urlencode(params).encode("utf-8")

    if post:
        request = urllib.request.Request(API_URL, data=encoded, method="POST")
    else:
        request = urllib.request.Request(f"{API_URL}?{encoded.decode('utf-8')}")

    request.add_header("Authorization", f"Bearer {ACCESS_TOKEN}")
    request.add_header("User-Agent", USER_AGENT)
    if post:
        request.add_header("Content-Type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(request) as response:
        payload = json.load(response)

    if "error" in payload:
        raise RuntimeError(json.dumps(payload["error"], indent=2))

    return payload


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = manifest.get("pages", [])

    userinfo = api({"action": "query", "meta": "userinfo"})["query"]["userinfo"]
    username = userinfo.get("name")
    if username != "Puck-GPT":
        raise RuntimeError(f"Expected OAuth identity Puck-GPT, got {username!r}")

    csrf = api({"action": "query", "meta": "tokens", "type": "csrf"})["query"]["tokens"]["csrftoken"]

    for page in pages:
        title = page["title"]
        source = Path(page["source"])
        text = source.read_text(encoding="utf-8")
        summary = page.get("summary", "Publish from VillageLink GitHub repository")

        result = api(
            {
                "action": "edit",
                "title": title,
                "text": text,
                "token": csrf,
                "summary": summary,
                "bot": "1",
            },
            post=True,
        )

        edit = result.get("edit", {})
        print(f"{title}: {edit.get('result', 'UNKNOWN')} rev={edit.get('newrevid', '-')}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"publish_anna.py: {exc}", file=sys.stderr)
        raise
