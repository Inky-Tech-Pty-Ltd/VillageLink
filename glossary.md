# Village Link Glossary

**Status:** Working draft  
**Last updated:** 29 October 2026

## Purpose

This glossary records Village Link terminology together with vocabulary emerging from [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble) and other candidate applications. The [README](README.md) explains the current working model. Normative requirements belong in the specification and accepted ADRs, not in this glossary.

**Draft discrepancy:** Parts of [specification.md](specification.md) (Draft 0.1, September 2026) still use the older `W states A ↔ B` and `wab.` formulation, whereas the current README and codec use strict referential equality expressed as `vl:[A in X]=[B in Y]` and encoded with the `vl:` scheme. Those documents need reconciliation; this glossary does not silently amend the specification. Historical terms are collected at the end.

## Terminology principles

- Village Link is agnostic about the technologies and semantics of endpoint memory systems.
- The equality asserted by a Village Link is **strict referential equality**, not similarity; an assertion is not established equivalence.
- A trace, and its identity in a memory system, need not be a person or an account.
- Do not mistake an interpretation of existing primitives for an additional primitive.
- Application terminology and experimental hypotheses are not Village Link protocol requirements.

---

## Assertion

**Definition:** A claim made through a Village Link that two traces in their respective memory systems have the same referent.

A published assertion is not necessarily true. Publication, interpretation and assessment are distinct activities. *Statement* may be used in ordinary prose, but *assertion* is the preferred term for the claim made by a Village Link.

---

## Consequence

**Definition:** An outcome arising for an entity through a memory system in which it has left a trace.

Consequences can be favourable, adverse or neutral. Their significance depends on the relevant memory system and its technology.

---

## Constraint

**Definition:** A limit or pressure on an entity's possible behaviour, including that arising from anticipated or actual consequences.

---

## Context

**Definition:** The circumstances in which a trace or expression is understood.

A memory system supplies its own context and semantics. Village Link does not impose a universal contextual hierarchy.

---

## Entity

**Definition:** Something that can leave traces in memory systems and be referred to by memes.

A person, organisation, software agent, animal or other thing may be an entity. Village Link does not prescribe which entities exist, or how they are governed.

---

## Equivalence

**Definition:** The strict equality of referent asserted by a Village Link between two traces, each considered in its own memory system. This is not approximate similarity, common wording or shared subject matter.

Conceptually: `vl:[A in X]=[B in Y]`.

The operator is an *assertion* of equivalence, not a proof of it. A graph may contain false, conflicting or contested assertions.

---

## Governance

**Definition:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace.

This is a **claim under test** in the project, not a property guaranteed by the Village Link primitive.

---

## Hypothesis

**Definition:** The meme proposed as the common referent at the centre of a star credential.

The centre is a meme like any other; *hypothesis* names its role in the star rather than introducing a new primitive or requiring a scientific proposition. A hypothesis might be *Joe Rasmussen*, *Memory is the masterpiece*, or a candidate memory proposed by a Cobbler.

A star credential asserts equivalence between the centre and its rays' endpoint traces. It does not establish that the equivalences are true, or that a proposition expressed by the hypothesis is true.

---

## Identifier

**Definition:** A means of referring to something within the conventions of a memory system.

The current Village Link codec represents its endpoints as independently meaningful trace URIs. Endpoint memory systems need not share an identifier scheme or implement Village Link. Whether a future implementation can work more directly with memory-native addresses remains experimental.

---

## Meme

**Definition:** A referent expressed through traces in memory systems.

In the project's primitive, the trace *in its memory system* is the expression of the meme. A meme is not necessarily an organism, document, identifier or scientific proposition; it may be an idea, entity, event or other referent.

Village Links assert that different traces express the same meme. They do not establish that this is so.

---

## Memory system

**Definition:** A system in which traces of memes are retained.

Its medium and technology are unrestricted: examples include websites, repositories, institutional records, correspondence, and recollections held by people or animals. Village Link does not define the internal semantics, permissions, judgements or consequences of any such system.

---

## Norm

**Definition:** An expectation, rule or standard concerning behaviour within a memory system or community.

Norms and their consequences belong to the relevant memory systems, not to the Village Link primitive.

---

## Provenance

**Definition:** Information about the origin, authorship, publication and subsequent history of a trace, assertion or supporting evidence.

Provenance may help a reader evaluate an assertion, but it is not itself proof of equality or an additional endpoint in the Village Link primitive.

---

## Publisher

**Definition:** A party or system that makes Village Link assertions available.

The publisher and location of publication are not additional endpoints of the `vl:` primitive. Their identity, reliability and reputation may be assessed elsewhere; publication alone does not establish an assertion's truth. Cobble also explores *internal publishers*: distinguish a publisher's proposed assertion inside an application from an externally published Village Link.

---

## Ray

**Definition:** A Village Link connecting the centre of a star credential to one of its member traces.

A ray is an ordinary Village Link, not a distinct link type. Adding a ray extends the set over which the credential asserts that the centre's meme is invariant.

---

## Reputation

**Definition:** An assessment of an entity arising from traces, histories, judgements or other evidence held in memory systems.

Village Link does not calculate reputation. A star credential can expose candidate sources of evidence; a recipient decides what significance to give them.

---

## Star credential

**Definition:** A collection of Village Links sharing a centre and asserting a set of traces over which a meme is invariant.

The centre may be called the *hypothesis*. Each link from that centre to a member trace is a *ray*. In the current illustrative JSON representation, `A` denotes the centre trace URI and `B` the collection of member trace URIs. Concrete normative Star Credential serialization remains open.

```json
{
  "type": "StarCredential",
  "A": "<centre-trace-URI>",
  "B": ["<member-trace-URI>", "<member-trace-URI>"]
}
```

A star credential may be offered for authentication, discovery, memory work or other purposes. It is not a centrally issued identity, nor proof of the equivalence claims it contains. A receiving memory system decides what to make of the evidence.

---

## Trace

**Definition:** An expression of a meme within a memory system.

A trace is understood *in* its memory system, not independently of it. Village Link connects addressable traces without specifying how each system represents, interprets or evaluates them.

*Memory trace* is an acceptable longer expression of the same term.

---

## URI

**Definition:** Uniform Resource Identifier.

The current codec uses URIs for its two trace endpoints. Their independent meaning is supplied by the systems that host or interpret them. A URI is an identifier, not necessarily a network location or a resource that can currently be dereferenced.

---

## Village Link

**Definition:** A two-ended link asserting that traces in two memory systems express the same meme.

The conceptual primitive is:

```text
vl:[A in X]=[B in Y]
```

The current codec serialises the two full trace URIs as:

```text
vl:<percent-encoded-P>!<percent-encoded-Q>
```

Here `P` and `Q` are endpoint trace URIs. The `=` operator is implicit in this encoding. The link neither defines the technologies of X and Y nor establishes the assertion's truth.

---

## Application and experimental terminology

These terms are in current use in the project, particularly in [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble) and the [Exhibits A, B, C, and D discussion](https://github.com/Inky-Tech-Pty-Ltd/VillageLink/discussions/78). They describe candidate services, experiments and hypotheses, **not new Village Link primitives or settled implementation requirements**.

### Arena

**Definition:** A bounded experimental environment in which a corpus of memory is subjected to inputs, interpretation, resource limits and consequences.

An arena makes scarcity measurable. Exhibit B envisages an initial arena containing the historical corpus without pre-arranged adjacency, Village Links or star credentials, followed by fresh inputs and attempts to organise memory. Multiple arenas may use different architectures or budgets. An arena's working-memory limit need not require deletion of its independently preserved source archive.

### Biography and autobiography

**Definition:** Two perspectives on an entity's retained history: a *biography* assembled from traces and accounts of the entity, and an *autobiography* told or maintained from the entity's own perspective.

These are exploratory descriptions of memory organisation, not guarantees of an enduring narrator or the truth of a narrative.

### Cobbler

**Definition:** A proposed Cobble service that selects, mints and maintains addressable traces and may search the corpus, propose Village Links and assemble star credentials.

The Cobbler is application machinery, not the Village Link primitive. Proposing an equivalence does not make it true; publishing one remains a separate, accountable act. Autonomous memory maintenance remains an experimental ambition.

### Composer

**Definition:** A stateless tool that constructs Village Links or star credentials from supplied identifiers without taking custody of a persistent credential store.

Composer is a current Village Link application role, distinct from a publisher, Trust Engine or Cobbler. See [ADR-007](docs/adr/007-stateless-composer.md).

### Corpus

**Definition:** The body of retained traces, source material, histories and associated provenance available to an entity or an experiment.

Distinguish the durable source corpus from any smaller, capacity-limited working representation inside an arena. A corpus may span GitHub, ChatGPT and other memory systems without treating their contents or authorities as interchangeable.

### Diversity dividend

**Definition:** The hypothesised benefit, particularly under changing conditions, of access to varied ideas, relationships and communities rather than relying only on one tightly bounded group.

An Exhibit C hypothesis, not an established outcome of Village Links or a compulsory objective for Cobble.

### Hemisphere

**Definition:** A semi-independent intelligence process that interprets a shared body of experience and may propose competing memories, hypotheses, links or actions.

Hemispheres can work separately or in parallel, argue, recombine findings and preserve unresolved disagreement. The term does not require **two** processes, a particular supplier, country, model family or enduring personality. A Cobble entity could use one, five or more.

### Internal graph, external graph and membrane

**Definition:** In the proposed Trust Engine model, the *internal graph* is the evidence and connections available to the entity; the *external graph* is the relevant adjacent environment; and the *membrane* is the boundary across which opportunities, risks and proposed transactions are assessed.

These are application-level modelling concepts, not properties encoded in a Village Link. The external graph is not presumed to be a complete global directory.

### Salience

**Definition:** An application-level judgement about which information matters for a particular context, entity or decision.

Salience may influence search, attention, retention or a summary supplied to another intelligence service. It is neither a universal importance score nor evidence that a Village Link assertion is true.

### Select → mint → publish

**Definition:** A proposed workflow for turning a particular occurrence within a larger resource into an addressable trace: *select* the occurrence, *mint* its stable identifier and *publish* it for use in assertions.

Selection, identity assignment and publication are separate acts. A minted trace need not make its source content public. See [Cobble Issue #4](https://github.com/Inky-Tech-Pty-Ltd/Cobble/issues/4).

### Self-sovereignty and portability

**Definition:** The proposed ability of an entity seated in its retained body of work to preserve and carry its memory, relationships and identity across intelligence suppliers and hosting environments, with reduced dependence on any one of them.

An aspiration being tested by Cobble, not a property conferred merely by using Village Links.

### Sense

**Definition:** An application-level capability through which an experimental entity can encounter or inspect information in its retained memory or adjacent environment.

A sense may expose source records, their metadata, incoming messages, or observations of the external world. The *sense* is the access mechanism; an *observation* is what it returns; and an *experience* is what the entity actually takes into its ongoing history. Having a source copied into a corpus does not, by itself, mean that the entity has sensed or understood it.

Cobble's initial Arena source catalogue is an **operator diagnostic** over archived file metadata, not yet an autonomously exercised or resource-metered sense of the juvenile learner. Future internal-memory and web-adjacent senses are experimental capabilities whose use must respect source permissions, privacy boundaries and explicit budgets for attention, retrieval, intelligence and external operations. A sense neither proves the truth of what is observed nor creates a Village Link assertion automatically.

### Theory of mind

**Definition:** An entity's revisable model of other entities' perspectives, interests, histories and likely responses, inferred from available traces and interactions.

A proposed Cobble capability for more context-sensitive relationships, not direct access to another mind or a licence to treat inferred motives as facts.

### Transaction cost

**Definition:** The resources and risks incurred in arranging, evaluating, undertaking and enforcing a transaction.

Risk belongs within transaction cost rather than being a separate category that must always be added to it. Village Links and star credentials are candidate technologies for reducing some of these costs.

### Trust Engine

**Definition:** A proposed reader-side service that uses available evidence, published graph assertions and a *problem vector*—the reader's question, opportunity or proposed transaction—to discover and assess relevant objects, paths and potential referees.

The working formulation is `Trust Engine = f(internal graph, external graph, problem vector)`. A Trust Engine interprets and ranks; it does not make an inferred equivalence true or automatically publish new Village Links or star credentials. See [trust-engine.md](trust-engine.md).

### Value function

**Definition:** A criterion used by an experimental entity to choose among competing uses of scarce resources, such as which memories to retain, compress, connect or release, and which actions to prefer.

Exhibit B proposes **social status**—understood in the setting of relationships, reputation and trade—as a candidate value function. Whether it is adaptive, how it would be measured and how it differs from mere popularity or sycophancy are questions for experiments, not assumptions of the primitive.

---

## Reference-browser terminology

**Split screen:** A reference browser view with the two endpoint resources displayed in separate panes. Not part of the primitive.

**Triple bar:** Reference browser chrome showing the Village Link URI and the two independently navigable endpoint addresses. Not part of the primitive.

---

## Deprecated and historical terminology

The entries below explain earlier project documents; they are **not** requirements of the current primitive.

| Earlier usage | Current treatment |
| --- | --- |
| `W states A ↔ B`, `A ← W → B` | Earlier publication-centred formulation. The current primitive asserts equivalence between traces in memory systems; W is not encoded as a third endpoint. |
| `wab.` and `vl.` DNS markers | Earlier schemes or conventions. The current codec uses the `vl:` URI scheme with `!` separating encoded trace URIs. Existing publisher hostnames can retain historical names without changing this. |
| `gc.` global-context naming | Earlier optional endpoint-namespace convention, not part of the current core. |
| `vc.` village-context naming | Earlier optional endpoint-namespace convention, not part of the current core. |
| *Global context* and *village context* | Historical contextual models; no longer assumed by the core primitive. |
| *Governance system* as generic endpoint system | Use *memory system*. |
| *Reputation system* as generic endpoint system | A possible kind of memory system, not the general term. |
| *Identifier equality* or *same entity* as the whole primitive | The current formulation is equivalence of traces' referent, a *meme*; it is not restricted to identity authentication. |
| *Statement* instead of *assertion* | Both are ordinary words; *assertion* is the preferred term for published equivalence claims. |
| *Star Credential Manager* as a core Village Link artefact | Retired in [ADR-007](docs/adr/007-stateless-composer.md): **Composer** constructs credentials without retaining a central private identity graph. A persistent manager would be a separate application and security decision. |

## Future terminology tooling

If the vocabulary stabilises sufficiently for standards work, terminology tooling such as Spec-Up-T may become useful.
