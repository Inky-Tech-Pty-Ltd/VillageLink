# ADR-005: Use conventional URIs and decentralised naming for endpoint identifiers

**Status:** Accepted  
**Date:** 4 September 2026

## Context

The Village Link primitive is:

**P asserts A ↔ B.**

A and B need independently meaningful identifiers. Existing online memory systems often already provide suitable URIs, but Village Link must also be able to refer to nouns in memory systems that do not already have an online namespace: for example, a person as remembered at `Family Christmas`, or a person visible in a particular collection of security-camera records.

Earlier design work proposed two useful naming conventions:

- `gc` — a **global-context** identifier, intended to identify a noun without restriction to a particular memory-system context; and
- `vc` — a **village-context** identifier, intended to identify a noun within a contextual namespace.

A possible implementation could introduce new URI schemes such as `gc:` or `vc:`. Doing so would require software to understand new schemes and would enlarge the standard unnecessarily. Conventional HTTPS and DNS already provide globally usable, decentralised namespaces.

There is also no reason for Village Link to define a closed ontology of context types. Contexts and memory systems are themselves nouns: they may have reputations, may be the centres of star credentials, and may themselves occur within broader contexts. Context structure is therefore naturally recursive.

## Decision

Village Link endpoint identifiers are **URIs**.

The Village Link standard does not introduce a new `gc:` or `vc:` URI scheme. Where the Village Link reference publisher mints endpoint identifiers, it will use conventional HTTPS and DNS syntax.

The project adopts `gc` and `vc` as **naming conventions**, not privileged endpoint types in the core primitive.

Examples minted by the reference publisher may include:

```text
https://gc.village.link/JoeRasmussen
https://vc.village.link/FamilyChristmas/JoeRasmussen
https://vc.village.link/FamilyChristmas/2025/JoeRasmussen
```

The intended meanings are:

- `gc` identifies a noun without restriction to a particular memory-system context. It does not certify that the identifier is true, authoritative, legally privileged or uniquely canonical.
- `vc` provides a contextual namespace in which path structure may express context, subcontext and noun relationships.

The path hierarchy may be recursive. A memory system or context may itself be identified as a noun and may participate in Village Links like any other noun.

The core standard does **not** assign universal semantics to individual path segments. A namespace may use a human-readable hierarchy such as:

```text
FamilyChristmas/2025/JoeRasmussen
```

while another publisher may use opaque identifiers or a different structure.

Other domain owners may adopt the `gc` and `vc` conventions independently, for example:

```text
https://gc.example.org/Alice
https://vc.example.org/SomeContext/Alice
```

They may also invent different naming conventions. Village Link does not require permission from, registration with, or dereferencing through `village.link` for an endpoint URI to participate in the graph.

## Consequences

The core remains small:

```text
P asserts A ↔ B
A and B are URIs.
```

Existing URIs may be used directly. Village Link naming conventions are available when a suitable endpoint URI does not already exist.

The reference publisher can provide human-facing assistance around naming, including redirects, disambiguation, context hierarchies and friendly labels, without making those facilities requirements of the primitive.

Because `gc` is a naming convention rather than an authority claim, multiple publishers may mint competing global-context identifiers for what they believe to be the same noun. Their equivalence, truth and weight remain matters for publishers, evidence, graph structure and consuming systems.

Because context hierarchy is namespace-controlled, the standard does not need to settle how many kinds or layers of context exist. Useful conventions may evolve through adoption rather than being constitutionalised in the primitive.

## Relationship to other ADRs

ADR-001 establishes the self-contained two-ended Village Link primitive. This ADR specifies the treatment of the endpoint identifiers A and B without enlarging that primitive.

ADR-003 governs the reference publisher implementation. The reference MediaWiki may use its existing redirect, disambiguation and governance machinery to make these endpoint namespaces usable by humans.