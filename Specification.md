# Village Link Specification

**Version:** Draft 0.1  
**Date:** 6 September 2026  
**Status:** Experimental

## 1. Scope

This document specifies the current Village Link core primitive and the abstract structure of a Star Credential built from Village Links.

A Village Link is a two-ended hyperlink found on a web resource W, stating that two independently meaningful identifiers refer to the same entity.

Conceptually:

**W states A ↔ B.**

Diagrammatically:

**A ← W → B**

This specification defines the semantics and current structural requirements of that statement. It does not define a universal identity system, truth service, reputation algorithm, governance system or application architecture.

The project requirements are recorded in [Requirements.md](Requirements.md). Terms are used as defined in [Glossary.md](Glossary.md). The architectural decision underlying the Village Link primitive is recorded in [ADR-001](docs/adr/001-two-ended-uri.md). The Star Credential data model is recorded in [ADR-004](docs/adr/004-star-credential-data-model.md). Endpoint naming is recorded in [ADR-005](docs/adr/005-endpoint-identifiers-and-naming.md). Serialization is recorded in [ADR-006](docs/adr/006-village-link-serialization.md).

## 2. Conventions

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** indicate normative requirements for this draft.

Because this is Draft 0.1, syntax and some conformance rules remain unsettled. Sections explicitly marked **Open** or **Proposed** are informative and MUST NOT be interpreted as settled normative syntax.

## 3. Conceptual model

A Village Link involves:

- **W — Web resource:** the resource on which the Village Link statement is found.
- **A — Endpoint A:** an independently meaningful identifier.
- **B — Endpoint B:** another independently meaningful identifier.
- **E — Entity:** the entity referred to by both A and B.

The core statement is:

> W states that A and B refer to the same E.

E is semantic rather than a required encoded field. A Village Link does not require a separate canonical identifier for E.

W is not encoded as a third endpoint in the Village Link. A and B are encoded in the link itself; W is the web resource in which the link is found.

The structural relationship is therefore **A ← W → B**.

## 4. Village Link semantics

### 4.1 Same-entity statement

A conforming Village Link states equivalence of reference for its two endpoints: A and B identify or denote the same entity in their respective contexts.

The statement does not mean that:

- A and B are textually identical;
- the endpoint systems are equivalent;
- all information associated with A applies to B;
- either endpoint system endorses the statement;
- the operator, author or publisher of W controls either endpoint; or
- the statement is objectively true.

### 4.2 Symmetry and encoded order

At the semantic level **A ↔ B** is symmetric.

The serialized order of A and B is nevertheless preserved. A Village Link-aware application MAY use that order for presentation, for example by displaying A in a left pane and B in a right pane. A global-context identifier may commonly be placed in A.

Two serializations containing A,B and B,A may therefore differ while expressing the same mathematical same-entity statement. Implementations MUST NOT infer greater semantic authority merely from endpoint position.

### 4.3 Publication

A Village Link statement occurs on W. Publication, authorship, control and provenance of W are distinct questions from the minimal relation stated by the link.

The same encoded A ↔ B pair may occur on multiple web resources. Applications and indexes SHOULD preserve the identity of W where provenance, publication or trust is relevant.

A publisher may publish W, but the publisher is not a component or symbol of the core primitive.

### 4.4 Truth and authority

Conformance establishes only that a statement is expressed as a Village Link. It does not establish that the statement is true, current, authorised, supported by evidence or worthy of trust.

## 5. Endpoint requirements

### 5.1 URI endpoints

A and B MUST each be represented by a URI. Each endpoint URI MUST be independently meaningful outside the Village Link itself. The endpoint URI does not have to be publicly dereferenceable.

### 5.2 Endpoint-system independence

An endpoint system is not required to know that Village Link exists, expose a Village Link API, modify the endpoint resource, publish reciprocal information or approve the Village Link statement.

### 5.3 Endpoint availability

Failure to dereference A or B MUST NOT, by itself, make the Village Link syntactically invalid. Endpoint availability MAY affect an application's assessment of the statement.

### 5.4 Adopted endpoint prefix conventions

Existing URI identifiers MAY be used directly as Village Link endpoints.

Where a suitable endpoint URI does not already exist, the project adopts two conventional DNS prefixes:

- `gc.` — **global context**: an identifier intended to identify a noun without restriction to a particular memory-system context; and
- `vc.` — **village context**: an identifier within a contextual namespace.

Reference examples include:

```text
https://gc.village.link/JoeRasmussen
https://vc.village.link/FamilyChristmas/JoeRasmussen
https://vc.village.link/FamilyChristmas/2025/JoeRasmussen
```

`gc.` and `vc.` are naming conventions, not privileged endpoint types. `gc.` does not assert truth, unique canonicality, legal privilege or endorsement by Village Link.

These are conventional HTTPS/DNS prefixes, not new `gc:` or `vc:` URI schemes. Other domain owners may adopt the same conventions beneath domains they control. The core standard does not require registration with or permission from `village.link`.

### 5.5 Recursive context hierarchy

A `vc.` namespace MAY use a recursive or hierarchical path. The core standard does not assign universal semantics to individual path segments; the namespace that mints an endpoint controls its internal naming structure.

Memory systems and contexts are themselves nouns and may participate in Village Links like other nouns.

### 5.6 Naming assistance

A publisher MAY provide human-facing facilities for endpoint naming, including friendly labels, redirects, disambiguation and context hierarchies. These facilities belong to the publisher layer and are not requirements of the core primitive.

## 6. Village Link representation

### 6.1 Self-contained two-ended form

A Village Link MUST be a single self-contained identifier containing representations of both endpoint URIs.

Conceptually:

```text
[wab marker] [encoded URI A] [separator] [encoded URI B]
```

A parser MUST be able to recover A and B without dereferencing a separate Village Link resource.

### 6.2 Adopted `wab.` marker; candidate separator

The project adopts `wab.` as the DNS marker prefix for the two-ended Village Link form. The prefix is deliberately independent of Village Link branding and provides a compact mnemonic for **A ← W → B**.

The reference form is currently:

```text
https://wab.village.link/<encoded-A>!<encoded-B>
```

In this form:

- `https` uses conventional URI and browser infrastructure;
- `wab.` is the adopted marker convention;
- `wab.village.link` is the reference marker implementation;
- `!` is the **proposed** structural boundary between A and B; and
- the encoded order of A and B is preserved.

`wab.village.link` is not a central registry, resolver or privileged authority. Other domain owners MAY expose the same marker convention through authorities they control, for example:

```text
https://wab.github.com/<encoded-A>!<encoded-B>
https://wab.example.org/<encoded-A>!<encoded-B>
```

No registration with or permission from `village.link` is required.

The project's reference browser MUST, when it encounters an HTTPS URI whose first DNS label is `wab`, first attempt to parse it locally as a Village Link before ordinary web dereferencing. Successful parsing MUST NOT depend on dereferencing the marker host. If local parsing fails, the browser MUST fall back to ordinary HTTPS handling.

Marker recognition MUST NOT be treated as evidence that the statement is true, trusted or authorised.

A literal `!` belonging to A or B must be escaped so that it cannot be confused with the structural separator. The exact escaping algorithm remains **Open**. The `wab.` marker is adopted; the `!` separator and endpoint escaping MUST NOT be treated as accepted wire syntax until the tests described in ADR-006 pass.

### 6.3 Serialization acceptance criterion — Open

For arbitrary valid endpoint URIs A and B, the eventual construction and parsing algorithms must satisfy:

```text
parse(make(A, B)) == (A, B)
```

Testing must exercise reserved characters, percent-encoded material, queries, fragments, Unicode or internationalised material, non-HTTP URI schemes and nested URI material.

### 6.4 No required dereferenceable link object

A conforming Village Link MUST NOT require a separate resource to be dereferenced in order to discover A and B.

A publisher or application MAY additionally provide a page, record, API resource, evidence bundle or other object describing the statement. Such an object is supplementary.

A marker operator MAY provide useful dereferencing behaviour for conventional browsers, including at `wab.village.link`. Such behaviour does not make dereferencing a requirement for parsing the primitive.

## 7. Web resource, publication and provenance

### 7.1 W

W is the web resource on which the Village Link statement is found.

The primitive does not by itself establish who authored, controls, publishes or endorses W. Those are provenance questions about W rather than an additional endpoint of the link.

### 7.2 Provenance mechanism — Open

Draft 0.1 does not prescribe a universal mechanism for proving authorship or control of W. A later revision should clarify treatment of copied links, quotations, mirrors, syndication, caches, archives, screenshots and compromised or transferred publishing contexts.

## 8. Multiplicity and conflict

The same A ↔ B statement MAY occur on multiple web resources. Web resources MAY also contain statements which, when combined, are inconsistent or disputed.

The core standard does not resolve such conflicts. An application MAY use provenance, publisher reputation, evidence, timestamps, graph structure, endpoint properties or other information to evaluate competing statements.

No universal trust weighting is specified.

## 9. Evidence and metadata

Evidence, timestamps, observations, confidence values and similar metadata are useful but are not currently fields of the minimal Village Link primitive.

Publishers and indexes MAY associate such metadata with a statement. Implementations SHOULD distinguish the Village Link statement itself from supporting evidence, provenance evidence, observation/publication time and later observations about its status.

## 10. Lifecycle

A Village Link statement may outlive the conditions under which it appeared. Relevant changes may include transfer or compromise of an endpoint, abandonment or reassignment of an identifier, change in the represented entity, retraction or alteration of W, or loss of provenance information.

**Open:** Draft 0.1 does not yet specify lifecycle states, revocation, retraction or expiry mechanisms.

## 11. Star Credentials and graph interpretation

### 11.1 Graph interpretation

Village Links can be combined into a graph. If W1 states A ↔ B and W2 states B ↔ C, an application may investigate whether A, B and C refer to the same entity. The core specification does not require that conclusion: transitive inference remains an application-level judgment.

### 11.2 Star Credential definition

A **Star Credential** consists of one distinguished centre noun A and a finite unordered set of nouns B.

If the B set is `S = {B1, B2, ... Bn}`, then the credential is `SC(A, S)` and states `{ A ↔ B | B is a member of S }` through its constituent Village Links.

The abstract structure is:

```text
[A]{[B1], [B2], ... [Bn]}
```

Each noun MUST be represented by a URI endpoint identifier satisfying Section 5. A MUST be recorded once as the centre. Each B MUST be recorded as a member of the associated set.

### 11.3 Unordered membership

The B nouns form a set, not an ordered list. Implementations MUST NOT assign semantic significance to their order. A B noun MUST NOT occur more than once.

Accordingly `SC(A, {B1, B2}) = SC(A, {B2, B1})` at the credential-content level.

### 11.4 Status of the centre

A is distinguished because it is the centre of this Star Credential. That structural role does not make the constituent Village Links directional: for each member B, the relation remains **A ↔ B**.

### 11.5 Serialization and presentation — Open

Draft 0.1 specifies the abstract Star Credential structure but does not prescribe a concrete serialization. A future serialization MUST preserve the distinction between A and the unordered B set.

## 12. Relationship to memory systems and governance

Village Link endpoints may identify entities within memory systems: systems capable of retaining traces associated with entities.

Village Link does not itself calculate reputation, establish norms, assess behaviour or impose consequences. Applications may use Village Link graphs to make relationships among memories, reputation and governance more traversable.

## 13. Privacy, abuse and harms

Publishing a connection between identifiers can reveal information that was previously difficult to correlate. Potential harms include unwanted identity correlation, impersonation, stalking, discrimination, amplification of inaccurate statements, exposure of abandoned identities and graph-based inference.

Conformance to Village Link syntax does not imply that publication is safe, ethical or lawful.

## 14. Conformance

A **conforming Village Link**:

1. contains exactly two endpoint URIs;
2. permits both endpoints to be recovered without dereferencing a separate Village Link resource;
3. states that both endpoints refer to the same entity; and
4. is found on a web resource W, which is not encoded as a third endpoint.

A **conforming consumer** MUST NOT interpret syntactic conformance as proof of truth and MUST NOT require cooperation from endpoint systems merely to parse the Village Link.

A conforming **Star Credential** designates exactly one centre noun A, contains a finite unordered set of B nouns without duplicates, and states one conforming Village Link A ↔ B for every B in the set.

## 15. Open specification issues

The following issues remain unresolved in Draft 0.1:

1. exact escaping of A and B within the `https://wab.village.link/<encoded-A>!<encoded-B>` form;
2. torture-test results for the proposed `!` separator;
3. canonical representation and equality comparison;
4. practical URI-length limits;
5. provenance rules for W;
6. copying, quotation, syndication and archival semantics;
7. lifecycle, retraction, expiry and compromise;
8. standard metadata and evidence formats;
9. discovery and indexing conventions;
10. final browser and user-agent behaviour;
11. privacy and harms requirements; and
12. Star Credential serialization and signing.

The current centre of the design remains deliberately small:

**W states A ↔ B.**

**A ← W → B**