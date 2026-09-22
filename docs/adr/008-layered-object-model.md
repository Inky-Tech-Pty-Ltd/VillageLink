# ADR-008: Separate relation, encoding, publication, and Star Credential layers

**Status:** Accepted  
**Date:** 22 September 2026

## Context

Village Link has used the words *Village Link* and *primitive* for several related but distinct things:

- an endpoint identifier such as A;
- the abstract same-entity relation A ↔ B;
- a self-contained URI encoding of A and B;
- the occurrence of that encoded link on a web resource W; and
- graph material later observed by a consuming application.

The ambiguity repeatedly encouraged a second mistake: treating the domain used inside an encoded Village Link as though it were W, the publisher, or an authority over the statement.

The SQL publication experiment in issue #42 made the distinction unavoidable. The project also needs the same clarity for Star Credentials, which are collections of Village Link relations but have their own abstract structure and serialization.

## Decision

The standard distinguishes the following layers.

### 1. Endpoint identifier

A and B are independently meaningful URI identifiers.

### 2. Same-entity relation

The abstract relation is:

```text
A ↔ B
```

It states that A and B refer to the same entity. The relation is symmetric.

### 3. Encoded Village Link

A **Village Link** is the self-contained URI encoding of one same-entity relation.

Conceptually:

```text
<domain>[A][B]
```

The current candidate HTTPS form is:

```text
https://wab.<domain>/<encoded-A>!<encoded-B>
```

The `<domain>` in this form is the **marker domain** used to make an ordinary URI. It is not W, is not necessarily the publisher, does not control either endpoint, and does not acquire truth or trust authority merely by appearing in the encoding.

`wab.village.link` is the project's reference marker implementation, not a required central authority.

### 4. Published Village Link statement

When an encoded Village Link is found on a web resource W:

```text
W states <domain>[A][B]
```

Semantically, W states the relation:

```text
W states A ↔ B
```

W belongs to the publication layer and is not encoded as a third endpoint in the Village Link.

The same encoded Village Link may occur on multiple web resources. Those are distinct publications even when the underlying relation and encoding are identical.

### 5. Abstract Star Credential

A **Star Credential** is:

```text
SC(A, S)
```

where A is one distinguished centre URI and S is a finite unordered set of URI identifiers:

```text
S = {B1, B2, ... Bn}
```

Its semantic content is the set of same-entity relations:

```text
{ A ↔ B | B is a member of S }
```

A Star Credential is domain-independent. It does not require a marker domain and does not require its members to be expanded into complete encoded Village Link URIs.

### 6. Encoded Star Credential

A Star Credential may be serialized in a machine-readable form that preserves:

- the distinguished centre A; and
- the unordered set S.

The standard does not yet adopt one wire serialization. JSON is the current reference candidate for Composer and prototype work, but JSON is an encoding of the Star Credential, not the Star Credential itself.

### 7. Published Star Credential statement

When a serialization of a Star Credential is found on W:

```text
W states SC(A, S)
```

The publication states the constituent A ↔ B relations as members of one credential.

Consumers may expand a Star Credential into its constituent relations for graph traversal, but SHOULD preserve the fact that the relations were published together as one Star Credential on one W.

### 8. Trust Engine observation

A Trust Engine or other consumer may observe published Village Links and published Star Credentials together with provenance, evidence, observation time, memory-system information and other application-specific context.

Those observations are application inputs. They are not additional fields of the encoded Village Link or the abstract Star Credential.

## Terminology rule

Current normative and explanatory documents SHOULD name the relevant layer explicitly rather than relying on the ambiguous phrase **the primitive**.

In particular:

- use **same-entity relation** for A ↔ B;
- use **Village Link** or **encoded Village Link** for the self-contained two-ended URI;
- use **published Village Link statement** for W stating a Village Link relation;
- use **Star Credential** for SC(A,S);
- use **Star Credential serialization** for a concrete JSON or other encoding; and
- use **published Star Credential statement** for W stating a Star Credential.

The word *primitive* may still be used informally when the intended layer is clear, but it must not erase these distinctions.

## Consequences

The marker domain and W can no longer be confused without crossing an explicit layer boundary.

A Village Link needs a marker domain because the project currently uses ordinary HTTPS/DNS machinery for the encoded two-ended URI. A Star Credential does not inherit that requirement.

The SQL experiment in issue #42 may compare candidate Village Link encodings without modelling W. A separate publisher or publication table may later record where encoded links or serialized Star Credentials are found.

Trust Engine work may operate over both individual published Village Links and published collections while preserving their publication provenance and collection boundaries.

Existing documents that use *Village Link*, *primitive*, *assertion* or *publisher* ambiguously should be read in light of this ADR and repaired as they are maintained.

## Relationship to other ADRs

ADR-001 establishes the self-contained two-ended URI architecture.

ADR-004 defines the centred unordered-set data model for Star Credentials.

ADR-005 defines endpoint URI and naming conventions.

ADR-006 defines the `wab` marker and candidate Village Link serialization.

ADR-007 separates stateless composition from persistent credential custody.

This ADR clarifies how those objects and decisions fit into one layered model.
