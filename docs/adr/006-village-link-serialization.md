# ADR-006: Use an HTTPS Village Link form with `wab` marker and `!` as the candidate endpoint separator

**Status:** Proposed  
**Date:** 4 September 2026  
**Marker decision adopted:** 6 September 2026  
**Candidate endpoint encoding added:** 8 September 2026

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

The project adopts `wab` as the HTTPS marker prefix for the two-ended primitive. The prefix is deliberately not derived from the Village Link project name: a neutral marker reduces unnecessary project branding in a convention intended for broad adoption by independent or competing parties. The letters also provide a compact visual mnemonic for the primitive: W between endpoints A and B, corresponding to **A ← W → B**.

An opaque Base64url encoding of each endpoint would make the boundary and round trip straightforward, for example:

```text
https://wab.village.link/<base64url(A)>/<base64url(B)>
```

but would turn recognisable material such as `gc.village.link`, `facebook.com` and `JoeRasmussen` into opaque text. Human readability is valuable enough that Base64url should be treated as a known fallback rather than the preferred representation unless a readable encoding proves impractical.

RFC URI syntax provides reserved characters for use as delimiters. Among the available candidates, `!` is visually distinctive and has relatively little competing structural meaning in an ordinary URI path.

## Adopted marker and proposed separator

The marker prefix is **adopted** as `wab`. Test the following serialization, with `!` as the leading candidate endpoint separator:

```text
https://wab.village.link/<encoded-A>!<encoded-B>
```

`wab.village.link` is the reference marker implementation. It is not a central registry, resolver or privileged authority.

The first DNS label `wab` is the marker convention. A domain owner may operate the same serialization beneath an HTTPS authority it controls. For example, each of the following is an eligible marker:

```text
https://wab.village.link/
https://wab.github.com/
https://wab.example.org/
```

A complete serialization beneath another domain owner's marker may therefore take the form:

```text
https://wab.github.com/<encoded-A>!<encoded-B>
```

No registration with or permission from `village.link` is required. The marker identifies the two-ended form; it does not establish that the statement is true, trusted or authorised by either endpoint system.

`!` is the candidate structural separator between endpoint A and endpoint B.

The encoded order is preserved. Therefore `VL(A,B)` and `VL(B,A)` may be different serializations even though the underlying same-entity statement is semantically symmetric. By default, a Village Link-aware browser may use the serialized order for presentation, for example A in the left pane and B in the right pane. Applications MUST NOT infer greater semantic authority merely from that ordering.

## Candidate endpoint encoding

For Draft 0.1 testing, treat each endpoint URI as an opaque Unicode string and encode it as UTF-8 bytes using percent-encoding.

Leave literal:

```text
A-Z a-z 0-9 - . _ ~ : /
```

All other bytes are percent-encoded using two hexadecimal digits.

The addition of literal `:` and `/` is deliberate. Earlier testing used the more conservative rule of leaving only the RFC 3986 unreserved character set literal. That encoding passed round-trip torture testing, but a real Apache deployment at `wab.inky.tech` returned 404 for the percent-encoded representation containing `%2F`, despite PHP successfully locating the published Village Link and attempting to return 200.

A more readable candidate that leaves `:` and `/` literal was therefore tested.

The candidate construction algorithm is:

```text
make(A, B) =
    "https://wab.village.link/"
    + encode(A)
    + "!"
    + encode(B)
```

Parsing removes the recognised marker prefix, requires exactly one literal `!` in the payload, splits at that character, and percent-decodes each side exactly once as UTF-8.

Characters with outer-URI or Village Link grammar significance remain encoded. In particular, literal endpoint `!`, `%`, `?`, `#`, spaces, Unicode bytes and other reserved material are percent-encoded as required by the codec.

Existing percent signs in an endpoint URI are therefore still encoded. For example an endpoint substring `%20` is embedded as `%2520`; a single parse operation restores the original literal `%20`. This preserves the endpoint string rather than normalising it.

A literal endpoint `!` is encoded as `%21`, so the structural separator is the only literal `!` in a valid payload produced by `make`.

For example:

```text
A = https://village.link/wiki/index.php/Asha_Bhosle
B = https://en.wikipedia.org/wiki/Asha_Bhosle
```

produces:

```text
https://wab.village.link/https://village.link/wiki/index.php/Asha_Bhosle!https://en.wikipedia.org/wiki/Asha_Bhosle
```

The implementation criterion remains:

```text
parse(make(A, B)) == (A, B)
```

This encoding remains a **candidate**, not accepted final wire syntax.

Testing to date includes:

- the existing URI torture suite;
- a 10,000-case deterministic generated round-trip run;
- Apache/PHP GET and HEAD testing at `wab.inky.tech`;
- nginx GET and HEAD testing;
- Village Link browser parsing and resource-probe behaviour.

The earlier conservative percent-unreserved form and Base64url remain useful comparison controls. Base64url is technically straightforward and transport-safe, but substantially reduces human readability.

## Acceptance tests for the remaining serialization

The `wab` marker decision is adopted. This ADR remains Proposed because the separator and endpoint-escaping syntax still require three classes of test.

### 1. URI conformance

The complete Village Link serialization must conform to the applicable conventional URI grammar.

### 2. Browser behaviour

Representative Village Links must be tested in conventional browsers and URI libraries to establish that significant information is not reinterpreted, normalised or destroyed unexpectedly.

A conventional browser should recognise the outer form as an HTTPS URI. A Village Link-aware browser should recognise an HTTPS URI whose first DNS label is `wab` and first attempt to interpret it locally as a Village Link, before ordinary web dereferencing. Successful parsing must not depend on the marker host being dereferenceable. If local Village Link parsing fails, the browser should fall back to ordinary HTTPS handling.

Marker recognition establishes only that the URI may use Village Link syntax. It does not establish truth, authority or trust.

### 3. Village Link round trip

For a torture set of endpoint URIs, construction and parsing must satisfy:

```text
parse(make(A, B)) == (A, B)
```

The torture set should include endpoints containing or exercising at least `/`, `?`, `#`, `%`, already percent-encoded material, literal `!`, Unicode/internationalised material, query parameters, fragments, non-HTTP URI schemes and embedded or nested URI material.

A prototype codec and executable torture tests are maintained in `prototype/villagelink/codec.py` and `prototype/tests/test_codec.py`.

Existing implementation tests produced by project contributors should be incorporated rather than replaced. Applicable standards-derived test cases should also be used where available.

## Consequences if the remaining syntax is accepted

The outer Village Link will use conventional HTTPS and DNS machinery rather than a new URI scheme such as `wab:`.

Conventional browsers will therefore have an ordinary HTTPS object to handle. Any marker operator may provide useful dereferencing behaviour, including the reference `wab.village.link` service, but dereferencing remains optional to the primitive: a Village Link-aware parser can recover A and B from the string itself.

The candidate syntax remains substantially human-readable: ordinary URI structure, including scheme separators and path slashes, remains visible, while characters significant to the outer URI or Village Link grammar are percent-encoded.

## Alternatives considered

### `vl` marker prefix

Superseded. Although compact, `vl` is an abbreviation of Village Link and therefore carries project branding into a convention intended to be usable by independent or competing adopters. `wab` is preferred because it is project-neutral and provides a mnemonic for the A–W–B structure.

### New `vl:` or `wab:` URI scheme

Rejected as the current direction because a new scheme would require corresponding software adoption when conventional HTTPS syntax appears capable of carrying the primitive.

### Base64url endpoint encoding

Retained as a technically simple fallback because it provides a restricted alphabet and straightforward round-trip parsing. Not preferred because it destroys the human-readable parts of endpoint URIs.

### Other reserved-character separators

Characters including comma, semicolon, at-sign and others remain possible alternatives if `!` fails testing. `!` is the current leading candidate, not yet accepted architecture.

## Relationship to other ADRs

ADR-001 establishes the self-contained two-ended URI primitive.

ADR-005 establishes endpoint URI and naming conventions.

This ADR adopts the `wab` marker prefix and specifies a readable-path candidate encoding for testing the serialization of the two endpoint URIs into one Village Link identifier.
