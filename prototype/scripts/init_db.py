from urllib.parse import quote

from villagelink.db import VillageLink, add_link, initialise


def demo_link(left: str, right: str) -> str:
    return (
        "https://village.link/demo"
        f"?left={quote(left, safe='')}"
        f"&right={quote(right, safe='')}"
    )


def main() -> None:
    initialise()

    samples = [
        VillageLink(
            link=demo_link(
                "https://sjbyrnes.com",
                "https://github.com/sbyrnes321",
            ),
            left_uri="https://sjbyrnes.com",
            right_uri="https://github.com/sbyrnes321",
            evidence_source="https://github.com/sbyrnes321/tmm",
            sampled_at="2026-08-21T04:02:00Z",
            notes=(
                "GitHub repository identifies Steven Byrnes as author and links "
                "to sjbyrnes.com as the author homepage. First prototype sample; "
                "evidence sampled from public web search result."
            ),
        ),
        VillageLink(
            link=demo_link(
                "https://sjbyrnes.com",
                "https://physics.stackexchange.com/users/3811/steve-byrnes",
            ),
            left_uri="https://sjbyrnes.com",
            right_uri="https://physics.stackexchange.com/users/3811/steve-byrnes",
            evidence_source="https://physics.stackexchange.com/users/3811/steve-byrnes",
            sampled_at="2026-08-21T04:02:00Z",
            notes=(
                "Physics Stack Exchange profile is named Steve Byrnes and lists "
                "sjbyrnes.com. First prototype sample."
            ),
        ),
    ]

    for item in samples:
        add_link(item)

    print(f"Initialised database with {len(samples)} first-pass Village Links.")


if __name__ == "__main__":
    main()
