# ADR-007: Separate stateless composition from credential management

**Status:** Accepted  
**Date:** 7 September 2026

## Context

The project previously described a fourth principal area of work as the **Star Credential Manager**. The concept combined two functions that initially appeared closely related:

1. constructing a village link or star credential from supplied identifiers; and
2. persistently managing a person's or other entity's Village Links and star credentials, including selecting different subsets for different audiences.

Further consideration showed that these are architecturally and ethically very different functions.

The first is a small transformation problem. A user supplies a small number of inputs; software serializes a conforming village link or a star credential; the result is returned. The tool need not know who the user is, maintain an account, retain the inputs, or remember the output. It can potentially run entirely client-side and be small enough to inspect, reimplement and distribute as open-source reference software.

The second function creates a new and unusually sensitive store of information. A persistent credential manager could accumulate equivalence relationships between identities that a person intentionally keeps separate across different memory systems and audiences.

For example, a person might legitimately be identifiable in one context as a member of a public organisation, in another under a pseudonym used for a social or sexual community, and in another through relationships with people to whom disclosure of those other identities could expose the person to serious harm. The sensitive information is not necessarily any individual identifier. It is the private assertion that the identifiers refer to the same person: **A ↔ B**.

A central database of such assertions would therefore aggregate precisely the information that Village Link makes powerful: equivalence across contexts. Compromise, misuse, coercive disclosure, accidental disclosure or changes in the operator's incentives could create harms far beyond those of losing an ordinary account database.

The project also recognised that people and organisations already use many mature mechanisms to control which information is disclosed to which audiences: separate accounts, applications, authentication and authorisation systems, encrypted communication, private groups, password managers, identity wallets and ordinary social practices. Village Link does not need to reproduce those systems merely because the primitive makes cross-context equivalence expressible.

## Decision

The project will sharply separate **composition** from **persistent credential management**.

The near-term fourth artefact is **Composer**.

Composer is a small, stateless reference tool that accepts supplied identifiers and constructs either:

- a conforming village link; or
- a machine-readable star credential, initially expected to include a JSON representation.

Composer SHOULD retain no user inputs or outputs after the composition operation. Where practical it SHOULD be capable of operating entirely client-side, without transmitting the supplied identifiers to a Village Link service. Its behaviour should be deterministic and straightforward to reproduce from the public standard.

The intended public location is provisionally:

`village.link/composer`

The name **Composer** is intentionally modest. It describes construction of artefacts without implying certification, custody, identity management, audience management or persistence.

The previously proposed **Star Credential Manager** is removed from the current project architecture and roadmap.

Village Link will not presently build a persistent application or central database for managing a user's complete collection of private Village Links, star credentials or audience-specific identity mappings.

This is a decision about present scope, not a claim that persistent credential-management software can never be built safely. Any future proposal to build such a system MUST be treated as a new architectural and security decision rather than as a natural extension of Composer.

## Rationale

### Construction does not require custody

A conforming artefact can be constructed without retaining the relationships from which it was made. Persistence is therefore unnecessary to the basic user need.

### Equivalence can itself be sensitive

Village Link's primitive makes the statement that two identifiers refer to the same entity. In private identity management, the most dangerous datum may be exactly that relationship. A database containing many such private equivalences can reveal connections that no individual memory system exposes.

### Existing audience-control systems should remain available

Users already have many ways to decide what information reaches which audience. Composer can produce an artefact for use in those systems without becoming the master system that remembers every possible audience and identity relationship.

### The standard remains independent

Composer is reference tooling over the Village Link standard. The standard does not require Composer, and independent implementations can construct the same artefacts without permission from or communication with `village.link`.

### Minimal software is easier to trust

A small stateless tool can be inspected, tested, reimplemented and potentially run locally. This creates a much smaller trust surface than a hosted identity-management service.

## Consequences

The project model becomes:

1. **Standard** — defines the Village Link primitive and related formats;
2. **Publisher** — publishes and governs public collections of Village Links;
3. **Browser + Trust Engine** — consumes and interprets the graph for a user; and
4. **Composer** — constructs village links and star credentials without becoming their custodian.

The previous shorthand **Define → Publish → Interpret → Disclose** is retired because Composer does not decide what should be disclosed to an audience. A more accurate shorthand is:

> **Define → Publish → Interpret → Compose**

Composer is expected to be needed relatively early because developers, editors and users require a reliable way to construct examples without hand-encoding the syntax.

Persistent private credential management is not a prerequisite for the standard, the publisher, the Trust Engine, the reference browser or Composer.

Documents that previously describe the Star Credential Manager as a principal Village Link component should be updated. Historical documents may retain the term where preserving the history of the idea is useful, but current architecture must not imply that a persistent manager remains planned.

## Security boundary

Composer MUST NOT quietly evolve into a credential database.

Features such as accounts, synchronisation, saved credentials, audience profiles, private identity graphs, cloud backup or cross-device persistence materially change its security model. Any proposal to add such functionality requires explicit architectural review, including threat modelling of unwanted correlation and disclosure of private equivalence relationships.

A useful default principle is:

> **Village Link should enable selective equivalence without encouraging universal identity aggregation.**

## Relationship to the Publisher

The public reference Publisher and Composer have different trust models.

The Publisher deliberately maintains a public, contestable graph whose legitimacy depends on governance, provenance and the ability to challenge assertions.

Composer need not publish anything. It may construct an artefact that the user publishes through the reference Publisher, uses through another publisher, transmits privately through an existing system, or never publishes at all.

This separation prevents the convenience of composition from requiring either public disclosure or central private custody.

## Alternatives considered

### Continue with the Star Credential Manager

Rejected for the current architecture. The name and concept strongly imply persistent management of credentials and audience-specific disclosure, combining a simple construction need with a substantially more dangerous identity-management problem.

### Build a secure central credential store

Not pursued. Encryption, access control and careful engineering could mitigate some risks, but the project has not established a need to possess this data in the first place. Avoiding unnecessary custody is a stronger initial control.

### Add audience and disclosure machinery to the Village Link standard

Rejected. Audience selection is an application concern and should not enlarge the primitive.

### Provide no construction tool

Rejected. A small reference Composer will make the standard easier to test, demonstrate and use, while imposing little architectural commitment.

## Future review

A future persistent credential-management proposal is not forbidden, but it starts from zero. It must establish a concrete user need, explain why existing tools are insufficient, define who holds the private equivalence data, and demonstrate a security and governance model proportionate to the consequences of disclosure.
