# Village Link Specification

**Version:** Draft 0.1  
**Date:** 4 September 2026  
**Status:** Experimental

## 1. Scope

This document specifies the current Village Link core primitive.

Village Link provides a way for a publisher to publish an assertion that two independently meaningful identifiers refer to the same entity.

Conceptually:

**P asserts A ↔ B.**

This specification defines the semantics and current structural requirements of that assertion. It does not define a universal identity system, truth service, reputation algorithm, governance system or application architecture.

The project requirements are recorded in [Requirements.md](Requirements.md). Terms are used as defined in [Glossary.md](Glossary.md). The architectural decision underlying this specification is recorded in [ADR-001](docs/adr/001-two-ended-uri.md). Endpoint naming is recorded in [ADR-005](docs/adr/005-endpoint-identifiers-and-naming.md). The current serialization candidate is recorded in [ADR-006](docs/adr/006-village-link-serialization.md).

## 2. Conventions

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** in this document indicate normative requirements for this draft.

Because this is Draft 0.1, syntax and some conformance rules remain unsettled. Sections explicitly marked **Open** or **Proposed** are informative and MUST NOT be interpreted as settled normative syntax.

## 3. Conceptual model

A Village Link involves four concepts:

- **P — Publisher:** the entity publishing the assertion.
- **A — Endpoint A:** an independently meaningful identifier.
- **B — Endpoint B:** another independently meaningful identifier.
- **E — Entity:** the entity that P asserts is referred to by both A and B.

The core assertion is:

> P asserts that A and B refer to the same E.

E is semantic rather than a required encoded field. A Village Link does not require a separate canonical identifier for E.

P is also not encoded as a third endpoint in the core primitive. P is established by publication context.

A and B are encoded in the Village Link itself.

## 4. Village Link semantics

### 4.1 Same-entity assertion

A conforming Village Link asserts equivalence of reference for its two endpoints: the publisher is asserting that A and B identify or denote the same entity in their respective contexts.

The assertion does not mean that:

- A and B are textually identical;
- the endpoint systems are equivalent;
- all information associated with A applies to B;
- either endpoint system endorses the assertion;
- the publisher controls either endpoint; or
- the assertion is objectively true.

### 4.2 Symmetry and encoded order

At the semantic level:

**A ↔ B**

is symmetric.

The serialized order of A and B is nevertheless preserved. A Village Link-aware application MAY use that order for presentation, for example by displaying A in a left pane and B in a right pane. Naming conventions may also encourage a conventional order; for example, an unrestricted or global-context identifier may commonly be placed in A.

The serializations `VL(A,B)` and `VL(B,A)` may therefore differ while expressing the same mathematical same-entity assertion.

Implementations MUST NOT infer greater semantic authority merely from endpoint position unless additional application-specific information establishes it.

### 4.3 Publication

The act of publication is part of the meaning of a Village Link.

A bare endpoint pair does not by itself identify P. An observer interprets the assertion in a publication context that supplies evidence about who published it.

Accordingly, the same encoded A ↔ B pair published by P1 and P2 represents two publisher-attributed assertions:

**P1 asserts A ↔ B**

**P2 asserts A ↔ B**

Applications and indexes MUST be able to preserve that distinction where publisher attribution is relevant.

### 4.4 Truth and authority

Conformance to this specification establishes only that an assertion is expressed as a Village Link.

It does not establish that the assertion is:

- true;
- current;
- authorised by the entity;
- authorised by either endpoint system;
- supported by evidence; or
- worthy of trust.

Those judgments belong to publishers, observers, evidence systems and applications.

## 5. Endpoint requirements

### 5.1 URI endpoints

In Draft 0.1, A and B MUST each be represented by a URI.

Each endpoint URI MUST be independently meaningful: an observer that encounters the URI outside the Village Link must be able, in principle, to interpret it as an identifier within its own context.

The endpoint URI does not have to be publicly dereferenceable.

### 5.2 Endpoint-system independence

A system responsible for an endpoint URI is not required to:

- know that Village Link exists;
- expose a Village Link API;
- modify the endpoint resource;
- publish reciprocal information; or
- approve the Village Link assertion.

### 5.3 Endpoint availability

Failure to dereference A or B MUST NOT, by itself, make the Village Link syntactically invalid.

An endpoint may be unavailable because it has moved, requires authentication, is temporarily offline, has been deleted, uses a non-HTTP URI scheme, or for other reasons.

Endpoint availability MAY affect an application's assessment of the assertion.

### 5.4 Endpoint naming conventions

Existing URI identifiers MAY be used directly as Village Link endpoints.

Where a suitable endpoint URI does not already exist, a publisher may mint one. Village Link proposes two useful naming conventions:

- `gc` — **global context**: an identifier intended to identify a noun without restriction to a particular memory-system context; and
- `vc` — **village context**: an identifier within a contextual namespace.

For the reference publisher, examples include:

```text
https://gc.village.link/JoeRasmussen
https://vc.village.link/FamilyChristmas/JoeRasmussen
https://vc.village.link/FamilyChristmas/2025/JoeRasmussen
```

`gc` and `vc` are naming conventions, not privileged endpoint types in the Village Link primitive. In particular, `gc` does not assert that an identifier is true, uniquely canonical, legally privileged or endorsed by Village Link.

The reference publisher uses conventional HTTPS and DNS syntax. Village Link does not introduce new `gc:` or `vc:` URI schemes.

Other publishers MAY adopt the same conventions under domains they control, or MAY use different naming conventions. The core standard does not require registration with or permission from `village.link`.

### 5.5 Recursive context hierarchy

A contextual namespace MAY use a recursive or hierarchical path. For example:

```text
https://vc.village.link/FamilyChristmas/2025/JoeRasmussen
```

may represent a hierarchy of context, subcontext and noun.

The core standard does not assign universal semantics to individual path segments. The namespace that mints an endpoint controls its internal naming structure.

Memory systems and contexts are themselves nouns. They may therefore have their own endpoint identifiers, reputations and star credentials, and may participate in Village Links like other nouns.

### 5.6 Reference-publisher naming assistance

The reference publisher MAY provide human-facing facilities for endpoint naming, including friendly labels, redirects, disambiguation and context hierarchies.

These facilities belong to the publisher layer and are not requirements of the core Village Link primitive.

## 6. Village Link representation

### 6.1 Self-contained two-ended form

A Village Link MUST be a single self-contained identifier containing representations of both endpoint URIs.

Conceptually:

```text
[Village Link marker] [encoded URI A] [separator] [encoded URI B]
```

A parser presented with the Village Link MUST be able to recover A and B without dereferencing a separate Village Link resource.

### 6.2 Candidate HTTPS serialization — Proposed

The leading Draft 0.1 serialization candidate is:

```text
https://vl.village.link/<encoded-A>!<encoded-B>
```

In this candidate:

- `https` uses conventional URI and browser infrastructure;
- `vl.village.link` identifies the reference Village Link form;
- `!` is the structural boundary between A and B; and
- the encoded order of A and B is preserved.

`vl.village.link` is the reference marker, not a central registry, resolver or privileged authority. The first DNS label `vl` is the marker convention within an HTTPS authority controlled by a domain owner. Other domain owners MAY expose the same candidate serialization through marker authorities they control, for example:

```text
https://vl.github.com/<encoded-A>!<encoded-B>
https://vl.example.org/<encoded-A>!<encoded-B>
```

No registration with or permission from `village.link` is required.

The project's reference browser MUST, when it encounters an HTTPS URI whose first DNS label is `vl`, first attempt to parse it locally as a Village Link before ordinary web dereferencing. Successful parsing MUST NOT depend on dereferencing the marker host. If local Village Link parsing fails, the browser MUST fall back to ordinary HTTPS handling.

A matching marker or successfully parsed Village Link form MUST NOT, by itself, be treated as evidence that the assertion is true, trusted, authorised or published by either endpoint system. Publisher attribution remains governed by publication context.

A literal `!` belonging to A or B must be escaped so that it cannot be confused with the structural separator.

The exact escaping algorithm for arbitrary endpoint URIs remains **Open**. The candidate MUST NOT be treated as accepted wire syntax until it passes URI-conformance, conventional-browser and exact round-trip tests as described in ADR-006.

Opaque Base64url encoding is retained as a technically straightforward fallback, but is not preferred because it destroys useful human readability in endpoint URIs.

### 6.3 Serialization acceptance criterion — Open

For arbitrary valid endpoint URIs A and B, the eventual construction and parsing algorithms must satisfy:

```text
parse(make(A, B)) == (A, B)
```

Testing must exercise reserved characters, percent-encoded material, queries, fragments, Unicode or internationalised material, non-HTTP URI schemes and nested URI material.

Representative output must also be tested in conventional browsers and URI libraries to establish that significant information is not unexpectedly reinterpreted, normalised or destroyed.

### 6.4 No required dereferenceable link object

A conforming Village Link MUST NOT require a separate resource to be dereferenced in order to discover A and B.

A publisher or application MAY additionally provide a page, record, API resource, evidence bundle or other object describing the assertion. Such an object is supplementary and is not the core Village Link primitive.

A marker operator MAY provide useful dereferencing behaviour for conventional browsers. This includes the reference `vl.village.link` service and other marker authorities operated beneath domains their owners control. Such behaviour does not make dereferencing a requirement for parsing or interpreting the primitive.

## 7. Publisher attribution

### 7.1 Publication context

P is established by the context in which the Village Link is published.

Examples may include publication on a web page, in a signed document, in a repository, through an authenticated service, or through another medium capable of providing evidence of provenance.

### 7.2 Attribution mechanism — Open

Draft 0.1 does not yet prescribe a universal mechanism for proving the identity of P.

A later revision MUST clarify the minimum publication-context information necessary for useful attribution and the treatment of:

- copied links;
- quotations;
- mirrors;
- syndication;
- caches;
- archives;
- screenshots and other representations; and
- compromised or transferred publishing contexts.

The intended distinction is between **P making an assertion** and **Q reporting that P made an assertion**.

## 8. Multiplicity and conflict

Village Link is intentionally multi-publisher.

Multiple publishers MAY publish the same A ↔ B assertion.

Publishers MAY also publish assertions which, when combined, are inconsistent or disputed. For example, graph data may imply incompatible identity relationships.

The core Village Link standard does not resolve such conflicts.

An application MAY use publisher reputation, evidence, timestamps, graph structure, endpoint properties or other information to evaluate competing assertions.

No universal trust weighting is specified.

## 9. Evidence and metadata

Evidence, timestamps, observations, confidence values and similar metadata are useful but are not currently fields of the minimal Village Link primitive.

Publishers and indexes MAY associate such metadata with an assertion.

Where metadata is retained, an implementation SHOULD distinguish:

1. the Village Link assertion itself;
2. evidence offered in support of the assertion;
3. evidence of who published it;
4. the time at which it was published or observed; and
5. later observations about its status.

A future specification may standardise some or all of these structures without changing the semantics of the two-ended primitive.

## 10. Lifecycle

A Village Link assertion may outlive the conditions under which it was made.

Relevant changes may include:

- transfer of control of an endpoint;
- compromise of an endpoint or publisher;
- abandonment of an identifier;
- deletion or reassignment of an account;
- change in the entity represented by an identifier;
- retraction by a publisher; or
- loss of the publication context needed to attribute P.

**Open:** Draft 0.1 does not yet specify lifecycle states, revocation, retraction or expiry mechanisms.

Consumers MUST therefore avoid assuming that a historically observed Village Link remains current merely because its encoded form still exists.

## 11. Graph interpretation

Village Links can be combined into a graph.

If P1 publishes A ↔ B and P2 publishes B ↔ C, an application may investigate whether A, B and C refer to the same entity. The core specification does not require that conclusion: transitive inference is an application-level judgment because the underlying assertions may differ in publisher, evidence, age and trustworthiness.

A sufficiently rich graph may support a **Star Credential**: a traversable structure of independently meaningful identifiers and associated memory traces referring to an entity.

A Star Credential is not required for Village Link conformance and is not specified further in Draft 0.1.

## 12. Relationship to memory systems and governance

Village Link endpoints may identify entities within memory systems: systems capable of retaining traces associated with entities.

Village Link does not require an endpoint system to be a reputation system or governance system. Nor does Village Link itself calculate reputation, establish norms, assess behaviour or impose consequences.

Applications may use Village Link graphs to make relationships among memories, reputation and governance more traversable. Those uses remain outside the core primitive.

## 13. Privacy, abuse and harms

Publishing a connection between identifiers can reveal information that was previously difficult to correlate.

Potential harms include unwanted identity correlation, impersonation, stalking, discrimination, amplification of inaccurate assertions, exposure of abandoned identities, and graph-based inference beyond what any individual publisher intended.

Conformance to the Village Link syntax does not imply that publication is safe, ethical or lawful.

**Open:** The project has not yet determined which protections belong in the core standard, in publisher practice, or in consuming applications. This question should be informed by explicit harms assessment rather than resolved implicitly through implementation choices.

## 14. Conformance

Draft 0.1 defines only provisional core conformance.

A **conforming Village Link**:

1. contains exactly two endpoint URIs;
2. permits both endpoints to be recovered without dereferencing a separate Village Link resource;
3. represents the publisher's assertion that both endpoints refer to the same entity; and
4. does not encode the publisher as a third endpoint.

A **conforming consumer**:

1. MUST NOT interpret syntactic conformance as proof of truth;
2. MUST permit publisher attribution to remain distinct from the endpoint pair; and
3. MUST NOT require cooperation from the endpoint systems merely to parse the Village Link.

A more complete conformance model will be possible once serialization and publication-context rules are settled.

## 15. Open specification issues

The following issues are intentionally unresolved in Draft 0.1:

1. exact escaping of A and B within the proposed `https://vl.village.link/<encoded-A>!<encoded-B>` form;
2. torture-test results for the proposed `!` separator;
3. canonical representation and equality comparison;
4. practical URI-length limits;
5. precise publisher-attribution rules;
6. copying, quotation, syndication and archival semantics;
7. lifecycle, retraction, expiry and compromise;
8. standard metadata and evidence formats;
9. discovery and indexing conventions;
10. final browser and user-agent behaviour;
11. privacy and harms requirements; and
12. useful conformance classes beyond the core primitive.

These are specification work, not reasons to enlarge the core assertion prematurely.

The current centre of the design remains deliberately small:

**P asserts A ↔ B.**