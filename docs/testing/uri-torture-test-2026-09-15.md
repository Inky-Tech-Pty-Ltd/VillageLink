# Village Link URI torture test — 15 September 2026

## Purpose

Test the Draft 0.1 candidate serialization from ADR-006 against adversarial endpoint material and record the result before wider browser interoperability testing.

Baseline tested: `main` at `04a3386978f0524909dc017562e915baeef87af1`.

Central acceptance criterion:

```text
parse(make(A, B)) == (A, B)
```

## Result

**PASS for codec round-trip behaviour.**

The candidate form remains:

```text
https://wab.<domain>/<encoded-A>!<encoded-B>
```

No tested endpoint material produced an A/B boundary collision. Percent-encoding all endpoint bytes except RFC 3986 unreserved characters leaves the structural `!` as the only literal separator produced by `make()`.

The torture set exercised reserved characters, literal `!`, `%`, already percent-encoded material, query strings, fragments, Unicode and internationalised material, non-HTTP schemes, nested URI material, nested Village Links, asymmetric endpoint hierarchies, long inputs, and deterministic generated strings. A 10,000-case generated round-trip run was also performed during the review; the committed regression suite retains 1,000 deterministic generated cases for routine execution.

## Hardening found during testing

The original parser was intentionally small and accepted several non-canonical outer forms that `make()` would not produce. The accompanying codec change tightens these boundaries without changing the candidate wire syntax produced by `make()`:

- reject userinfo in the marker authority;
- reject explicit ports in the marker authority;
- reject extra leading payload slashes rather than normalising them;
- reject malformed percent escapes and expose invalid UTF-8 percent encoding as `ValueError`; and
- validate the publishing domain as DNS-label syntax, including IDNA-aware label length checks.

These are parser/composer hardening changes, not evidence against the `!` separator or endpoint percent-encoding design.

## Scope distinction

The codec treats A and B as opaque Unicode strings for serialization. The Village Link specification separately requires conforming endpoints to be URIs. This test establishes serialization round-trip behaviour; it does not make the codec a general URI-validity checker.

## Still outstanding

ADR-006 also calls for conventional-browser behaviour testing. That remains a separate acceptance class. Representative links should be exercised in current conventional browsers to detect unexpected URI reinterpretation or normalisation, and the Village Link prototype should receive a human regression pass against the exact published `main` build.

## Executable record

Routine adversarial regression cases are in:

```text
prototype/tests/test_uri_torture.py
```

Existing contributor tests in `prototype/tests/test_codec.py` are retained unchanged.
