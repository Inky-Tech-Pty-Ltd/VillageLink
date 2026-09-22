# ADR-004: Define a Star Credential as a centred unordered set

**Status:** Accepted  
**Date:** 5 September 2026  
**Layering clarified:** 22 September 2026

## Context

ADR-001 defines a Village Link as a self-contained two-ended URI connecting two endpoint identifiers. ADR-008 later separates the relation, encoding and publication layers.

At the relation layer:

**A ↔ B.**

When an encoded Village Link is found on W:

**W states A ↔ B.**

Publishers and applications also need to group Village Links that connect one noun to representations of that noun in multiple contexts. The project calls this larger object a **Star Credential**.

Without a separate data model, a Star Credential might be treated as an ordered list of complete Village Links, a table, or the editable contents of a wiki page. Those alternatives confuse the credential itself with a serialization or presentation, leave the significance of ordering unclear, and repeat the common endpoint in every Village Link.

The Star Credential therefore requires a definition as precise as the Village Link primitive while remaining independent of any particular wire format or user interface.

## Decision

A Star Credential consists of:

1. one distinguished centre noun, designated **A**; and
2. a finite unordered set of nouns, designated **B**.

Each noun is represented by a URI endpoint identifier conforming to the Village Link endpoint requirements.

If:

```text
S = {B1, B2, ... Bn}
```

then the Star Credential is:

```text
SC(A, S)
```

and states the set of Village Links:

```text
{ A ↔ B | B is a member of S }
```

Its compact abstract structure is:

```text
[A]{[B1], [B2], ... [Bn]}
```

A is recorded once as the centre. Each B is recorded as a member of the associated set.

The B set is **unordered**. The order in which its members happen to be serialized, stored or presented has no semantic significance.

A B noun cannot occur more than once in the set. Repetition does not create an additional statement or add weight to an statement.

The distinguished role of A is structural: A is the centre of this Star Credential. It does not make the underlying Village Links directional and does not confer greater truth, authority or importance on A. Each individual statement remains the symmetric equivalence statement A ↔ B defined by the Village Link specification.

Two Star Credentials with the same A and the same set of Bs have the same credential content regardless of the order in which the Bs are represented. Separate publications of that content may nevertheless remain distinct publisher-attributed acts.

This ADR does not select a concrete serialization such as JSON, XML or CSV.

A Star Credential is domain-independent. It does not require the marker domain used by an encoded Village Link and does not require each member relation to be expanded into a complete Village Link URI.

## Rationale

The centred-set model captures the defining topology of the object without importing presentation or storage choices into its meaning.

Recording A once avoids unnecessary repetition. Treating the Bs as a set reflects the fact that the credential makes independent A ↔ B statements and makes no statement about an ordering among the Bs.

The model also supports subset operations naturally. An audience-specific Star Credential can be formed by retaining A and selecting an appropriate subset of the available Bs without changing the Village Link primitive.

Separating the abstract object from its serialization allows the same credential to be represented as machine-readable data, rendered as a table, or presented through another interface without changing its semantics.

JSON is a natural candidate serialization for the reference Composer, but JSON would be one encoding of `SC(A,S)`, not the credential itself.

## Consequences

The normative definition belongs in [specification.md](../../specification.md). This ADR records the decision and its rationale.

A concrete serialization must preserve the distinction between A and the B set and must not assign meaning to the serialized order of the Bs. It need not contain a Village Link marker domain.

A renderer may choose an order for human use, such as alphabetical, chronological or relevance order. That choice is presentation only.

The reference publisher's Entity page described in ADR-003 may present a Star Credential assembled from published Link statements. Whether the publisher stores the credential directly or generates it as a projection of those statements is a publisher-layer implementation decision and does not alter this data model.

When a serialization of a Star Credential is found on W, the publication can be expressed as **W states SC(A,S)**. Consumers may expand the credential into its constituent A ↔ B relations for graph traversal while preserving the fact that those relations were published together as one credential on one W.

The following questions remain open:

- the minimum number of Bs required for a publishable Star Credential;
- the concrete wire serialization;
- canonical byte representation for hashing or signatures;
- the treatment of metadata, evidence and provenance;
- how a MediaWiki stores, validates and edits the structured object; and
- how the human-facing Entity page presents the credential and surrounding material.

## Alternatives considered

### Ordered list of Bs

Rejected. Applications may order Bs for presentation, but no general ordering belongs to the meaning of the credential.

### List of complete Village Links

A list of complete Village Links can express the same statements, but it repeats A for every member and does not by itself identify which endpoint is the centre. It may be useful as an export or expanded representation, but it is not the abstract Star Credential model.

### Table or wiki page as the credential

Rejected as the definition. A table or wiki page may present and govern a Star Credential, but presentation markup is not the machine-readable object itself.

## Relationship to other ADRs

ADR-001 establishes the self-contained two-ended Village Link primitive.

ADR-002 restricts each Village Link to equivalence.

ADR-003 establishes the MediaWiki reference publisher and its Entity-page and Link-page views.

ADR-005 establishes that endpoint identifiers are URIs and records naming conventions.

ADR-006 addresses serialization of an individual Village Link. Serialization of a Star Credential remains a separate decision.

ADR-008 separates the relation, Village Link encoding, publication and Star Credential layers and records that the abstract Star Credential is domain-independent.
