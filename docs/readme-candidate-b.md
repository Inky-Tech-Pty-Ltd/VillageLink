# Village Link

Village Link begins with a question: **What is governance?**

The project explores whether systems that govern humans can tell us anything useful about governing AI. It does not propose a new government, identity provider or reputation platform. It proposes something much smaller: a web primitive for connecting reputational traces that already exist.

## Governance is layered

Human behaviour is constrained by many systems at once: law, workplaces, families, professional communities, clubs, universities, software platforms, groups of friends and marketplaces.

Some constraints are formal: permissions, contracts, laws and technical access controls. Others are informal: expectations, memory, reputation and the possibility of sanction by people whose opinion matters.

No single one of these systems governs a person. Governance emerges from their overlap.

AI agents increasingly participate in the same world of transactions, institutions and scarce resources. If they are to become durable participants in that world, the question is not only what rules can be placed inside an AI system, but what external systems can hold an agent accountable over time.

That requires memory, reputation and connection between contexts.

## The missing primitive

The web has a simple primitive for saying **P points to A**: the hyperlink.

Village Link proposes a similarly small primitive for saying **P asserts A ↔ B**.

In words: the entity identified as A in one context is the same entity identified as B in another context.

A Village Link is therefore a **two-ended hyperlink**. Both endpoint identifiers are carried by the link itself; the publisher is established by the context in which the link is published.

The architectural decision is described in [ADR-001](adr/001-two-ended-uri.md).

The project asks what happens if assertions of this kind become easy to publish, crawl, compare and combine.

## We already do this without computers

When two strangers meet, they often perform a small ceremony:

> What do you do? Where do you live? Where did you go to school? Do you know Sam?

The questions sound like biography. They also perform a practical function.

The two people are searching for contexts they understand in common: workplaces, neighbourhoods, families, institutions, professions and acquaintances. Each answer creates possible connections to other people and systems capable of corroborating a claim.

A stranger becomes less strange.

The parties are assembling a small reputational graph and discovering potential third-party referees. That graph can reduce the uncertainty surrounding whatever they might want to do next: share information, extend trust, enter a transaction, offer access, make an introduction or collaborate.

The same pattern appears in more formal ceremonies. A curriculum vitae lists institutions and roles that can be checked. A speaker introduction locates an unfamiliar person inside institutions and achievements the audience may already recognise.

Human beings have been constructing these graphs for a very long time. We have simply lacked a general digital primitive for expressing their edges.

## The Star Credential

A collection of Village Links around an entity forms what this project calls a **Star Credential**.

<p align="center">
  <img src="diagrams/rendered/Multiple%20Memberships%20Joe%20v2.png" alt="A Star Credential linking one entity across multiple contexts" width="450" />
</p>

A Star Credential is not a master identity issued by Village Link. Its spokes point outward to identities and reputational traces maintained by independent systems. Those systems retain their own rules, evidence and authority. The credential gains strength from plurality rather than centralisation.

When two Star Credentials meet, their graphs may reveal systems, institutions or referees they have in common. Those paths can provide multiple independent ways to establish identity, reputation or trust.

The idea applies not only to people. The endpoints of a Village Link can identify organisations, services, devices, datasets or AI agents.

## Why AI matters

An AI agent that participates in consequential transactions needs more than an identifier. Other participants need ways to ask where it has acted before, which systems recognise it, who is willing to make claims about it, what reputational consequences can follow from its behaviour, and whether independent paths exist by which its claims can be checked.

Village Link does not answer those questions. It proposes infrastructure through which answers held by different systems can be connected.

The broader hypothesis is that accountable AI may depend partly on the same thing accountable human behaviour depends on: participation in multiple systems with memory, rules, reputation and consequences.

## One primitive, many possible consequences

The primitive is intentionally smaller than the ambitions that motivate it.

A standard way to publish **P asserts A ↔ B** could support experiments in multi-path authentication, reputation and fraud resistance, third-party verification, linking online and offline identities, portable organisational and agent reputation, discovery of overlapping governance systems, and AI accountability.

Village Link should not prescribe these applications prematurely. The immediate task is to determine whether the primitive itself is coherent, implementable and useful.

## Three project roles

The project currently separates its work into three roles:

1. **Develop the standard** — specify the Village Link primitive and the conventions required for interoperable publication.
2. **Publish an initial graph** — create enough real and test assertions to learn how the primitive behaves outside examples.
3. **Explore applications** — investigate commercial, public-interest and research opportunities that emerge if the graph becomes useful.

These roles have different objectives and constraints. Keeping them separate is part of the project design.

See the [Roadmap](../Roadmap.md), [Wishlist](../Wishlist.md), and [ADR-001](adr/001-two-ended-uri.md) for current work and architectural decisions.

## What happens next

Village Link is at the prototype and specification stage. The near-term work is to tighten the specification, build a small corpus of links, publish and browse them with working software, and expose the idea to criticism.

The project particularly welcomes challenges around privacy, abuse, evidence, lifecycle, conflicting assertions, publisher reputation, URI design and the consequences of linking reputational systems that are currently separate.

The proposition is deliberately simple:

**P asserts A ↔ B.**

If that is a useful thing for the web to be able to say, we should find out what follows.
