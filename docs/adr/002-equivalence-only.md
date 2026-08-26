# ADR-002: Restrict the Village Link primitive to equivalence

**Status:** Accepted  
**Date:** 27 August 2026

## Context

The Village Link primitive connects two representations of an entity in different contexts:

`(A in X) = (B in Y)`

where `A in X` and `B in Y` identify representations within existing memory systems.

Once this form is admitted, an obvious generalisation presents itself.

First, Village Link might support explicit non-equivalence:

`(A in X) ≠ (B in Y)`

More generally, the fixed equivalence relation could be replaced by an arbitrary operator:

`(A in X) OPERATOR (B in Y)`

This would permit assertions such as:

- A is not B
- A owns B
- A employs B
- A trusts B
- A is a member of B
- A is a parent of B

Such a design would turn Village Link into a general mechanism for expressing relationships between entities. It would begin to resemble a subject–predicate–object system or general-purpose semantic graph.

That is a coherent architecture, but it is not the architecture Village Link intends to provide.

## Decision

Village Link will define **one relation only: equivalence of entity representations across contexts**.

The primitive remains:

`(A in X) = (B in Y)`

The protocol will not generalise this relation to an arbitrary operator.

Explicit non-equivalence (`≠`) is also excluded from the primitive at this stage. The usefulness of non-equivalence assertions is recognised, particularly where identities are ambiguous, but their inclusion would require a separate architectural decision.

This restriction is deliberate.

## Rationale

Village Link is intended to perform a very small operation: to stitch together representations that already exist in independent memory systems.

It does not attempt to describe the full set of relationships among entities in those systems or in the world.

The expressive poverty of the primitive is therefore a design property.

A conventional hyperlink similarly provides a deliberately narrow relation:

`P → A`

It does not attempt to encode the semantic relationship between the source and destination.

Village Link introduces a different narrow relation:

`A ↔ B`

with the specific meaning that the two endpoints represent the same entity in different contexts.

Restricting the primitive in this way keeps the protocol small while allowing richer structures, evidence, disagreement, governance and consequences to emerge around published links.

## Consequences

Village Link cannot directly express arbitrary relationships between entities.

Applications requiring those relationships must represent them elsewhere or build additional structures above the Village Link primitive.

Publishers may disagree about whether two representations are equivalent. Such disagreement does not require additional operators in the primitive: competing assertions, evidence and the systems consuming them can handle questions of truth, confidence and governance.

If a future use case demonstrates that explicit non-equivalence or other operators are necessary, that capability should be considered through a new architectural decision rather than treated as an implicit extension of this one.

## Alternatives considered

### Equivalence and non-equivalence

Support both:

`A = B`

and:

`A ≠ B`

This provides additional expressive power but begins to change Village Link from a linking primitive into an assertion language.

**Rejected for the initial architecture.**

### Arbitrary operators

Define the general form:

`A OPERATOR B`

This would provide a highly expressive graph model capable of representing many kinds of relationships.

**Rejected.** This is a substantially larger problem domain and duplicates capabilities available in existing semantic and graph technologies.

### Equivalence only

Define one deliberately constrained operation:

`A = B`

**Accepted.**

Village Link is not intended to say everything that can be said about two entities.

It is intended to say one thing extremely simply:

**these two representations are of the same thing.**
