# Village Link Glossary

**Status:** Working draft  
**Last updated:** 22 September 2026

## Purpose

This glossary records how the Village Link project currently uses important terms. The definitions are intended to make project documents internally consistent. Where a term acquires a normative meaning in the specification, the specification takes precedence.

## Terminology principles

- Prefer one term for one concept.
- Reuse established external terminology where it fits.
- Record deprecated or superseded terms when older project material may still contain them.
- Do not infer truth merely from the existence of a statement or memory trace.

---

## Consequence

**Definition:** An outcome associated with an entity's behaviour, including outcomes arising from assessment against a norm.

Consequences may be favourable, adverse or neutral. A favourable consequence may function as a reward; an adverse consequence may function as a sanction.

---

## Constraint

**Definition:** A limit or pressure on possible behaviour arising from norms and anticipated or actual consequences.

An entity subject to multiple memory systems may experience overlapping constraints, including civilising and chilling effects.

---

## Context

**Definition:** The circumstances within which an identifier or memory trace has meaning.

A context may be provided by, or represented within, a memory system. *Context* describes where something has meaning; *memory system* describes a system capable of retaining traces.

---

## Entity

**Definition:** A person, organisation, software agent, object or other thing that can be referred to by identifiers and about which memory traces may exist.

Village Link does not require an entity to be human or to possess a single canonical identity.

---

## Global context

**Definition:** The universal set, relative to the universe of discourse of the Village Link model.

A claim of global context does **not** imply that a representation is authoritative, canonical, verified or true. It is a claim about scope of context.

**Prefix convention:** `gc.`

A URI beneath a `gc.` namespace may identify a noun without restriction to a particular memory-system context, for example `https://gc.village.link/JoeRasmussen`.

---

## Governance

**Definition:** For an entity, the consequences that arise from the memory systems in which it has left a trace.

Governance may operate across multiple memory systems. Anticipated consequences may also create constraints that shape the entity's behaviour.

---

## Governance system

**Status:** Discouraged as a generic project term.

Earlier Village Link discussions sometimes used *governance system* for the broader category now called *memory system*. That usage is deprecated.

---

## Identifier

**Definition:** A reference that identifies or denotes an entity within a context.

Village Link connects independently meaningful identifiers. Endpoint systems do not need to share an identifier scheme or implement Village Link.

An identifier may also serve as a key by which an application queries a memory system; the identifier does not, by itself, select that memory system.

---

## Memory system

**Definition:** A system capable of retaining traces associated with entities.

A memory system may record accounts, memberships, transactions, permissions, observations, endorsements, rewards, sanctions or other history. It need not exercise authority over, or interact directly with, the entity it remembers.

---

## Memory trace

**Definition:** Information retained by a memory system and associated with an entity, its activity, relationships or history.

A trace need not be evaluative. Its existence does not establish that its contents are true, current or authoritative.

---

## Norm

**Definition:** An expectation, rule or standard concerning how an entity should behave.

---

## Reputation

**Definition:** An evaluative understanding of an entity derived from memories, observations, statements or other evidence.

Village Link does not itself calculate or determine reputation.

---

## Reputation system

**Definition:** A memory system whose retained traces are used to support evaluative judgments about entities.

A reputation system is a kind of memory system, not the generic category.

---

## Reward

**Definition:** A favourable consequence associated with an entity's behaviour or with an assessment of that behaviour against a norm.

---

## Sanction

**Definition:** An adverse consequence associated with an entity's behaviour or with an assessed breach of a norm.

---

## Split screen

**Definition:** The reference browser view that displays the two endpoint resources of a Village Link simultaneously, with A in one pane and B in the other.

The split screen is a browser interaction convention, not part of the Village Link primitive itself. Either pane may subsequently be promoted to ordinary single-page browsing.

---

## Star Credential

**Definition:** A domain-independent centred collection `SC(A,S)`, where A is one distinguished centre URI and S is a finite unordered set of B URIs.

Its semantic content is the set of same-entity relations `{ A ↔ B | B is a member of S }`.

A Star Credential is not a new master identity issued by a central authority. Its centre may claim global context, but need not. A Star Credential does not require a marker domain and does not require its members to be expanded into complete encoded Village Link URIs.

A concrete JSON or other machine-readable form is a **Star Credential serialization**, not the credential itself.

---

## Statement

**Definition:** Content stated by a web resource W through publication of a Village Link or Star Credential.

For an individual Village Link:

**W states A ↔ B.**

For a Star Credential:

**W states SC(A,S).**

The word *states* does not imply that W is a moral agent, that the statement is true, or that the operator or author of W warrants it.

---

## Triple bar

**Definition:** The reference browser chrome used when displaying a Village Link: one bar for the Village Link URI and one address bar for each of its two endpoint panes.

The triple bar makes the composite edge and its two independently navigable endpoints simultaneously visible. It is a reference-browser interaction convention, not part of the Village Link primitive itself.

---

## URI

**Definition:** Uniform Resource Identifier.

Village Link currently uses URIs for its two independently meaningful endpoints.

---

## Village context

**Definition:** A contextual namespace in which an identifier has meaning within a particular context or hierarchy of contexts.

**Prefix convention:** `vc.`

A `vc.` namespace may use recursive path structure, for example `https://vc.village.link/FamilyChristmas/2025/JoeRasmussen`.

The path structure is controlled by the namespace and is not assigned universal semantics by the core standard.

---

## Village Link

**Definition:** A single self-contained two-ended URI encoding one same-entity relation between independently meaningful endpoint identifiers A and B.

At the semantic layer:

**A ↔ B**

At the encoding layer, conceptually:

`<domain>[A][B]`

When the encoded Village Link is found on a web resource W:

**W states A ↔ B.**

Diagrammatically at the publication layer: **A ← W → B**.

W is external to the encoded Village Link. The marker domain inside the encoded URI is not W and is not, merely by appearing in the encoding, the publisher or a trust authority.

---

## Marker domain

**Definition:** The domain component beneath the `wab.` marker used to construct an encoded Village Link as an ordinary HTTPS URI.

General candidate form: `https://wab.<domain>/<encoded-A>!<encoded-B>`.

The marker domain is part of the encoding layer. It is not W, need not be the publisher, and does not gain authority over A, B or their relation merely by appearing in the URI.

---

## WAB marker

**Definition:** The adopted DNS-prefix convention `wab.` identifying the two-ended Village Link form within an HTTPS authority.

General candidate form: `https://wab.<domain>/<encoded-A>!<encoded-B>`.

Reference instance: `https://wab.village.link/<encoded-A>!<encoded-B>`.

The prefix is deliberately not an abbreviation of *Village Link*. This reduces project-specific branding in a convention intended for adoption by independent or competing parties.

`wab` remains a compact mnemonic for the two-ended web structure **A ← W → B**. The W in that mnemonic is the web resource at publication time; it is not the marker domain encoded in the URI.

`wab.` is a marker convention, not a central registry, resolver, trust authority or new URI scheme. Other domain owners may use the convention beneath authorities they control.

The `wab.` marker is adopted; the current `!` separator and endpoint escaping remain under test.

---

## Web resource

**Definition:** The web resource in which an encoded Village Link or serialized Star Credential is found.

**Symbol:** **W** in **W states A ↔ B** or **W states SC(A,S)**.

For an ordinary hyperlink, the structural relationship can be represented as **W → A**. For a published Village Link it becomes **A ← W → B**.

W is publication context, not part of the encoded Village Link. The existence of a statement on W does not by itself establish who authored, controls or endorses W, or whether the statement is true.

---

## Adopted prefix family

The project uses three conventional DNS prefixes:

| Prefix | Meaning |
| --- | --- |
| `wab.` | Marker for the two-ended Village Link form; mnemonic for A–W–B. |
| `gc.` | Global-context endpoint naming. |
| `vc.` | Village-context endpoint naming. |

These are conventions within ordinary HTTPS/DNS naming, not new URI schemes.

---

## Layer terminology

Current documents should name the relevant layer when ambiguity is possible:

| Layer | Preferred term |
| --- | --- |
| `A` | Endpoint identifier |
| `A ↔ B` | Same-entity relation |
| `<domain>[A][B]` | Village Link / encoded Village Link |
| `W states <domain>[A][B]` | Published Village Link statement |
| `SC(A,S)` | Star Credential |
| JSON or another concrete form of `SC(A,S)` | Star Credential serialization |
| `W states SC(A,S)` | Published Star Credential statement |

Avoid using **the primitive** when it is unclear which of these layers is intended.

---

## Deprecated and historical terminology

| Earlier usage | Current treatment |
| --- | --- |
| **Assertion / asserts** for the core Village Link relation | Prefer *statement / states*: **W states A ↔ B**. |
| **Publisher (P)** as a component of the core primitive | Superseded by **W states A ↔ B**. Publisher remains valid for actual publication roles and processes. |
| **`vl.`** as the Village Link marker prefix | Superseded by **`wab.`**. `vl.` carried unnecessary Village Link branding; `wab.` is project-neutral and mnemonic of A–W–B. |
| **Context** as the generic endpoint system | Prefer *memory system* where the system's capacity to retain traces matters. |
| **Governance system** as the generic endpoint system | Use *memory system*. |
| **Reputation system** as the generic endpoint system | Use *memory system*. A reputation system is a more specific kind of memory system. |

## Future terminology tooling

If the glossary becomes sufficiently stable or Village Link moves further into standards work, consider migrating these definitions to Spec-Up-T or compatible terminology tooling.