# ADR-008: Link traces by a shared referent with a publisher-independent URI

**Status:** Proposed  
**Date:** 28 September 2026

## Context

The first Village Link model described a publisher's web resource W stating that two endpoint identifiers represented the same entity: **W states A ↔ B**. Its candidate serialization placed the assertion beneath a publisher-controlled HTTPS `wab.` host. This helped establish the two-ended, self-contained link, but bundled the link's identity with one location of publication and described its ends primarily as representations of an entity.

The project now needs to distinguish three things: a trace in a memory system, the relation asserted between two traces, and the act of publishing that assertion. The same relation can be published by different parties, and a publisher can make several statements about it. A memory system need not be a website, although software needs URI identifiers for the traces it addresses.

The prototype codec, Composer, browser and two test publishers have been adapted to a publisher-independent `vl:` link. This ADR records the architectural decision those implementations are testing. The README's compact notation is an explanation of the idea, not a byte-for-byte serialization rule.

## Decision

A Village Link relates **two URI-identified traces in memory systems** and asserts that they have the **same referent**, M. Conceptually:

```text
vl:[A in X]=[B in Y]
```

A is a trace in memory system X; B is a trace in memory system Y. The equality sign asserts sameness of referent, not textual equality of A and B, equivalence of X and Y, or agreement between everything those systems say. M is not a required third endpoint or a privileged canonical identifier.

The relation is symmetric in meaning. An implementation preserves the order of A and B in the encoded link for presentation and exact round trips; that order gives neither endpoint greater authority.

Let P be the URI identifier for [A in X], and Q the URI identifier for [B in Y]. The Village Link identifier is **independent of its publisher**. In the current draft codec it is a self-contained URI:

```text
vl:<percent-encoded-P>!<percent-encoded-Q>
```

The codec percent-encodes each URI as UTF-8, leaving only RFC 3986 unreserved characters literal, and uses one literal `!` as the separator. Parsing recovers P and Q without dereferencing a publisher or a separate assertion object. This records the tested draft format; the specification remains the place for detailed conformance rules and any future revision of wire syntax.

A publisher may place the same Village Link in a wiki page, a database-backed publication, or another medium. The publication supplies provenance, context and an opportunity for governance. Neither the publisher's domain nor the publication location is part of the link's two-ended URI. Repetition of one link by several publishers produces distinct publication acts, not distinct endpoint relations merely because the hosts differ.

The link expresses an assertion. Its syntax alone does not establish truth, consent, authority, trust or permanence. A trace or its memory system may change, disappear, contradict another trace, or have no directly dereferenceable web page.

## Rationale

Separating the relation from publication lets independent publishers quote, challenge and contextualise the same link without minting different link identifiers for the same encoded endpoint pair. It also lets the browser recognise a Village Link before attempting ordinary navigation, while the publishers retain their own governance and reputations.

The shared-referent statement stays deliberately narrow. Applications can infer richer meanings from traces and memory systems; the primitive does not need a general predicate grammar to encode them.

## Consequences

- The codec and browser recognise `vl:` directly. A conventional browser need not render that scheme without additional handling; publisher pages can still expose ordinary HTTPS pages and links.
- Publishers store or display the link along with their own publication record. The URI by itself does not identify who made or endorsed a particular publication.
- Endpoint URIs are handles for traces. The mechanism by which a non-web trace gets such a handle, and the reliability of that handle over time, remain questions for memory systems and publishers.
- A Star Credential can continue to distinguish one centre A and an unordered set of Bs. This ADR does not revise its data model. ADR-007 keeps Composer stateless and removes a persistent Star Credential Manager from the current architecture and roadmap; this decision does not reopen that question.
- The specification, glossary, examples and older ADR cross-references should be reconciled with this decision in a separate documentation pass. Until then, they contain historical wording and candidate syntax that conflict with the current implementation.

## Relationship to earlier decisions

- **ADR-001:** Retains the self-contained, two-ended link and the separation between the assertion and its publication. Supersedes the framing of W as necessarily the web resource in which the link is found and clarifies that W is not encoded in the link.
- **ADR-002:** Retains one narrow relation. Refines “equivalence of entity representations” to an assertion that two traces have the same referent; it does not introduce arbitrary predicates or explicit non-equivalence.
- **ADR-005:** Retains URI endpoints. The `gc.` and `vc.` naming examples are possible endpoint conventions, not required trace types or privileged authorities.
- **ADR-006:** Supersedes the adopted `wab.` HTTPS marker and its publisher-domain form as the Village Link identifier. The current draft uses the `vl:` scheme and an encoded `!`-separated pair. A `wab.` host may still be an ordinary publisher address.
- **ADR-004:** Retains the centred, unordered Star Credential model.
- **ADR-007:** Retains stateless composition and the decision not to build a persistent Star Credential Manager as part of the current architecture.

The earlier ADRs remain in the repository as the record of how the architecture developed. This ADR states which decisions now govern the primitive; detailed specification updates should follow rather than silently rewriting those historical records.
