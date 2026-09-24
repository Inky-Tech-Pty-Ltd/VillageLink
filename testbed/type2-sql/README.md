# Type 2 SQL publisher

This is the deliberately small SQL-backed Village Link publisher for Issue #42. It is unlike Anna/MediaWiki: four relational tables are the backing store, and a minimal PHP application publishes web resources from them.

The database is not W. Each successful HTTP resource emitted by the PHP application is a W.

## Files

- `schema.sql` creates `endpoints`, `links`, `encodings`, and `representations`.
- `seed.sql` loads one Asha Bhosle test link and its `percent-unreserved` representation.
- `public/` is the document-root application.
- `config.example.php` documents the private database configuration shape.

The schema is tested against MariaDB 10.5 and uses `utf8mb4_unicode_ci` for MySQL/MariaDB portability.

## Deployment shape

The `wab.inky.tech` document root contains only the files in `public/`. The real configuration is stored outside the web root as:

```
/home12/inkytech/vl2-config.php
```

Copy `config.example.php` there and supply the database-user password. Do not commit the real configuration.

## Test corpus

The exact seeded representation is:

```
https://wab.inky.tech/https%3A%2F%2Fvillage.link%2Fwiki%2Findex.php%2FAsha_Bhosle!https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAsha_Bhosle
```

The application supports `GET` and `HEAD`. The exact encoded URI is intentionally important: the current codec percent-encodes slashes, while Apache may reject `%2F` before the rewrite reaches PHP. Reproducing that response is part of the Issue #42 / Issue #41 interoperability experiment, not a database failure.
