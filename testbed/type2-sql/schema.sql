-- Village Link Type 2 testbed
-- Minimal four-table backing store for Issue #42.
-- This database is not W. A web publisher creates W from these records.
-- Tested on MariaDB 10.5; utf8mb4_unicode_ci also remains portable to MySQL.

SET NAMES utf8mb4;
SET time_zone = '+00:00';

CREATE TABLE endpoints (
    endpoint_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    endpoint_uri TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
    endpoint_hash CHAR(64) CHARACTER SET ascii
        GENERATED ALWAYS AS (SHA2(endpoint_uri, 256)) STORED,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (endpoint_id),
    UNIQUE KEY uq_endpoints_hash (endpoint_hash)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE links (
    link_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    endpoint_a_id BIGINT UNSIGNED NOT NULL,
    endpoint_b_id BIGINT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (link_id),
    UNIQUE KEY uq_links_ordered_pair (endpoint_a_id, endpoint_b_id),
    KEY ix_links_endpoint_b (endpoint_b_id),
    CONSTRAINT fk_links_endpoint_a
        FOREIGN KEY (endpoint_a_id) REFERENCES endpoints (endpoint_id),
    CONSTRAINT fk_links_endpoint_b
        FOREIGN KEY (endpoint_b_id) REFERENCES endpoints (endpoint_id),
    CONSTRAINT chk_links_distinct_endpoints
        CHECK (endpoint_a_id <> endpoint_b_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE encodings (
    encoding_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    encoding_name VARCHAR(100) NOT NULL,
    encoding_version VARCHAR(40) NOT NULL,
    description TEXT NOT NULL,
    definition JSON NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (encoding_id),
    UNIQUE KEY uq_encodings_name_version (encoding_name, encoding_version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE representations (
    representation_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    link_id BIGINT UNSIGNED NOT NULL,
    encoding_id BIGINT UNSIGNED NOT NULL,
    serialized_value MEDIUMTEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
    serialized_hash CHAR(64) CHARACTER SET ascii
        GENERATED ALWAYS AS (SHA2(serialized_value, 256)) STORED,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (representation_id),
    UNIQUE KEY uq_representations_link_encoding (link_id, encoding_id),
    UNIQUE KEY uq_representations_hash (serialized_hash),
    KEY ix_representations_encoding (encoding_id),
    CONSTRAINT fk_representations_link
        FOREIGN KEY (link_id) REFERENCES links (link_id),
    CONSTRAINT fk_representations_encoding
        FOREIGN KEY (encoding_id) REFERENCES encodings (encoding_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
