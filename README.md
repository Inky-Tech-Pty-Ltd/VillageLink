# Village Link

Village Link is an experiment in connecting names across memory systems.

A candidate Village Link looks like this:

```text
vl:[X]in[A]=[Y]in[B]
```

Read it literally:

> the thing called `X` in memory system `A` is the same thing as the thing called `Y` in memory system `B`

That is the primitive.

Everything else in this project should be judged by whether it needs to be in that statement, or can be built above it.

## Why this exists

The same entity is named differently in different systems.

For example, one system might know a person as:

```text
Joe-Rasmussen
```

while another knows the same person by a different local name.

Those systems do not need to share a global identifier, naming authority, database, ontology, or implementation.

Village Link proposes a small way to state the equality directly:

```text
vl:[Joe-Rasmussen]in[GitHub]=[some-other-name]in[another-memory-system]
```

The names are local. The equality is the link.

## Memory systems

A **memory system** is any system capable of retaining traces associated with entities.

It may be online or offline. It may be a website, database, register, organisation, family, institution, community, device, archive, or something else entirely.

Village Link does not require memory systems to use the same technology.

It also does not require Village Link to understand how a memory system works internally.

A memory system only needs some way for an endpoint to be identified well enough for a link to refer to it.

## Local names are not URLs

A useful distinction is:

```text
local name
memory system
resource address
```

These are not necessarily the same thing.

On GitHub, for example:

```text
local name:       Joe-Rasmussen
memory system:    GitHub
resource address: https://github.com/Joe-Rasmussen
```

A URL may be a convenient identifier for a trace or a memory system, but Village Link should not assume that every memory system is on the web, or that every local name is a URL.

The square-bracketed items in the candidate notation are therefore conceptual identifiers, not necessarily web addresses.

## Same-context links

The same primitive also works inside one memory system:

```text
vl:[X]in[A]=[Y]in[A]
```

That is a synonym or alias assertion.

No separate synonym mechanism is required.

## Across systems

When the contexts differ:

```text
vl:[X]in[A]=[Y]in[B]
```

the link connects two local traces across memory systems.

This gives a simple form of disambiguation.

There may be several people called `Joe Rasmussen` in one context, but only one of them may connect to `Joe-Rasmussen` in GitHub. Additional links can make the intended entity progressively clearer without requiring a single global name.

## A link is not a publisher

Earlier Village Link designs encoded or implied a publishing domain as part of the link.

That made it easy to confuse two different things:

1. the equality being asserted; and
2. the system or resource that publishes an assertion about that equality.

The current candidate separates them.

The Village Link is:

```text
vl:[X]in[A]=[Y]in[B]
```

A publisher may publish that link, comment on it, index it, reject it, contradict it, or attach evidence to it.

The publisher is not necessarily part of the identity of the link.

This is closer to the role of a conventional hyperlink: the edge does not need a separate web resource whose purpose is to describe the edge.

## URI scheme

The project is exploring `vl:` as a dedicated URI scheme.

Conceptually:

```text
vl:<encoded village link>
```

The human-readable form and the machine representation do not need to be identical.

A browser or library might render:

```text
Joe-Rasmussen in GitHub = Joe in Family
```

while carrying a canonical encoded form underneath.

The encoding is still experimental.

## Memes

A Village Link is one equality edge.

A larger object can emerge from many such edges.

For example:

```text
[X]in[A] = [Y]in[B]
[Y]in[B] = [Z]in[C]
[Z]in[C] = [Q]in[D]
```

Together, those links identify a connected set of locally named traces.

We are exploring the word **meme** for that distributed object: not a single canonical name, but continuity reconstructed across memory systems.

In that sense, a meme is not encoded by one Village Link. It emerges from a graph of them.

This is currently a research idea, not a requirement of the primitive.

## What developers should get

The primitive should support small, boring, useful tools.

A Village Link utility kit might provide functions such as:

```text
parse(vl)
validate(vl)
left(vl)
right(vl)
name(endpoint)
context(endpoint)
isSameContext(vl)
connectedComponent(vls, endpoint)
equivalent(a, b, graph)
```

The first useful package does not need to solve trust, reputation, governance, or ontology.

It can simply help developers:

- create Village Links;
- parse them;
- validate them;
- inspect their endpoints;
- traverse networks of equality assertions;
- identify aliases;
- disambiguate locally named traces.

Higher-level systems can decide what weight to give any assertion.

## Browser

A Village Link browser sits above the primitive.

It is therefore allowed to know things that the primitive does not know: HTTP, web pages, search, publishers, natural-language input, rendering conventions, and particular memory-system adapters.

That distinction matters.

A useful design test is:

> Is this requirement inherent to a Village Link, or merely convenient for a Village Link browser?

Requirements from higher layers should not silently become requirements of the primitive.

## Current status

Village Link is experimental.

The project is currently revisiting several earlier architectural assumptions, including:

- whether a Village Link should contain any publishing domain;
- the exact syntax and codec for `vl:`;
- how endpoints identify local names and memory systems;
- how online and offline memory systems coexist;
- which graph operations belong in a core developer utility kit;
- how publishers, browsers and trust systems sit above the primitive;
- whether distributed objects such as memes should be named or merely discovered.

The goal is deliberately small:

**make equality across memory systems expressible without requiring the systems themselves to agree on a global identity architecture.**

If that primitive is useful, the larger consequences can be investigated afterwards.

## Repository

This repository contains the evolving specification, architectural decisions, prototypes, publisher testbeds, browser work, examples and research notes.

The project is young enough that terminology and architecture remain open to challenge.

Useful criticism is especially welcome where the primitive appears to require more machinery than the statement itself justifies.
