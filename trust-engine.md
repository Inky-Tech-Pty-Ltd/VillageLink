# Trust Engine

## Status

Concept document.

The Trust Engine is one of the principal Village Link concepts. It describes a possible reader-side application of the Village Link graph. This document defines the problem and the emerging design direction; it is not yet a technical specification.

## The idea

A Village Link publisher creates a graph of assertions of the form:

> **P asserts A ↔ B**

Once enough Village Links exist, a different problem appears:

> **Given a graph of Village Links, what can a reader compute that cannot be computed — or cannot be computed in the same way — from the conventional Web?**

The working name for the machine that answers this question is the **Trust Engine**.

The name is intended to evoke a **search engine**, while deliberately describing a broader problem.

## A reader-side technology

The Trust Engine is principally a reader-side technology.

It does not decide what Village Links exist. Publishers do that.

It consumes a graph produced by many publishers and helps a reader decide what to discover, include, exclude, rank, compare, investigate or trust.

In its shortest form:

> **Trust Engine: What should I discover from the graph?**

This is distinct from **Composer**, which merely constructs village links or star credentials from inputs supplied by a user and need not discover, rank, publish or retain anything.

## Opening the reader's own memory

A URI in a Village Link is an identifier, not necessarily a destination.

For example, `mailto:alice@example.com` conventionally invites an application to compose an email to Alice. A Village Link-aware application may instead use the address as a key for querying one or more email memory systems authorised by the reader.

The address does not itself identify or select the memory system. Bob's client determines which of Bob's mailboxes may be searched and what Bob is authorised to see.

The result is therefore reader-relative. When Bob follows Alice's email identifier, he may not be opening a public resource belonging to Alice. He may be opening **his own memory of Alice**.

The same principle may apply to `tel:` identifiers and authorised call, message or contact histories.

## The existing territory

On the conventional Web, several classes of system perform pieces of this work.

### Search engines

Search engines help a reader find information in a very large collection of published material. They rank results according to relevance, authority and many other signals.

### Filters and firewalls

Filters and firewalls determine what information, entities or interactions should be admitted, excluded or treated with caution.

### Marketplaces

Marketplaces help participants discover and evaluate other participants. They commonly incorporate identity, reputation, reviews, transaction history and rules particular to the marketplace.

These systems solve different problems, but all are concerned in some way with selecting useful or trustworthy possibilities from a much larger universe.

The Trust Engine is intended to explore the territory across these categories rather than reproduce any one of them.

## Why Village Link changes the problem

The conventional Web is built primarily from directed links between resources.

Village Link introduces a different primitive: a publisher makes an assertion connecting two representations of an entity across contexts.

The graph therefore contains explicit information about sameness, correspondence and context. Its symmetries are different from those of the conventional Web.

That difference may change the optimisation problem.

For example, a reader may be able to reason across multiple independent memory systems without requiring any one of those systems to become the canonical identity provider, reputation service or marketplace.

A useful reputation signal may emerge from the shape of the graph itself: which contexts connect, who publishes the connections, which assertions agree, which conflict, and what paths exist between independently governed systems.

Exactly which computations prove useful is an open research and design question.

## Trust is contextual

The working title should not be taken to imply that the Trust Engine computes a universal trust score.

Trust is ordinarily trust **for something**, in some context, from some point of view.

A reader looking for a plumber, a research paper, an employee, a software package, a seller, an AI agent or a source of political information may legitimately apply different criteria to the same graph.

Village Link should preserve that plurality rather than collapse it into a single authoritative ranking.

## Relationship to the Village Link roles

The project currently distinguishes four principal areas of work:

1. **Developer of the Standard** — defines the Village Link primitive.
2. **Publisher** — publishes Village Links and thereby helps establish the graph.
3. **Browser + Trust Engine** — reads and interprets the graph for a user.
4. **Composer** — constructs village links and star credentials without becoming their persistent custodian.

These can be summarised as:

> **Define → Publish → Interpret → Compose**

The Trust Engine occupies the third position: interpretation.

The previously proposed Star Credential Manager is not a current project area; [ADR-007](docs/adr/007-stateless-composer.md) records the decision to separate stateless composition from persistent credential management.

## Architectural restraint

The Trust Engine must not be allowed to enlarge the Village Link standard merely because a useful application would benefit from additional machinery.

A central architectural objective of Village Link is to keep the underlying primitive small and general.

The Trust Engine should therefore be treated as software operating **over** the graph, not as functionality that must be encoded **into** every Village Link.

Different Trust Engines should be possible.

They may use different algorithms, policies, economic models and definitions of relevance or trust while operating over the same underlying graph.

That plurality is a feature.

## Open questions

Important unresolved questions include:

- Which graph properties produce useful trust or discovery signals?
- How should the identity and reputation of publishers affect interpretation of their assertions?
- How should agreement, contradiction and uncertainty be represented to a reader?
- What useful computations arise specifically from the symmetry of Village Links?
- How much can be inferred without centralising identity or reputation?
- How should a Trust Engine expose its ranking or filtering rules?
- What adversarial behaviours emerge once Trust Engines have economic value?
- Where do search, filtering, firewall and marketplace functions genuinely converge, and where should they remain separate?

## Working hypothesis

The Trust Engine is not presently a promised product or a settled architecture.

It is a hypothesis:

> **A sufficiently rich graph of Village Links will support useful reader-side computations that differ materially from those available on the conventional Web.**

The next task is to discover what those computations are.
