-- Minimal Type 2 test corpus for Issue #42.
-- Uses the existing prototype codec's percent-unreserved-v1 output.
-- INSERT IGNORE keeps this fixed corpus safe to load more than once.

SET NAMES utf8mb4;
SET time_zone = '+00:00';

INSERT IGNORE INTO endpoints (endpoint_uri) VALUES
    ('https://village.link/wiki/index.php/Asha_Bhosle'),
    ('https://en.wikipedia.org/wiki/Asha_Bhosle');

INSERT IGNORE INTO links (endpoint_a_id, endpoint_b_id)
SELECT a.endpoint_id, b.endpoint_id
FROM endpoints AS a
JOIN endpoints AS b
  ON b.endpoint_hash = SHA2('https://en.wikipedia.org/wiki/Asha_Bhosle', 256)
WHERE a.endpoint_hash = SHA2('https://village.link/wiki/index.php/Asha_Bhosle', 256);

INSERT IGNORE INTO encodings (
    encoding_name,
    encoding_version,
    description,
    definition
) VALUES (
    'percent-unreserved',
    'draft-0.1',
    'UTF-8 percent-encoding with only RFC 3986 unreserved characters literal; endpoints separated by one literal !.',
    JSON_OBJECT(
        'marker', 'https://wab.village.link/',
        'separator', '!',
        'literal_characters', 'A-Z a-z 0-9 - . _ ~',
        'source', 'docs/adr/006-village-link-serialization.md'
    )
);

INSERT IGNORE INTO representations (link_id, encoding_id, serialized_value)
SELECT l.link_id, e.encoding_id,
       'https://wab.village.link/https%3A%2F%2Fvillage.link%2Fwiki%2Findex.php%2FAsha_Bhosle!https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAsha_Bhosle'
FROM links AS l
JOIN endpoints AS a ON a.endpoint_id = l.endpoint_a_id
JOIN endpoints AS b ON b.endpoint_id = l.endpoint_b_id
JOIN encodings AS e
  ON e.encoding_name = 'percent-unreserved'
 AND e.encoding_version = 'draft-0.1'
WHERE a.endpoint_hash = SHA2('https://village.link/wiki/index.php/Asha_Bhosle', 256)
  AND b.endpoint_hash = SHA2('https://en.wikipedia.org/wiki/Asha_Bhosle', 256);
