# Research 001: Prior art for URI equivalence and link collections

**Date:** 27 August 2026  
**Status:** Initial research note

## Purpose

This note records prior art relevant to two related Village Link architectural ideas:

1. the Village Link primitive: a self-contained, two-ended equivalence link between representations in different contexts; and
2. the Star Credential: a collection of Village Links sharing a common entity.

The purpose is to preserve the design research that informed the architecture, including both similarities to existing standards and the distinctions that currently appear significant.

This is not a patent or legal novelty search. Absence of a precedent from this research should not be interpreted as a claim that no precedent exists.

## Village Link primitive

Conceptually, Village Link asserts:

`(A in X) = (B in Y)`

or, in abbreviated form:

`A ↔ B`

The intended semantics are narrow: the two endpoints are representations of the same entity in different contexts or memory systems.

ADR-002 deliberately restricts Village Link to this equivalence relation rather than introducing an arbitrary operator.

## 1. URIs containing URI or identifier material

There is substantial precedent for constructing URI forms that contain other identifiers, including URI-valued components.

Examples include nested URI proposals and deployed URI schemes such as Magnet URIs, which can contain multiple identifier- or URI-valued parameters.

This establishes that the broad syntactic idea of packaging independently meaningful identifier material within a URI is not itself unusual.

However, these precedents do not necessarily provide the Village Link semantics of two peer endpoints whose referents are asserted to be equivalent.

## 2. `owl:sameAs` and URI equivalence

OWL provides a strong semantic precedent through `owl:sameAs`.

An `owl:sameAs` assertion can state that two URI references refer to the same individual. In simplified form:

`URI-A — owl:sameAs — URI-B`

This is closely related to the semantic problem addressed by Village Link: establishing that identifiers used in different systems have the same referent.

The associated Linked Data literature also discusses **co-reference**: distinct URIs that refer to the same resource or entity.

### Important distinction

`owl:sameAs` has strong formal identity semantics. Care is therefore required when comparing it with Village Link.

Two records or Web resources are not necessarily themselves identical merely because they represent the same underlying entity. For example, a GitHub account record and a Facebook account record concerning the same person remain different records.

Village Link's intended assertion is about the common **referent** of representations in different contexts.

This distinction should be made explicit in the Village Link Specification.

## 3. Linksets

Two related Linkset traditions are relevant.

### RFC 9264 Linkset

RFC 9264 defines a way to publish collections of Web Links as standalone documents.

A Linkset can be self-contained, with link context and target represented using absolute URI references. This provides an important precedent for publishing a collection of links independently of the resources being linked.

The underlying Web Linking model remains directional and relational, conceptually:

`context URI — relation → target URI`

This differs from the deliberately symmetric Village Link equivalence primitive.

### VoID and sameAs linksets

The Semantic Web / Linked Data tradition also uses the term **linkset** for collections of RDF links between datasets. Such collections may contain `owl:sameAs` assertions and may be published independently of the datasets being linked.

This is particularly relevant to the Star Credential.

## 4. Apparent relationship to the Star Credential

A Star Credential consists conceptually of multiple Village Links sharing a common entity:

`E ↔ A`

`E ↔ B`

`E ↔ C`

`E ↔ D`

The individual Village Links are the **rays** of the star. The Star Credential is a published collection of those rays.

This has a strong architectural resemblance to Linkset approaches: an independently publishable collection of links involving URI-identified resources.

A useful current formulation is:

> Village Link defines the ray. Linkset provides prior art for the container.

It remains an open question whether RFC 9264 or another existing Linkset representation could eventually serve directly as a serialization mechanism for Star Credentials, or whether Village Link requires its own container representation.

A Star Credential should therefore not yet be defined as an RFC 9264 Linkset. The relationship warrants further technical investigation.

## 5. The apparent gap

The research so far identifies clear precedent for each of the following:

- URIs containing other URI or identifier material;
- asserting equivalence or co-reference between two URI-identified things;
- publishing collections of links independently of the resources being linked; and
- publishing collections of equivalence links.

What has **not yet been identified** is a clear precedent combining all of the following properties:

1. two independently meaningful endpoint URIs;
2. a fixed assertion that their representations have the same referent;
3. both endpoints encoded into one self-contained URI; and
4. the resulting URI itself functioning as the publishable hyperlink, without requiring dereferencing of a separate assertion resource to discover the endpoints.

Conceptually:

`URI-A + equivalence + URI-B → ONE HYPERLINK`

This currently appears to be the most precise distinction between Village Link and the neighbouring architectures identified in this research.

It should be treated as an **apparent gap in the prior art found so far**, not as a claim of novelty.

## 6. Architectural comparison

| Approach | Basic form | Relevant property |
| --- | --- | --- |
| Conventional hyperlink | `P → A` | Publisher publishes a directional link to one target |
| OWL / RDF | `A — owl:sameAs — B` | Explicit equivalence assertion between identifiers |
| VoID Linkset | collection of RDF links | Independently publishable collection, potentially including `sameAs` links |
| RFC 9264 Linkset | collection of Web Links | Self-contained publication of link relationships |
| Village Link | `A ↔ B` | Two-ended equivalence assertion intended to be the hyperlink itself |
| Star Credential | collection of `E ↔ n` rays | Collection of Village Links sharing a common entity |

## 7. Implications for Village Link documentation

This research suggests several documentation requirements.

The Specification should distinguish carefully between:

- two representations having the same referent; and
- two URI-addressed resources being identical.

Documentation should acknowledge `owl:sameAs` and related Linked Data work so that Village Link is not presented as inventing the general concept of URI co-reference.

Documentation of the Star Credential should acknowledge Linksets as relevant prior art and investigate reuse before introducing a bespoke container format.

The distinctive architectural proposition currently worth investigating further is not simply "two URIs identify the same entity." That proposition has substantial precedent.

It is instead the decision to make the two-ended equivalence assertion itself a **single, self-contained, publishable hyperlink**.

## References for further investigation

- W3C OWL documentation: `owl:sameAs`
- W3C Web Architecture discussions of multiple URIs identifying the same resource
- RFC 9264: Linkset — Media Types and a Link Relation Type for Link Sets
- W3C VoID Vocabulary: linksets
- Linked Data literature concerning co-reference and `sameAs` linksets
- Nested URI proposals and deployed multi-identifier URI schemes such as Magnet URIs

These references should be expanded into precise citations as the research matures.
