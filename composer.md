# Composer

## Status

Near-term reference-tool concept.

Composer is a small, stateless tool for constructing artefacts that conform to the Village Link standard.

Its intended public location is provisionally:

`village.link/composer`

## The idea

Composer accepts a small set of supplied identifiers and produces either:

- a village link; or
- a machine-readable star credential, initially expected to include a JSON representation.

In deliberately simple form:

> **inputs → compose → output → forget**

Composer does not need an account, a credential database or a persistent record of the relationships it processes.

## Trust model

A user's private equivalence relationships can be highly sensitive. The fact that identifier A and identifier B refer to the same entity may itself be information that the user depends upon remaining undisclosed.

Composer should therefore know as little as technically possible.

Where practical, it should run entirely client-side so that supplied identifiers need not be transmitted to a Village Link service. It should not retain inputs or outputs after the composition operation.

This is not merely an implementation convenience. Avoiding custody is part of the intended security model.

## Relationship to the standard

Composer is reference tooling, not part of the Village Link primitive.

A conforming village link or star credential can be constructed by any implementation. Nobody should need to contact `village.link`, use Composer or obtain permission from the Village Link project to create one.

Composer exists because a tiny, inspectable reference implementation makes the standard easier to test, demonstrate and use.

## Relationship to publishing

Composition is not publication.

A user may take Composer's output and:

- publish it through the reference MediaWiki Publisher;
- publish it through another publisher;
- transmit it privately using an existing system;
- store it using tools of their own choosing; or
- discard it.

Composer does not decide which audience should receive an artefact.

## Relationship to the former Star Credential Manager

The project previously considered a **Star Credential Manager** that combined construction with persistent management of identity relationships and audience-specific disclosure.

[ADR-007](docs/adr/007-stateless-composer.md) records the decision to split those concerns sharply. Composer retains the small construction function. Persistent private credential management is outside the current project architecture.

Features such as saved credentials, accounts, synchronisation, audience profiles, private identity graphs or cloud backup would materially change Composer's security model and require a new architectural decision.

## Near-term objective

Build the smallest useful Composer that can reliably construct examples from the evolving specification. It should make hand-encoding unnecessary while remaining simple enough to inspect and replace.
