from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "village_links.db"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


@dataclass(frozen=True)
class VillageLink:
    link: str
    left_uri: str
    right_uri: str
    evidence_source: str
    sampled_at: str
    notes: str | None = None


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def initialise(path: Path = DB_PATH) -> None:
    with connect(path) as connection:
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def add_link(item: VillageLink, path: Path = DB_PATH) -> None:
    with connect(path) as connection:
        connection.execute(
            """
            INSERT OR IGNORE INTO village_links
                (link, left_uri, right_uri, evidence_source, sampled_at, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                item.link,
                item.left_uri,
                item.right_uri,
                item.evidence_source,
                item.sampled_at,
                item.notes,
            ),
        )


def all_links(path: Path = DB_PATH) -> list[sqlite3.Row]:
    with connect(path) as connection:
        return list(
            connection.execute(
                "SELECT * FROM village_links ORDER BY sampled_at DESC, id DESC"
            )
        )


def main() -> None:
    initialise()
    for row in all_links():
        print(f"{row['id']:>3}  {row['link']}")
        print(f"     {row['left_uri']}")
        print(f"  <-> {row['right_uri']}")
        print(f"     evidence: {row['evidence_source']} @ {row['sampled_at']}")


if __name__ == "__main__":
    main()
