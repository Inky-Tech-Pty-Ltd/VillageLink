# Village Link prototype

This directory is intentionally small and disposable. Its job is to get from architectural discussion to a working demonstration quickly.

## First slice

The prototype does four things:

1. stores Village Links in SQLite;
2. records the evidence/source URL and the time that evidence was sampled;
3. can list stored links from Python;
4. provides a tiny desktop browser which opens ordinary URLs normally and opens a demo Village Link as two side-by-side web views.

The demo URL encoding is **not** a proposed Village Link specification. It is only transport for the prototype browser:

`https://village.link/demo?left=<encoded-url>&right=<encoded-url>`

## Database

The first schema is deliberately boring:

- `link` — the Village Link URI used by the prototype;
- `left_uri` and `right_uri` — the two targets;
- `evidence_source` — where the equivalence assertion was observed;
- `sampled_at` — UTC datetime at which the evidence was sampled;
- `notes` — optional provenance/context notes.

SQLite is used so the Linux VM needs no database server.

## Run

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python scripts/init_db.py
villagelink-browser
```

The browser dependency (`PySide6`) is intentionally the only non-standard-library dependency.

## Steve Byrnes harvesting

`data/steve_byrnes_candidates.csv` contains candidate identity edges found during the first pass. Rows should only be promoted into the database once the stated evidence URL has actually been sampled. The Steve Byrnes homepage currently returns HTTP 403 to automated fetching, so homepage-derived claims are not marked as sampled yet.
