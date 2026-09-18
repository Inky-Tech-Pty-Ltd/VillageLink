# Village Link

## Elevator pitch

In the Village Link project, we’ve been thinking about all of the trust graphs—digital and analogue.

We have two questions:

**A:** How do they connect?  
**B:** How do the layers add up to governance?

We have a candidate for **A**. 

It might open a path to **B**.

## Sibling project

Village Link and [Information is life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life) emerged from the same body of work and have now speciated into sibling projects. Information is life develops the broader evolutionary thesis; Village Link develops a deliberately small technical primitive. Each can be evaluated independently.

## Memory and trust

A typical first conversation between strangers will contain an exchange of biographical information. 
The conversation might establish that the strangers have contexts in common. It may reveal mutual acquaintances.
A curriculum vitae is a formal example of the same ritual.

Accountability necessarily rests upon the trail of memories that entities have left behind in different contexts.
The constraints that we call _governance_ emerge from the consequences of accountability.

Parties have an incentive to reveal context, and to accept the constraints of governance, in order to reduce transaction costs.

Village Link proposes a small web primitive for making a statement that two independently meaningful identifiers in different memory systems refer to the same entity.

Conceptually, for a webpage, W:

**W states A ↔ B.**

Where:

- **A** is an identifier in one system;
- **B** is an identifier in another system; and
- **W** is the web resource where the statement is found.

A conventional hyperlink says, in effect, **W points to one resource, A**. 

A Village Link extends that pattern, **W points to two resources, A ← W → B**.

The project is exploring what becomes possible when this primitive is available at web scale.

## The primitive

A Village Link is a single, self-contained, two-ended hyperlink containing both endpoint URIs.

For example, a webpage might state that these two identifiers refer to the same entity:

```text
https://github.com/Joe-Rasmussen
https://www.facebook.com/joe.rasmussen.70/
```

Conceptually:

`[wab identifier] [separator] [URI A] [separator] [URI B]`

The architectural decision is recorded in [ADR-001](docs/adr/001-two-ended-uri.md).

The important properties are:

- endpoint systems do not need to implement Village Link;
- the statement can be understood without dereferencing a separate link object;
- the webpage W supplies the web context in which the statement is found rather than being encoded as a third endpoint;
- multiple webpages may contain matching or conflicting statements;
- the _truth_, or perhaps better to say the _weight_ of the statement is an emergent property of the graph.

Like a conventional hyperlink, a Village Link carries information both through its endpoints and from the web resource in which it occurs. Its two-ended form creates graph structures that ordinary directed links do not express directly.

### The existing web

<p align="center">
  <img src="docs/diagrams/rendered/wikipedia%20-%20pagerank.png" alt="Wikipedia PageRank diagram" width="550" />
  <br>
  <em>Taken from Wikipedia: PageRank. A one-headed hyperlink drives a ranking algorithm</em>
</p>

### New primitive, new symmetries

<p align="center">
  <img src="docs/diagrams/rendered/pagerank%20diagram%20adapted.png" alt="Adapted PageRank diagram" width="300" />
  <br>
  <em>Two web resources, E and C, both state the relation E ↔ F. For webpage E, this is a statement <strong>about itself.</strong></em>
</p>

## Why this matters

People, organisations and software agents already exist in many separate **memory systems**: systems capable of retaining traces associated with entities. A memory system may record accounts, memberships, transactions, permissions, observations, endorsements, sanctions or other history. It need not impose rules or exercise authority over the entity it remembers.

Those memory systems are usually disconnected.

Village Link provides a standard way to state connections between them on the web.

A sufficiently rich set of connections can form a graph around an entity. We call this a **Star Credential**: not a new master identity issued by a central authority, but a collection of independently meaningful identities and memory traces that can be traversed together.

This may support applications including:

- multi-path authentication;
- reputation and fraud resistance;
- discovery of third-party referees;
- linking online and offline contexts;
- organisational and agent identity;
- research into governance and AI alignment.

These are possible consequences of the primitive, not requirements of the primitive itself.

## Memory systems and governance

A **memory system** is any system capable of retaining traces associated with entities. Some memory systems also contain norms about how entities should behave. Some record breaches of those norms or sanctions imposed in response. Others contain no norms, breach assessments or sanctions at all.

**Governance** is broader than any one such system. It arises when an entity is exposed, through one or more memory systems, to norms and to possible consequences associated with conformity or breach.

The relevant functions do not need to live in the same place. An action may occur in one system, be assessed against a norm somewhere else, and lead to a sanction recorded or imposed somewhere else again. A person, organisation or software agent may therefore be subject to complex, overlapping layers of governance without belonging to any single "governance system".

Village Link does not itself perform governance. It makes it possible to state connections between memories of the same entity across otherwise separate systems. A sufficiently rich graph may therefore make existing relationships of reputation, accountability and governance more visible and traversable without creating a new central identity authority.

## Current status

Village Link is an early-stage experimental project. The repository currently contains:

- the evolving project argument in this repository;
- an accepted architectural decision for the two-ended hyperlink primitive;
- a [documentation map](documentation.md), roadmap and wishlist;
- diagrams and worked examples;
- prototype work toward creating and browsing Village Links.

The syntax, indexing model, lifecycle rules, browser behaviour, evidence model and provenance model remain under active development.

## Project roles

The work is being separated into four areas that should remain conceptually distinct:

1. **Develop the standard** — define the primitive, syntax, semantics and supporting specifications.
2. **Build and govern an initial graph** — use a MediaWiki to create and test a corpus of Village Link statements.
3. **Interpret the graph** — investigate reader-side discovery, filtering, ranking and trust through the [Trust Engine](trust-engine.md).
4. **Compose artefacts** — provide a small, stateless [Composer](composer.md) for constructing village links and star credentials without taking custody of a user's private identity graph.

In shorthand: **Define → Publish → Interpret → Compose.**

The project previously considered a persistent **Star Credential Manager** for audience-specific identity and credential management. [ADR-007](docs/adr/007-stateless-composer.md) records the decision to separate simple composition from that much higher-risk problem and to leave persistent credential management outside the current architecture.

See [Roadmap](roadmap.md) and [Wishlist](wishlist.md) for the evolving work program.

## Design principles

The project currently favours:

- a minimal primitive;
- no required central authority;
- compatibility with existing identifiers;
- provenance through the web resource W;
- independent and potentially contradictory statements;
- explicit separation between the link primitive and applications built on top of it.

## Contributing

The project is young enough that architecture, terminology and implementation remain open to challenge.

Useful contributions include criticism of the primitive, edge cases, alternative architectures, privacy and abuse analysis, prototype code, test data, and examples from existing identity, reputation, memory and governance systems.

If the underlying statement — **W states A ↔ B** — is useful, the next task is to discover where it breaks.
