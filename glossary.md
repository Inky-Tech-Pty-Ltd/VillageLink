# Village Link Glossary

**Status:** Working draft  
**Last updated:** 14 October 2026

## Purpose

This glossary records current Village Link terminology. The [README](README.md) explains the project; the specification takes precedence wherever it assigns a normative meaning. Historical terms are collected at the end rather than treated as current architecture.

## Terminology principles

- Village Link is agnostic about the technologies and semantics of endpoint memory systems.
- An assertion of equivalence is not established equivalence.
- A trace, and its identity in a memory system, need not be a person or an account.
- Do not mistake an interpretation of existing primitives for an additional primitive.

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

**Definition:** The relation asserted by a Village Link: two traces, considered in their respective memory systems, have the same referent.

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

Village Link endpoints are expressed as independently meaningful trace URIs. Endpoint systems need not share an identifier scheme or implement Village Link.

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

## Publisher

**Definition:** A party or system that makes Village Link assertions available.

The publisher and location of publication are not additional endpoints of the `vl:` primitive. Their identity, reliability and reputation may be assessed elsewhere; publication alone does not establish an assertion's truth.

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

The centre may be called the *hypothesis*. Each link from that centre to a member trace is a *ray*. In the minimal representation, `A` denotes the centre trace URI and `B` the collection of member trace URIs.

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

The current codec uses URIs for its two trace endpoints. Their independent meaning is supplied by the systems that host or interpret them.

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

## Future terminology tooling

If the vocabulary stabilises sufficiently for standards work, terminology tooling such as Spec-Up-T may become useful.
