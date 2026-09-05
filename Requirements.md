# Village Link Requirements

**Status:** Draft 0.1  
**Date:** 6 September 2026

## Purpose

This document states the current requirements for the Village Link project.

Village Link is being developed through four conceptually distinct areas:

1. **Develop the standard** — define the primitive, syntax, semantics and conformance rules.
2. **Publish and govern an initial graph** — publish a corpus of Village Link statements to test the standard and establish useful data.
3. **Interpret the graph** — investigate reader-side discovery, filtering, ranking and trust through Trust Engines.
4. **Manage disclosure** — investigate how entities or publishers present audience-specific subsets of Star Credentials.

The requirements below are grouped into the standard, the reference publisher and consuming applications. Terms are used as defined in [Glossary.md](Glossary.md).

Normative keywords **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** indicate the intended strength of requirements.

---

## 1. Requirements for the standard

### Core primitive

**REQ-STD-001 — Two independently meaningful endpoints**  
A Village Link MUST connect two identifiers that are independently meaningful outside the Village Link itself.

**REQ-STD-002 — Same-entity statement**  
A Village Link MUST state that its two endpoint identifiers refer to the same entity.

Conceptually: **W states A ↔ B.**

**REQ-STD-003 — Self-contained statement**  
The two endpoint identifiers MUST be recoverable from the Village Link itself without requiring dereferencing of a separate Village Link resource.

**REQ-STD-004 — URI endpoints**  
The standard MUST support URIs as endpoint identifiers.

**REQ-STD-005 — Endpoint independence**  
An endpoint system MUST NOT be required to implement, recognise or cooperate with Village Link merely because one of its identifiers appears as an endpoint.

**REQ-STD-006 — Symmetry**  
The semantic relation connecting A and B MUST NOT imply that one endpoint is intrinsically the source, subject, authority or subordinate of the other.

### Publication and truth

**REQ-STD-007 — Web resource**  
A Village Link MUST be interpretable in relation to a web resource W on which the statement is found. W is not represented as a third endpoint in the core link.

**REQ-STD-008 — Statement, not adjudication**  
The standard MUST NOT treat publication of a Village Link as proof that the stated relationship is true, current or authoritative.

**REQ-STD-009 — Independent publication**  
The standard MUST permit multiple web resources independently to state the same endpoint relation.

**REQ-STD-010 — Disagreement permitted**  
The standard MUST permit a wider graph to contain statements that are matching, overlapping, ambiguous or in conflict. Village Link itself MUST NOT require a central mechanism to adjudicate among them.

### Minimality, prefixes and decentralisation

**REQ-STD-011 — Minimal primitive**  
The core standard SHOULD impose no requirement that is necessary only for a particular application, business model, reputation model or governance model.

**REQ-STD-012 — No required central identity authority**  
The standard MUST NOT require a central authority to establish a canonical identity for an entity.

**REQ-STD-013 — Adopted HTTPS prefix conventions**  
The project adopts three conventional DNS prefixes:

- `wab.` — marker for the two-ended Village Link form;
- `gc.` — global-context endpoint naming; and
- `vc.` — village-context endpoint naming.

These are conventions within ordinary HTTPS/DNS naming, not new URI schemes and not authorities whose use requires registration with `village.link`.

The `wab.` prefix is deliberately independent of Village Link branding and provides a mnemonic for the primitive **A ← W → B**.

**REQ-STD-014 — Decentralised marker authority**  
Publication and interpretation of a Village Link MUST NOT depend on registration in a single central Village Link database or service. `wab.village.link` MUST NOT be treated as the sole permitted marker authority: domain owners MUST be able to operate conforming `wab.` HTTPS marker namespaces beneath domains they control without registering with or obtaining permission from `village.link`.

**REQ-STD-015 — Existing identifiers**  
The standard SHOULD permit existing identifiers to participate without modification wherever technically practical. `gc.` and `vc.` are available naming conventions where a suitable endpoint URI does not already exist.

### Lifecycle, safety and interpretation

**REQ-STD-016 — Lifecycle representability**  
The standard MUST allow implementations to reason about the continuing status of a statement where an endpoint or relevant web resource changes state.

**REQ-STD-017 — Publication context**  
The standard MUST preserve enough publication context for an observer to identify W and assess available provenance evidence separately from the primitive statement.

**REQ-STD-018 — Copying and quotation**  
The standard MUST address the distinction between a statement found on W and reproducing, quoting, indexing, caching or archiving that statement elsewhere.

**REQ-STD-019 — No inherited trust**  
The standard MUST NOT require an observer to trust a statement merely because it conforms to Village Link syntax.

**REQ-STD-020 — Harms remain assessable**  
The standard SHOULD preserve sufficient information for downstream systems and researchers to assess privacy, abuse, impersonation, unwanted correlation and other harms created or amplified by published links.

### Extensibility

**REQ-STD-021 — Application independence**  
The standard MUST permit applications to derive additional structures — including Star Credentials, reputation models, authentication paths and governance relationships — without making those structures part of the core Village Link statement.

**REQ-STD-022 — Entity neutrality**  
The standard MUST NOT assume that the entity referred to by the endpoints is a human.

---

## 2. Requirements for publishing an initial graph

These requirements apply to the project's experimental publishing role. They are not automatically requirements of every conforming publisher.

**REQ-PUB-001 — Standards-conforming corpus**  
The initial graph SHOULD use the current Village Link specification except where an experiment deliberately tests a proposed change or known edge case.

**REQ-PUB-002 — Publication visibility**  
The publication mechanism MUST make W and relevant publication context sufficiently clear to test provenance and attribution questions.

**REQ-PUB-003 — Evidence retention**  
For experimental and research purposes, the initial corpus SHOULD retain evidence supporting each statement where such evidence can lawfully and responsibly be retained.

**REQ-PUB-004 — Observation time**  
The corpus SHOULD record when a statement or its supporting evidence was observed, sampled or published.

**REQ-PUB-005 — Multiple web resources**  
The initial graph SHOULD include examples in which multiple web resources independently state the same endpoint relation.

**REQ-PUB-006 — Contradiction and ambiguity**  
The initial graph SHOULD deliberately include difficult cases rather than containing only clean demonstrations.

**REQ-PUB-007 — Structural symmetry**  
The initial graph SHOULD include cases useful for exploring **A ← W → B** and larger graph symmetries.

**REQ-PUB-008 — Harm minimisation**  
Experimental publication SHOULD avoid unnecessary disclosure, unwanted correlation or amplification of sensitive information. Test data MAY be synthetic where real publication would create disproportionate risk.

**REQ-PUB-009 — Reproducibility**  
Where practical, the initial corpus SHOULD distinguish the Village Link statement itself from evidence, timestamps, indexing data and other experimental metadata.

---

## 3. Requirements for consuming applications

**REQ-APP-001 — Preserve web-resource distinction**  
An application MUST NOT silently collapse identical endpoint pairs found on different web resources in a way that destroys relevant provenance information.

**REQ-APP-002 — Do not present syntax as truth**  
An application MUST NOT imply that a relationship is verified merely because it is expressed as a syntactically valid Village Link.

**REQ-APP-003 — Independent trust models**  
Applications MAY assign different weight to web resources, publishers, evidence, memory systems, endpoint types, age of statements or graph structure.

**REQ-APP-004 — Conflicting statements**  
Applications SHOULD be capable of encountering conflicting or incompatible statements without treating the graph itself as invalid.

**REQ-APP-005 — Missing and unavailable endpoints**  
Applications SHOULD tolerate endpoint resources that cannot be dereferenced, have moved, require authentication or no longer exist.

**REQ-APP-006 — No mandatory Star Credential interpretation**  
An application MUST NOT be required to construct or recognise a Star Credential in order to process an individual Village Link.

**REQ-APP-007 — Safety choices remain application-specific**  
Applications MAY impose stronger privacy, consent, evidence, moderation or lifecycle policies than the core standard requires.

**REQ-APP-008 — Marker-first interpretation by the reference browser**  
The project's reference browser MUST first attempt to parse an HTTPS URI whose first DNS label is `wab` as a Village Link before ordinary web dereferencing. Successful parsing MUST NOT require the marker host to be dereferenceable. If Village Link parsing fails, the browser MUST fall back to ordinary HTTPS handling. Marker recognition MUST NOT be presented as evidence of truth, authority or trust.

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

Draft 0.1 deliberately leaves several requirements unresolved, including lifecycle mechanisms, responsible-publication controls, URI encoding and transport constraints, historical observations, harms controls and useful conformance classes.

These questions are intended to be challenged through prototype implementation, harms analysis and external review.