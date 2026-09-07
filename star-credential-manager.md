# Star Credential Manager

## Status

**Superseded by [ADR-007](docs/adr/007-stateless-composer.md), 7 September 2026.**

This file is retained as a historical concept document because it records the line of thought that led to an important architectural reversal.

The project originally grouped two functions under the working name **Star Credential Manager**:

1. constructing village links and star credentials from supplied identifiers; and
2. persistently managing a person's or other entity's cross-context identity relationships and deciding which subsets to present to different audiences.

Further analysis showed that these functions have radically different trust and security characteristics.

The first has become **Composer**, a small stateless reference tool described in [composer.md](composer.md).

The second is **not part of the current Village Link architecture**. A persistent store of private cross-context equivalence relationships could reveal exactly the connections that users depend upon keeping separate. Any future proposal to build such a system requires a fresh architectural and security decision rather than continuation of this concept.

The reasoning and decision are recorded in ADR-007.

---

## Historical concept

The original concept asked:

> **Given all the contexts in which a noun has left traces, which of those traces should be presented to this audience?**

It observed that truth and appropriate disclosure are different questions and considered an **outer-boundary star credential** from which public, professional, family, financial-services, dating or transaction-specific subsets might be selected.

That exploration produced two useful conclusions which remain valid:

- audience management should not enlarge the Village Link primitive; and
- existing authentication, authorisation, access-control, private-group, encrypted-messaging and selective-disclosure systems already provide extensive machinery for controlling audiences.

The subsequent decision goes further: Village Link presently has no demonstrated need to become the custodian of the complete private identity graph from which such audience-specific subsets might be selected.

The project's current four areas are therefore:

1. **Standard** — define;
2. **Publisher** — publish;
3. **Browser + Trust Engine** — interpret; and
4. **Composer** — compose.

In shorthand:

> **Define → Publish → Interpret → Compose**

For the current architecture, see [DOCUMENTATION.md](DOCUMENTATION.md), [composer.md](composer.md) and [ADR-007](docs/adr/007-stateless-composer.md).
