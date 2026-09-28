# ADR-008: A village link asserts equality between two expressions of a meme

**Status:** Proposed  
**Date:** 28 September 2026

## Context

A Village Link began with a compact idea:

```text
W states A ↔ B
```

That formulation contained two ideas that were useful, but became entangled.

First, there is the **assertion itself**: two traces in two memory systems are expressions of the same thing.

Second, there is the **publication of that assertion**: somebody, somewhere, says so.

Early candidate serializations placed the link beneath a publisher-controlled HTTPS domain. That made the publisher's location appear to be part of the identity of the link. In effect, the project had allowed **W**, the publication, and **<domain>**, a component of the serialization, to collapse into one another.

They are not the same thing.

A Village Link must be able to exist independently of any one place in which it is published. The same link may be published by many parties, in many systems, each acquiring its own provenance, context and reputation.

At the same time, the project has sharpened what the two ends of the link are. They are not merely "representations of an entity". They are **traces in memory systems**. The thing that is equal is not the traces themselves, nor the systems that contain them, but the idea to which both traces refer.

We call that idea a **meme**.

## Decision

A Village Link asserts equality between two expressions of a meme.

Conceptually:

```text
vl:[A in X]=[B in Y]
```

A is a trace in memory system X.  
B is a trace in memory system Y.

Both have the same referent, M:

```text
M = [A in X]
M = [B in Y]
```

Therefore:

```text
[A in X] = [B in Y]
```

The equality is **referential equality**.

It does not assert that:

- A and B are textually identical;
- X and Y are equivalent memory systems;
- X and Y agree about everything they record;
- either trace is complete, authoritative or true;
- M has a privileged canonical identifier.

It asserts one thing only: **these two traces are expressions of the same meme**.

## The primitive and its publication are separate

The Village Link itself is the relation between the two trace identifiers.

Its publication is a separate act.

If W publishes a Village Link, then W is evidence about **who published the assertion, where, when, and under what governance**. W is not part of the primitive merely because it published it.

This distinction resolves the earlier confusion between:

```text
W states A ↔ B
```

and serializations of the form:

```text
https://<domain>/...
```

In the earlier model, `<domain>` appeared inside the serialized identifier of the link. Because W was also imagined as the web resource that published the assertion, the identity of the link became entangled with the place of publication.

ADR-008 separates them.

The same Village Link may be published at W1, W2 and W3. Those are three publication acts of one relation, not three different relations.

A publisher domain may still identify an ordinary web resource. It simply does not define the identity of the Village Link.

## Serialization

Let:

```text
P = URI identifying [A in X]
Q = URI identifying [B in Y]
```

The current draft serialization is:

```text
vl:<percent-encoded-P>!<percent-encoded-Q>
```

The `vl:` URI is self-contained and publisher-independent.

The codec percent-encodes P and Q as UTF-8, leaving RFC 3986 unreserved characters literal, and separates the two encoded operands with one literal `!`.

Parsing the URI recovers P and Q. It does not require dereferencing a publisher, resolving a `wab.` host, or retrieving a separate assertion object.

The README notation:

```text
vl:[A in X]=[B in Y]
```

describes the meaning of the primitive.

The codec notation:

```text
vl:<percent-encoded-P>!<percent-encoded-Q>
```

describes its current machine serialization.

The two should not be confused.

## Symmetry

The asserted relation is symmetric in meaning.

If:

```text
[A in X] = [B in Y]
```

then neither endpoint is semantically primary.

An implementation may preserve the encoded order of P and Q for presentation and exact round trips. That ordering does not confer greater authority on either endpoint.

## Publication, provenance and governance

A publisher may publish a Village Link in a wiki, a database-backed service, a plain web page, a signed record, or another medium entirely.

That publication can contribute:

- provenance;
- context;
- authorship;
- timing;
- reputation;
- challenge or endorsement;
- consequences within a memory system.

These properties belong to the publication environment, not to the minimal equality relation itself.

The primitive therefore remains small enough to be repeated across systems while publishers remain free to accumulate their own governance and reputation.

## What the primitive does not claim

A Village Link is an assertion, not a proof.

Its syntax does not establish truth, consent, authority, trust or permanence.

A trace may change or disappear. A memory system may be unreliable. Different publishers may publish contradictory links. A meme may have many traces, and those traces may reveal different aspects of it.

Those are not failures of the primitive. They are the conditions under which reputation and governance become meaningful.

## Consequences

- Village Links are identified independently of their publishers.
- The same Village Link can be published repeatedly without being reminted for each publisher.
- Publishers can acquire reputation for the assertions they choose to publish.
- The browser and codec can recognise and parse a Village Link without first navigating to a publisher-controlled host.
- URI endpoints remain handles for traces in memory systems, including systems that are not themselves websites.
- The primitive remains deliberately narrow: equality of referent only.
- Richer meaning is left to applications, memory systems, publication context and the graph that emerges from many assertions.
- A Star Credential remains a composition of Village Links around one centre; this ADR does not alter the Star Credential data model.
- ADR-007 remains intact: composition is stateless, and the project does not require a persistent Star Credential Manager.

## Relationship to earlier decisions

- **ADR-001:** Retains the two-ended primitive and the distinction between an assertion and its publication. Refines the role of W: W is a publication of the assertion, not a component required to identify the assertion.
- **ADR-002:** Retains one narrow relation. Equality is now stated more precisely as equality of referent between two traces.
- **ADR-004:** Retains the centred Star Credential model.
- **ADR-005:** Retains URI identifiers for endpoints. They identify traces; naming conventions such as `gc.` and `vc.` are not privileged trace types.
- **ADR-006:** Supersedes the `wab.` publisher-domain serialization as the identity of a Village Link. A `wab.` host may remain a publisher, but its domain is not part of the primitive.
- **ADR-007:** Retains stateless composition and the decision not to build a persistent Star Credential Manager.

Earlier ADRs remain as the architectural history of the project.

ADR-008 records the point at which the primitive becomes fully separable from its publication:

```text
vl:[A in X]=[B in Y]
```

Two traces.  
Two memory systems.  
One meme.
