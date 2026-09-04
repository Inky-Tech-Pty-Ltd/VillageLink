# ADR-006: Use an HTTPS Village Link form with `!` as the candidate endpoint separator

**Status:** Proposed  
**Date:** 4 September 2026

## Context

ADR-001 establishes that a Village Link is a single self-contained identifier containing two endpoint URIs. A parser must be able to recover A and B without dereferencing a separate Village Link object.

ADR-005 establishes that A and B are URIs and that the reference publisher may mint conventional HTTPS endpoint identifiers using `gc` and `vc` naming conventions.

The remaining problem is serialization: given arbitrary valid endpoint URIs A and B, produce a single Village Link URI that:

1. identifies itself as a Village Link;
2. preserves the encoded order of A and B;
3. has an unambiguous A/B boundary;
4. permits exact round-trip recovery of A and B;
5. is a valid conventional URI;
6. does not require dereferencing in order to parse;
7. works predictably in conventional browsers; and
8. preserves useful human readability where practical.

An opaque Base64url encoding of each endpoint would make the boundary and round trip straightforward, for example:

```text
https://vl.village.link/<base64url(A)>/<base64url(B)>
```

but would turn recognisable material such as `gc.village.link`, `facebook.com` and `JoeRasmussen` into opaque text. Human readability is valuable enough that Base64url should be treated as a known fallback rather than the preferred representation unless a readable encoding proves impractical.

RFC URI syntax provides reserved characters for use as delimiters. Among the available candidates, `!` is visually distinctive and has relatively little competing structural meaning in an ordinary URI path.

## Proposed decision

Test the following Village Link serialization as the leading candidate:

```text
https://vl.village.link/<encoded-A>!<encoded-B>
```

`vl.village.link` is the Village Link marker for the reference implementation.

`!` is the candidate structural separator between endpoint A and endpoint B.

The encoded order is preserved. Therefore:

```text
VL(A,B)
```

and:

```text
VL(B,A)
```

may be different serializations even though the underlying same-entity assertion is semantically symmetric. By default, a Village Link-aware browser may use the serialized order for presentation, for example A in the left pane and B in the right pane. Applications MUST NOT infer greater semantic authority merely from that ordering.

A literal `!` belonging to A or B must not be confused with the structural separator and therefore must be escaped by the endpoint encoding.

The exact endpoint escaping algorithm is deliberately **not yet accepted**. It must be derived and tested against arbitrary valid endpoint URIs rather than selected by inspection.

## Acceptance tests

This ADR remains Proposed until the candidate syntax passes three classes of test.

### 1. URI conformance

The complete Village Link serialization must conform to the applicable conventional URI grammar.

### 2. Browser behaviour

Representative Village Links must be tested in conventional browsers and URI libraries to establish that significant information is not reinterpreted, normalised or destroyed unexpectedly.

A conventional browser should recognise the outer form as an HTTPS URI. A Village Link-aware browser should additionally recognise the marker and parse the two endpoints locally.

### 3. Village Link round trip

For a torture set of endpoint URIs, construction and parsing must satisfy:

```text
parse(make(A, B)) == (A, B)
```

The torture set should include endpoints containing or exercising at least:

- `/`;
- `?`;
- `#`;
- `%` and already percent-encoded material;
- literal `!`;
- Unicode / internationalised material;
- query parameters;
- fragments;
- non-HTTP URI schemes such as `urn:` and `mailto:`; and
- embedded or nested URI material.

Existing implementation tests produced by project contributors should be incorporated rather than replaced. Applicable standards-derived test cases should also be used where available.

## Consequences if accepted

The outer Village Link will use conventional HTTPS and DNS machinery rather than a new URI scheme such as `vl:`.

Conventional browsers will therefore have an ordinary HTTPS object to handle. The reference `vl.village.link` service may provide useful dereferencing behaviour, but dereferencing remains optional to the primitive: a Village Link-aware parser can recover A and B from the string itself.

The syntax will remain substantially human-readable rather than encoding both endpoints as opaque Base64 text.

## Alternatives considered

### New `vl:` URI scheme

Rejected as the current direction because it would require a new scheme and corresponding software adoption when conventional HTTPS syntax appears capable of carrying the primitive.

### Base64url endpoint encoding

Retained as a technically simple fallback because it provides a restricted alphabet and straightforward round-trip parsing. Not preferred because it destroys the human-readable parts of endpoint URIs.

### Other reserved-character separators

Characters including comma, semicolon, at-sign and others remain possible alternatives if `!` fails testing. `!` is the current leading candidate, not yet accepted architecture.

## Relationship to other ADRs

ADR-001 establishes the self-contained two-ended URI primitive.

ADR-005 establishes endpoint URI and naming conventions.

This ADR addresses only the serialization of those two endpoint URIs into one Village Link identifier.