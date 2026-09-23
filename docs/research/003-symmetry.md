# Research 003: Symmetry

## Status

Exploratory research note recording the equivalence-typed baseline from which the project began. The candidate symmetries, invariants and mathematical analogies below are provisional. This document does not amend the specification, settle the primitive's semantics, or claim that Village Link has already established a novel mathematical structure. Issue #55 and its feature branch separately explore a strictly untyped primitive in which equivalence is one possible graph-discovered interpretation rather than a meaning built into `↔`.

## Purpose

Village Link introduces a small same-entity assertion:

> **W states A ↔ B.**

The endpoints remain independently meaningful identifiers in their native memory systems. Neither endpoint becomes the canonical form of the other, and W remains the provenance-bearing resource on which the assertion occurs.

This note asks:

> **What useful properties become possible when identity relations between independent memory systems are represented without privileging one representation, one hierarchy or one canonical source?**

The method is **symmetry hunting**: propose a transformation, identify what appears unchanged, then look for useful consequences and destructive counterexamples.

The note is intended as a specimen tray, not a catalogue of conclusions. Its first external question is deliberately simple:

> **What kind of mathematical object have we accidentally built?**

## Working distinctions

A mathematical symmetry is a transformation that preserves some relevant structure. The word is used cautiously here. Some specimens may prove to be genuine symmetries, some only useful invariances, and some misleading resemblances.

Three layers must remain distinct:

1. **Relation:** A and B are asserted to refer to the same entity.
2. **Representation:** A and B are encoded in an ordered serialization and may be displayed differently.
3. **Provenance:** W is the resource responsible for making the assertion.

Thus:

- **A ↔ B is symmetric at the semantic level;**
- **the encoded order A,B is preserved;** and
- **W states is asymmetric.**

Removing either endpoint order or provenance merely to obtain a tidier mathematical object would discard information the architecture intentionally retains.

## Specimen 1: Endpoint exchange

Given:

**W states A ↔ B.**

exchange the endpoints:

**W states B ↔ A.**

### Candidate invariant

The same-entity claim is unchanged. Endpoint position does not confer greater truth, authority or canonical status.

### Possible consequence

Applications can traverse the assertion from either endpoint and can reason across memory systems without choosing one as the master namespace. This may be useful where either representation can be the reader's point of entry: changed names, pseudonyms, migrated accounts, renamed organisations and cross-platform software identities.

### Counterexample or limit

The serialized forms are not identical. Order may control presentation, navigation or a user's immediate context—for example, which endpoint opens in the left pane. Exchanging A and B therefore preserves the semantic relation but not every property of an interface event or encoded artefact.

### Domain to test

Browser behaviour, identity portability and entity resolution.

## Specimen 2: Independent native hierarchies

Suppose A and B are complete native addresses in different memory systems. Their internal paths may organise the world differently:

`A = a₀/a₁/…/aₘ`

`B = b₀/b₁/…/bₙ`

No correspondence between the path segments is required.

### Candidate invariant

The Village Link relation depends on the two complete endpoint identifiers, not on the systems sharing a hierarchy, schema, vocabulary or path length.

### Possible consequence

A memory system can reorganise or model its own context without forcing another system into the same ontology. Village Link may connect municipal, familial, professional, geographic, institutional or platform-specific descriptions while preserving their local structure.

This may be a particularly important symmetry between memory systems: each is permitted to remain native.

### Counterexample or limit

If an endpoint URI changes, the old and new identifiers are not interchangeable merely because they occupy analogous positions in a hierarchy. Redirects, aliases, transferred identifiers and recycled account names create lifecycle and security problems. Independence of hierarchy does not imply immunity to identifier change.

### Domain to test

Local-government records, academic identity, organisational restructures, renamed entities and context-dependent identifiers.

## Specimen 3: Multiplicity without collapse

Suppose the graph contains:

**W₁ states A ↔ B.**

**W₂ states B ↔ C.**

The relation tempts us to infer:

**A ↔ C.**

But the two published assertions remain separate events with separate provenance.

### Candidate invariant

A reasoning system may explore an equivalence-like closure over endpoints while preserving the original assertion nodes, publishers and paths that support each proposed connection.

### Possible consequence

Village Link may support an **equivalence relation with memory**: sameness can be considered across a graph without quotienting all representations into one canonical record. Competing paths, corroboration and disagreement remain inspectable.

This phrase is only a prompt for mathematical classification. It is not yet a formal definition.

### Counterexample or limit

Transitivity is unsafe when either assertion is false, stale, ambiguous, scoped differently or refers to a transferred identifier. A Trust Engine must not silently publish A ↔ C merely because it used the path internally. It should expose the path and uncertainty rather than collapse the endpoints into truth.

### Domain to test

Trust Engine inference, disputed identity, fraud resistance, historical identity and provenance-sensitive knowledge graphs.

## Specimen 4: Assertion symmetry and provenance asymmetry

Hold the endpoint pair fixed and change the publishing resource:

**W₁ states A ↔ B.**

**W₂ states A ↔ B.**

### Candidate invariant

The semantic endpoint pair is the same unordered pair `{A, B}`.

### Possible consequence

Agreement can accumulate without erasing who agreed. Multiple independent publishers may corroborate a claim; copied, coordinated or dependent publications may contribute much less. A reader-side system can compare the same proposition across different memories.

### Counterexample or limit

Substituting W is not a symmetry of the full assertion. W may change authority, responsibility, time, evidence and trust. Ten copied statements are not necessarily ten independent observations. Treating publisher exchange as harmless would destroy precisely the provenance that makes the graph useful.

### Domain to test

Corroboration, misinformation, publisher reputation, citation networks and Sybil resistance.

## Specimen 5: Permutation of star-credential spokes

Represent a star credential as a distinguished centre A with an unordered collection of spokes:

`H = [A][B₁][B₂]…[Bₙ]`

Permute the Bs:

`[A][B₁][B₂][B₃] ~ [A][B₃][B₁][B₂]`

### Candidate invariant

If the Star Credential data model treats the spokes as unordered, their permutation does not change the credential's asserted relationships.

### Possible consequence

Canonicalisation, comparison and deduplication can ignore incidental spoke order. More interestingly, a Trust Engine can ask which properties depend on the membership of the set rather than its presentation: diversity of memory systems, independent paths, resilience to one missing system and routes to potential referees.

### Counterexample or limit

Permutation is not substitution. Replacing a spoke, duplicating one, omitting one, changing its publisher or changing its evidence may alter the credential materially. Interfaces may also impose an order for explanation without making that order part of the credential's semantics.

### Domain to test

Credential serialization, selective disclosure, authentication, referee discovery and resilient recovery.

## Specimen 6: Structural relabelling

Consider two subgraphs whose identifiers and publishers differ but whose typed relationships and provenance pattern have the same shape.

### Candidate invariant

Some graph-level properties may survive a consistent relabelling of nodes: number of independent paths, cut vertices, cycles, publisher concentration, spoke diversity or vulnerability to removal of one memory system.

### Possible consequence

A Trust Engine may discover reusable structural signals without assuming that every identity domain shares the same content. Synthetic G0/G1 experiments could test whether these invariants predict robustness, ambiguity or attack susceptibility.

### Counterexample or limit

Graph isomorphism does not imply equal trust. The identities and histories of particular publishers and memory systems matter. A perfectly matching malicious graph may be constructed deliberately. Structure must be evaluated alongside provenance, time, evidence and reader purpose.

### Domain to test

G0/G1 simulation, adversarial graph construction, ranking and anomaly detection.

## Transformations worth attacking

The specimens above suggest a more systematic test programme. For each Village Link, star credential or graph fragment, vary one feature at a time:

- exchange A and B;
- reverse encoded order while preserving the relation;
- rename identifiers consistently;
- move an endpoint into a different internal hierarchy;
- replace, duplicate or remove W;
- add a second independent publisher;
- compose a path through B;
- permute, duplicate, omit or substitute star spokes;
- split one memory system into two;
- merge two nominally separate memory systems;
- transfer or recycle an identifier;
- introduce a stale, false or malicious assertion; and
- remove one node, publisher or entire context.

For each transformation ask:

1. What remains unchanged?
2. What only appears unchanged because information was discarded?
3. What can a reader now compute?
4. Which attack exploits the proposed invariance?
5. Does the result belong in the primitive, a publisher, a Trust Engine or an application?

## Candidate mathematical neighbours

The project should seek classification before invention. Possible neighbouring bodies of work include:

- equivalence relations and quotient constructions;
- labelled multigraphs and hypergraphs;
- graph automorphisms and invariants;
- provenance semirings and annotated relations;
- group actions on representations;
- category-theoretic treatments of identity, spans or correspondences;
- entity resolution and record linkage;
- belief revision, paraconsistent reasoning and truth-maintenance systems; and
- distributed systems that preserve conflicting or independently sourced assertions.

These are search directions, not claims that Village Link is an instance of any one of them.

## Questions for mathematical review

A mathematically informed reviewer could help most by attacking these questions:

1. What is the smallest formal object that preserves endpoint symmetry, encoded order and asymmetric provenance?
2. Is “an equivalence relation with memory” coherent, already named, or misleading?
3. Which transformations above are genuine symmetries, and which are only implementation invariances?
4. What useful invariants can be computed without collapsing independently meaningful representations?
5. How should time, contradiction and scoped identity alter any equivalence-like closure?
6. Does a star credential add mathematical structure beyond a set of provenance-bearing pairwise assertions?
7. Which established machinery would let us state the problem more simply—and which machinery would smuggle in assumptions Village Link rejects?

A negative result is valuable. If these properties are routine, trivial or already well understood, the project should learn that early and use the existing language.

## Research programme

The near-term programme is:

1. refine the specimens against the specification and adversarial examples;
2. ask a mathematically formidable software practitioner to classify the object without first steering them toward a preferred branch of mathematics;
3. encode the transformations in the G0/G1 experimental model;
4. test candidate invariants under false, stale, transferred and coordinated assertions; and
5. promote only durable findings into the Trust Engine design, requirements or specification through their normal decision processes.

The central discipline is to preserve the primitive's restraint:

> **Find the consequences of the symmetry before adding machinery to the standard.**
