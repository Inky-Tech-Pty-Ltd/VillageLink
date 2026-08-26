# Village Link Glossary

**Status:** Working draft  
**Last updated:** 26 August 2026

## Purpose

This glossary records how the Village Link project currently uses important terms.

The definitions are intended to make project documents internally consistent and to expose conceptual disagreements rather than hide them behind ambiguous language. They are not, by themselves, conformance requirements. Where a term acquires a normative meaning in the Village Link specification, the specification takes precedence.

The glossary is deliberately maintained as simple Markdown while the terminology is still evolving. Entries are structured so that they can later be migrated to a terminology-aware specification tool such as **Spec-Up-T**, and aligned or cross-referenced with external glossaries where appropriate.

## Terminology principles

- Prefer one term for one concept.
- Distinguish ordinary-language uses from project-specific meanings where ambiguity matters.
- Reuse established external terminology where it fits rather than creating unnecessary Village Link vocabulary.
- Record deprecated or superseded terms when older project material may still contain them.
- Treat definitions as revisable while the architecture remains experimental.
- Do not infer truth merely from the existence of an assertion or memory trace.

---

## Assertion

**Definition:** A claim made by a publisher.

In the core Village Link formulation, the assertion is that two independently meaningful identifiers refer to the same entity: **P asserts A ↔ B**.

**Related terms:** Publisher, Village Link, Entity, Identifier.

---

## Context

**Definition:** The circumstances or system within which an identifier has meaning.

Context is not used as a synonym for *memory system*. A memory system may provide a context in which an identifier is meaningful, but the concepts are distinct.

**Related terms:** Identifier, Memory system.

---

## Entity

**Definition:** A person, organisation, software agent, object or other thing that can be referred to by identifiers and about which memory traces may exist.

Village Link does not require an entity to be a human or to possess a single canonical identity.

**Related terms:** Identifier, Memory trace, Star Credential.

---

## Governance

**Definition:** A process by which norms and anticipated or actual consequences constrain or shape the behaviour of entities.

Governance may operate across multiple memory systems. An action may occur in one system, be assessed against a norm somewhere else, and lead to a consequence or sanction recorded or imposed somewhere else again.

Governance therefore does not require an entity to belong to a single *governance system*.

**Related terms:** Memory system, Norm, Sanction.

---

## Governance system

**Status:** Discouraged as a generic project term.

**Definition:** A system that participates in governance by establishing, applying or enforcing norms or consequences.

Earlier Village Link discussions sometimes used *governance system* for the broader category now called *memory system*. That usage is deprecated because a memory system need not contain norms or sanctions, and governance may emerge across several systems rather than reside in one.

**Preferred term:** Memory system, when referring to the generic system capable of retaining traces.

---

## Identifier

**Definition:** A reference that identifies or denotes an entity within a context.

Village Link connects independently meaningful identifiers. The endpoint systems do not need to share an identifier scheme or implement Village Link.

**Related terms:** Entity, Context, URI, Village Link.

---

## Memory system

**Definition:** A system capable of retaining traces associated with entities.

A memory system may record accounts, memberships, transactions, permissions, observations, endorsements, sanctions or other history. It may contain norms about how entities should behave, but it need not. It may record breaches or sanctions, but it need not.

A memory system therefore need not exercise authority over, or even interact directly with, the entity it remembers.

**Related terms:** Memory trace, Governance, Reputation system, Context.

---

## Memory trace

**Definition:** Information retained by a memory system and associated with an entity, its activity, relationships or history.

A trace need not be evaluative. Its existence does not establish that its contents are true, current or authoritative.

**Short form:** Trace.

**Related terms:** Memory system, Entity, Reputation.

---

## Norm

**Definition:** An expectation, rule or standard concerning how an entity should behave.

A norm may be formal or informal and need not be stored in the same memory system as the actions assessed against it or any resulting sanction.

**Related terms:** Governance, Sanction, Memory system.

---

## Publisher

**Definition:** The entity that publishes a Village Link assertion.

Publication records that the publisher made the assertion; it does not make the assertion true. Multiple publishers may make matching, overlapping or conflicting assertions.

**Symbol:** **P** in the formulation **P asserts A ↔ B**.

**Related terms:** Assertion, Village Link.

---

## Reputation

**Definition:** An evaluative understanding of an entity derived from memories, observations, assertions or other evidence.

Village Link does not itself calculate or determine reputation. Reputation may be inferred by observers or applications from traces distributed across one or more memory systems.

**Related terms:** Memory trace, Reputation system, Governance.

---

## Reputation system

**Definition:** A memory system whose retained traces are used to support evaluative judgments about entities.

A reputation system is therefore a kind of memory system, not the generic category. Earlier Village Link material sometimes used *reputation system* more broadly; that usage is deprecated.

**Broader term:** Memory system.

**Related terms:** Reputation, Memory trace.

---

## Sanction

**Definition:** A consequence imposed or experienced in response to an assessed breach of a norm.

A sanction need not be imposed by the same system in which the relevant action occurred, the norm was expressed, or the breach was assessed.

**Related terms:** Governance, Norm, Memory system.

---

## Star Credential

**Definition:** A graph of independently meaningful identifiers and associated memory traces that can be traversed together as referring to the same entity.

A Star Credential is not a new master identity issued by a central authority. It is a structure that may emerge from multiple Village Links and the systems they connect.

The architecture and terminology of the Star Credential remain under active development.

**Related terms:** Village Link, Entity, Identifier, Memory system.

---

## URI

**Definition:** Uniform Resource Identifier.

Village Link currently uses URIs for its two independently meaningful endpoints.

**Related terms:** Identifier, Village Link.

---

## Village Link

**Definition:** A published assertion connecting two independently meaningful identifiers as referring to the same entity.

Conceptually: **P asserts A ↔ B**.

The current architectural direction represents a Village Link as a single, self-contained, two-ended hyperlink containing both endpoint URIs. The publisher is identified by publication context rather than encoded as a third endpoint.

A Village Link records an assertion, not an authoritative determination of identity or truth.

**Related terms:** Assertion, Publisher, Identifier, Entity, URI.

---

## Deprecated and historical terminology

The following terms may appear in older project documents or discussions:

| Earlier usage | Current treatment |
| --- | --- |
| **Context** as the name of the endpoint system | Use *memory system* for the generic system; retain *context* for the circumstances in which an identifier has meaning. |
| **Governance system** as the generic endpoint system | Use *memory system*. Governance may operate across multiple memory systems. |
| **Reputation system** as the generic endpoint system | Use *memory system*. A reputation system is a more specific kind of memory system. |

## Future terminology tooling

If the glossary becomes sufficiently stable or Village Link moves further into standards work, consider migrating these definitions to **Spec-Up-T** or compatible terminology tooling. A migration should preserve, where useful:

- preferred terms and definitions;
- aliases and deprecated terms;
- relationships between terms;
- links from specifications and other documents to definitions;
- references to externally governed definitions; and
- machine-readable terminology outputs.

Migration should not require changing the conceptual definitions merely to satisfy the tool.