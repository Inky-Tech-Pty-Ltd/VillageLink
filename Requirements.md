# Village Link Requirements

**Status:** Draft 0.1  
**Date:** 26 August 2026

## Purpose

This document states the current requirements for the Village Link project.

Village Link is being developed through four conceptually distinct areas:

1. **Develop the standard** — define the primitive, syntax, semantics and conformance rules.
2. **Publish and govern an initial graph** — publish a corpus of Village Link assertions to test the standard and establish useful data.
3. **Interpret the graph** — investigate reader-side discovery, filtering, ranking and trust through Trust Engines.
4. **Manage disclosure** — investigate how entities or publishers present audience-specific subsets of star credentials.

The requirements below are grouped into the standard, the reference publisher and consuming applications. The application requirements apply to both reader-side interpretation and disclosure tools where relevant; the separate concept documents define their different purposes. This separation is intentional: requirements imposed on the standard should not be confused with choices made by a publisher, Trust Engine or Star Credential Manager.

Terms are used as defined in [Glossary.md](Glossary.md). The current architectural decision for the core primitive is recorded in [ADR-001](docs/adr/001-two-ended-uri.md).

Normative keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** indicate the intended strength of requirements. At this early stage they should be read as draft normative language rather than as a claim that the standard is stable.

---

## 1. Requirements for the standard

### Core primitive

**REQ-STD-001 — Two independently meaningful endpoints**  
A Village Link MUST connect two identifiers that are independently meaningful outside the Village Link itself.

**REQ-STD-002 — Same-entity assertion**  
A Village Link MUST express the publisher's assertion that its two endpoint identifiers refer to the same entity.

Conceptually:

**P asserts A ↔ B.**

**REQ-STD-003 — Self-contained assertion**  
The two endpoint identifiers MUST be recoverable from the Village Link itself without requiring dereferencing of a separate Village Link resource.

**REQ-STD-004 — URI endpoints**  
The standard MUST support URIs as endpoint identifiers.

**REQ-STD-005 — Endpoint independence**  
An endpoint system MUST NOT be required to implement, recognise or cooperate with Village Link merely because one of its identifiers appears as an endpoint.

**REQ-STD-006 — Symmetry**  
The semantic assertion connecting A and B MUST NOT imply that one endpoint is intrinsically the source, subject, authority or subordinate of the other.

### Publisher and truth

**REQ-STD-007 — Publisher attribution**  
A Village Link MUST be interpretable as an assertion made by a publisher. The publisher is established through publication context rather than represented as a third endpoint in the core link.

**REQ-STD-008 — Assertion, not adjudication**  
The standard MUST NOT treat publication of a Village Link as proof that the asserted relationship is true, current or authoritative.

**REQ-STD-009 — Independent publication**  
The standard MUST permit multiple publishers independently to publish assertions concerning the same endpoints.

**REQ-STD-010 — Disagreement permitted**  
The standard MUST permit a wider graph to contain assertions that are matching, overlapping, ambiguous or in conflict. Village Link itself MUST NOT require a central mechanism to adjudicate among them.

### Minimality and decentralisation

**REQ-STD-011 — Minimal primitive**  
The core standard SHOULD impose no requirement that is necessary only for a particular application, business model, reputation model or governance model.

**REQ-STD-012 — No required central identity authority**  
The standard MUST NOT require a central authority to establish a canonical identity for an entity.

**REQ-STD-013 — No required Village Link registry or marker authority**  
Publication and interpretation of a Village Link MUST NOT depend on registration in a single central Village Link database or service. `vl.village.link` MUST NOT be treated as the sole permitted marker authority: domain owners MUST be able to operate conforming HTTPS marker namespaces beneath domains they control without registering with or obtaining permission from `village.link`.

**REQ-STD-014 — Existing identifiers**  
The standard SHOULD permit existing identifiers to participate without modification wherever technically practical.

### Lifecycle, safety and interpretation

**REQ-STD-015 — Lifecycle representability**  
The standard MUST allow implementations to distinguish, or otherwise reason about, the continuing status of an assertion where an endpoint or publisher is transferred, compromised, abandoned, deleted or otherwise changes state.

This requirement does not yet prescribe the lifecycle mechanism.

**REQ-STD-016 — Publication context**  
The standard MUST define enough about publication context for an observer to determine what evidence supports attribution of an assertion to P.

**REQ-STD-017 — Copying and quotation**  
The standard MUST address the distinction between making an assertion and reproducing, quoting, indexing, caching or archiving an assertion made by somebody else.

**REQ-STD-018 — No inherited trust**  
The standard MUST NOT require an observer to trust an assertion merely because it conforms to Village Link syntax.

**REQ-STD-019 — Harms remain assessable**  
The standard SHOULD preserve sufficient information for downstream systems and researchers to assess privacy, abuse, impersonation, unwanted correlation and other harms created or amplified by published links.

### Extensibility

**REQ-STD-020 — Application independence**  
The standard MUST permit applications to derive additional structures — including Star Credentials, reputation models, authentication paths and governance relationships — without making those structures part of the core Village Link assertion.

**REQ-STD-021 — Entity neutrality**  
The standard MUST NOT assume that the entity referred to by the endpoints is a human. People, organisations, software agents, objects and other entities MAY be represented where suitable identifiers exist.

---

## 2. Requirements for publishing an initial graph

These requirements apply to the project's experimental publishing role. They are not automatically requirements of every conforming Village Link publisher.

**REQ-PUB-001 — Standards-conforming corpus**  
The initial graph SHOULD use the current Village Link specification except where an experiment deliberately tests a proposed change or known edge case.

**REQ-PUB-002 — Publisher visibility**  
The publication mechanism MUST make the publication context sufficiently clear to test publisher attribution.

**REQ-PUB-003 — Evidence retention**  
For experimental and research purposes, the initial corpus SHOULD retain evidence supporting each assertion where such evidence can lawfully and responsibly be retained.

Evidence is metadata about the publication process; it is not part of the minimal two-ended primitive unless the specification later says otherwise.

**REQ-PUB-004 — Observation time**  
The corpus SHOULD record when an assertion or its supporting evidence was observed, sampled or published.

**REQ-PUB-005 — Multiple publishers**  
The initial graph SHOULD include examples in which multiple publishers independently make assertions about the same entity or endpoints.

**REQ-PUB-006 — Contradiction and ambiguity**  
The initial graph SHOULD deliberately include test cases involving disagreement, stale identifiers, ambiguous attribution and other difficult cases rather than containing only clean demonstrations.

**REQ-PUB-007 — Self-assertion**  
The initial graph SHOULD include cases where a publisher makes an assertion involving one of its own identifiers, allowing the resulting graph symmetry to be explored.

**REQ-PUB-008 — Harm minimisation**  
Experimental publication SHOULD avoid unnecessary disclosure, unwanted correlation or amplification of sensitive information. Test data MAY be synthetic where real publication would create disproportionate risk.

**REQ-PUB-009 — Reproducibility**  
Where practical, the initial corpus SHOULD make it possible to distinguish the Village Link assertion itself from evidence, timestamps, indexing data and other experimental metadata.

---

## 3. Requirements for consuming applications

These requirements apply to applications that interpret, select or disclose Village Links. They are deliberately modest: the project should leave room for Trust Engines and Star Credential Managers to adopt different trust, reputation, audience and disclosure policies.

**REQ-APP-001 — Preserve publisher distinction**  
An application MUST NOT silently collapse identical endpoint pairs published by different publishers in a way that destroys information about who made each assertion.

**REQ-APP-002 — Do not present syntax as truth**  
An application MUST NOT imply that a relationship is verified merely because it is expressed as a syntactically valid Village Link.

**REQ-APP-003 — Independent trust models**  
Applications MAY assign different weight to publishers, evidence, memory systems, endpoint types, age of assertions or graph structure.

**REQ-APP-004 — Conflicting assertions**  
Applications SHOULD be capable of encountering conflicting or incompatible assertions without treating the graph itself as invalid.

**REQ-APP-005 — Missing and unavailable endpoints**  
Applications SHOULD tolerate endpoint resources that cannot be dereferenced, have moved, require authentication or no longer exist. URI persistence and resource availability are not equivalent to truth of the underlying assertion.

**REQ-APP-006 — No mandatory Star Credential interpretation**  
An application MUST NOT be required to construct or recognise a Star Credential in order to process an individual Village Link.

**REQ-APP-007 — Safety choices remain application-specific**  
Applications MAY impose stronger privacy, consent, evidence, moderation or lifecycle policies than the core standard requires.

**REQ-APP-008 — Marker-first interpretation by the reference browser**  
The project's reference browser MUST first attempt to parse an HTTPS URI whose first DNS label is `vl` as a Village Link before ordinary web dereferencing. Successful parsing MUST NOT require the marker host to be dereferenceable. If Village Link parsing fails, the browser MUST fall back to ordinary HTTPS handling. Marker recognition MUST NOT be presented as evidence of truth, authority or trust.

---

## 4. Non-requirements

The following are explicitly not current requirements of the Village Link primitive:

- creation of a universal or canonical identity;
- proof that two identifiers refer to the same entity;
- endorsement by either endpoint system;
- membership of an entity in a Village Link system;
- a central registry, resolver or trust authority;
- a universal reputation score;
- a prescribed governance model;
- a prescribed authentication method;
- construction of a Star Credential;
- persistence or dereferenceability of a separate Village Link object; or
- agreement among publishers.

These capabilities may be provided by publishers, applications or later standards without being properties of the core primitive.

---

## 5. Open requirements questions

Draft 0.1 deliberately leaves several requirements unresolved:

1. What minimum evidence is required to attribute publication to P?
2. What lifecycle states, if any, belong in the standard rather than applications or indexes?
3. Does responsible publication require any concept of consent, notice or discoverability control at the standard layer?
4. What requirements follow from URI length, encoding and transport constraints?
5. What distinction should the standard make between a live assertion and a historical observation that the assertion existed?
6. Which harms controls belong in the primitive, which belong in publication practice, and which belong in consuming applications?
7. What conformance classes are useful without making the standard unnecessarily large?

These questions are intended to be challenged through prototype implementation, harms analysis and external review.