# ADR-003: Wiki-style contestability for Role 2 publishers

**Status:** Proposed  
**Date:** 28 August 2026

## Context

Role 2 Village Link projects publish collections of Village Links.

Publication creates the possibility of harm. A publisher may publish a mistaken, misleading or malicious equivalence assertion; evidence may change; an assertion that was reasonable when made may later become wrong; or a publisher may become a point at which errors, bias or abuse are propagated into systems that consume Village Links.

One response would be to place responsibility for maintaining the published collection entirely with the publisher. This gives the publisher substantial epistemic and governance authority: the publisher determines what appears in the collection, what is corrected, and what disappears.

Wikipedia demonstrates another architectural pattern. Contributions can be broadly open while changes remain historically visible. Assertions are not protected from challenge merely because they have already been published. Edits, reversions, discussion and provenance provide mechanisms through which mistakes and abuse can be observed and repaired.

This suggests a possible governance pattern for Role 2 Village Link publishers.

## Proposal

A Role 2 Village Link publisher may implement its published collection as a **contestable public record** rather than as an opaque, publisher-controlled database.

In a wiki-style implementation, participants might be able to:

- propose a new Village Link;
- challenge or dispute an existing Village Link;
- add, amend or challenge supporting evidence;
- propose correction or removal of a Village Link; and
- inspect the history of these actions.

Changes should not silently overwrite the previous state. The system should preserve enough history to make changes inspectable and, where appropriate, reversible.

The architectural principle is:

**openness of contribution + persistence of history + reversibility + accountability.**

The publisher need not act as an oracle determining a single final truth. It can instead provide machinery through which assertions are made, challenged, corrected and accumulated.

## Rationale

This pattern does not prevent harmful assertions from being made or published.

It may, however, make an important class of harms **observable, contestable and repairable**.

A mistaken or malicious Village Link need not become an unexplained fact in a database. Its origin, subsequent challenges, evidence and revision history can themselves become part of the information available to people and systems evaluating it.

This also fits the Village Link architecture established in ADR-001 and ADR-002. The core primitive remains deliberately small. Questions of evidence, disagreement, governance and consequence can be handled by systems built around published Village Links rather than being encoded into the primitive itself.

## Consequences and open questions

A wiki-style publication model introduces its own risks and design requirements, including:

- vandalism and spam;
- coordinated manipulation or brigading;
- harassment through repeated publication or editing;
- edit wars;
- moderation and dispute-resolution mechanisms;
- contributor identity, pseudonymity and reputation;
- rate limits and other anti-abuse controls;
- circumstances in which records or edits should be protected;
- how deletion requests interact with persistent revision history;
- whether a disputed Village Link remains visible and, if so, how its status is represented;
- whether an edit modifies an existing assertion or creates a new competing assertion; and
- how downstream consumers learn that an assertion has been challenged, corrected or withdrawn.

The existence of an audit trail may itself create privacy or safety harms. Persistence is therefore not an unconditional good and requires further analysis.

## Relationship to harms assessment

This proposal suggests a useful question for harms analysis of Role 2 systems:

> When the system causes or propagates harm, what machinery exists for detecting, contesting and repairing it?

Avoiding harm remains important, but the capacity for repair may also be an architectural property worth evaluating explicitly.

## Status of this proposal

This ADR records an architectural idea, not a requirement of Village Link or a decision binding Role 2 publishers.

Further harms analysis, implementation experience and discussion should determine whether the proposal is accepted, modified or rejected.
