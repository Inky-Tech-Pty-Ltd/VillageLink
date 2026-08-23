CREATE TABLE IF NOT EXISTS village_links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT NOT NULL UNIQUE,
    left_uri TEXT NOT NULL,
    right_uri TEXT NOT NULL,
    evidence_source TEXT NOT NULL,
    sampled_at TEXT NOT NULL,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_village_links_sampled_at
    ON village_links(sampled_at);
