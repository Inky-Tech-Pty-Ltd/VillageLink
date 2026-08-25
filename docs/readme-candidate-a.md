# Village Link

Village Link proposes a small web primitive for publishing assertions that two independently meaningful identifiers refer to the same entity in different contexts.

Conceptually:

**P asserts A ↔ B.**

Where:

- **A** is an identifier in one system;
- **B** is an identifier in another system; and
- **P** is the publisher making the assertion.

A conventional hyperlink says, in effect, **P points to A**. A Village Link extends that pattern: **P connects A and B**.

The project is exploring what becomes possible when these assertions can be published, discovered, compared and combined at web scale.

## The primitive

A Village Link is a single, self-contained, two-ended hyperlink containing both endpoint URIs.

For example, a publisher might assert that these two identifiers refer to the same entity:

```text
https://github.com/Joe-Rasmussen
https://www.facebook.com/joe.rasmussen.70/
```

The architectural decision is recorded in [ADR-001](adr/001-two-ended-uri.md).

The important properties are:

- endpoint systems do not need to implement Village Link;
- the assertion can be understood without dereferencing a separate link object;
- the publisher is identified by publication context rather than encoded as a third endpoint;
- multiple publishers may make matching or conflicting assertions;
- Village Link itself does not decide which assertions are true.

## Why this matters

People, organisations and software agents already exist in many separate systems. Each system accumulates a partial history: accounts, memberships, transactions, permissions, sanctions, endorsements and other reputational traces.

Those systems are usually disconnected.

Village Link provides a standard way to publish connections between them.

A sufficiently rich set of connections can form a graph around an entity. We call this a **Star Credential**: not a new master identity issued by a central authority, but a collection of independently meaningful identities and reputational traces that can be traversed together.

This may support applications including:

- multi-path authentication;
- reputation and fraud resistance;
- discovery of third-party referees;
- linking online and offline contexts;
- organisational and agent identity;
- research into governance and AI alignment.

These are possible consequences of the primitive, not requirements of the primitive itself.

## Governance

Village Link uses **governance** in a broad sense: systems of rules, norms, permissions, constraints and sanctions that shape behaviour.

A person can simultaneously participate in many such systems: family, workplace, professional communities, software platforms, clubs, legal jurisdictions and informal social groups. Organisations and AI agents can also be subject to overlapping systems of constraint.

The project asks whether making relationships between these systems explicit can improve accountability and make reputational information more portable without creating a new central identity authority.

## Current status

Village Link is an early-stage experimental project. The repository currently contains:

- the evolving project argument in this repository;
- an accepted architectural decision for the two-ended hyperlink primitive;
- roadmap and wishlist documents;
- diagrams and worked examples;
- prototype work toward publishing and browsing Village Links.

The syntax, indexing model, lifecycle rules, browser behaviour, evidence model and publisher-reputation model remain under active development.

## Project roles

The work is being separated into three roles that should remain conceptually distinct:

1. **Develop the standard** — define the primitive, syntax, semantics and supporting specifications.
2. **Publish an initial graph** — create and test a corpus of Village Link assertions to establish useful data and expose practical problems.
3. **Explore applications** — investigate products, services and institutions that might become possible if the standard and graph prove useful.

See [Roadmap](../Roadmap.md) and [Wishlist](../Wishlist.md) for the evolving work program.

## Design principles

The project currently favours:

- a minimal primitive;
- no required central authority;
- compatibility with existing identifiers;
- publisher accountability;
- independent and potentially contradictory assertions;
- explicit separation between the link primitive and applications built on top of it.

## Contributing

The project is young enough that architecture, terminology and implementation remain open to challenge.

Useful contributions include criticism of the primitive, edge cases, alternative architectures, privacy and abuse analysis, prototype code, test data, and examples from existing identity, reputation and governance systems.

If the underlying assertion — **P asserts A ↔ B** — is useful, the next task is to discover where it breaks.
