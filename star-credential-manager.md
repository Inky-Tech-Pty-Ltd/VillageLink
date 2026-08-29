# Star Credential Manager

## Status

Early concept document.

The Star Credential Manager is currently the least mature of the four principal Village Link concepts. This document records the problem and the emerging design space; it does not imply that Village Link must ultimately provide this functionality.

One legitimate architectural conclusion remains: **this may not be our problem**.

## The idea

A **star credential** is a collection of Village Link edges connecting an entity to traces it has left in different memory systems.

The entity can be a person, company, AI agent, algorithm, place, word or any other noun.

A sufficiently broad star credential might therefore contain representations of the same noun across many contexts.

That creates a problem which does not arise merely from whether the individual Village Links are true:

> **Given all the contexts in which a noun has left traces, which of those traces should be presented to this audience?**

The working name for a tool that helps answer that question is the **Star Credential Manager**.

## A subject- and publisher-side technology

The Star Credential Manager is principally concerned with disclosure.

Where the **Trust Engine** asks a reader what should be discovered from the graph, the Star Credential Manager asks what an entity or publisher should present to a particular audience.

In deliberately simple form:

> **Trust Engine: What should I discover from the graph?**
>
> **Star Credential Manager: What should the graph discover about me?**

The second formulation is most natural for people, but the underlying idea is more general. A company, AI agent or other entity may also have reasons to present different collections of contextual evidence to different audiences.

## The Anna problem

An example from *Anna Karenina* illustrates the issue.

Anna leaves traces in many memory systems: her household, family, social circle and relationship with Count Vronsky, among others.

A servant in the Karenin household may possess true information connecting Anna to the context of Anna-and-Vronsky.

The danger does not arise because the connection is necessarily false. It arises because a true connection can be profoundly inappropriate for a particular audience.

Village Link therefore exposes a general problem:

> **Truth and appropriate disclosure are different questions.**

A system capable of connecting contexts makes that distinction especially important.

## The outer-boundary star

One emerging model is an **outer-boundary star credential**.

The outer-boundary star is the broadest collection of contextual links that an entity is willing and able to use when constructing credentials for any audience.

It is not necessarily a credential that would ever be published as a whole.

Instead, particular credentials can be constructed as projections or subsets of that larger star.

For example, a person might construct:

- a **public star**;
- a **professional star**;
- a **family star**;
- a **financial-services star**;
- a **dating star**;
- or a credential assembled for one particular transaction or audience.

These examples are deliberately diverse. The point is not to prescribe credential categories, but to show that the same noun can legitimately present different evidence in different contexts.

In shorthand:

> **Outer-boundary star → audience-specific stars**

## Why subsets may be simpler than permissions

A tempting design would attach elaborate access-control rules to every ray of a single star credential.

That may be unnecessary.

An alternative is to regard a presented credential simply as a newly constructed subset of available links. The underlying Village Links remain small and general; audience management occurs at a higher layer.

This has an important architectural advantage:

> **The Village Link standard does not need to know that the Star Credential Manager exists.**

The manager can operate over Village Links without adding audience, permission or identity-management machinery to the primitive itself.

## Existing technologies

Twenty-first-century publishers already have extensive mechanisms for controlling audiences: authentication, authorisation, access-control lists, private groups, encrypted messaging, capability systems, selective disclosure and many others.

Village Link should not reproduce these technologies merely because star credentials make the audience problem visible.

The project must therefore distinguish two questions:

1. **Is management of audience-specific star credentials an important problem?**
2. **Does Village Link itself need to provide a new solution to that problem?**

The answer to the first appears to be yes.

The answer to the second remains open.

## Relationship to the Village Link roles

The project currently distinguishes four principal areas of work:

1. **Developer of the Standard** — defines the Village Link primitive.
2. **Publisher** — publishes Village Links and thereby helps establish the graph.
3. **Trust Engine** — reads and interprets the graph for a user.
4. **Star Credential Manager** — helps an entity construct or disclose appropriate subsets of its available star credential to different audiences.

These can be summarised as:

> **Define → Publish → Interpret → Disclose**

The Star Credential Manager occupies the fourth position: disclosure.

## Architectural restraint

The Star Credential Manager is particularly susceptible to scope expansion.

Identity management, authentication, authorisation, encryption, consent, revocation, wallets, credential formats and access control are all mature and complicated fields. Village Link should not absorb them without a compelling reason.

The strongest current constraint is therefore:

> **Do not make the Village Link primitive more complicated in order to solve the Star Credential Manager problem.**

If existing technologies can provide the necessary audience control, using them may be the correct architecture.

If no new Village Link-specific technology is required, that is a successful design outcome rather than a failure to build a product.

## Open questions

Important unresolved questions include:

- Is the outer-boundary star a useful conceptual object, or merely a design aid?
- Who constructs a star credential: the subject, a publisher, an agent acting for the subject, or some combination?
- Should an audience-specific star be persistent, ephemeral or generated on demand?
- How should a credential distinguish absence of a link from deliberate non-disclosure?
- What happens when third parties publish true links that the subject would prefer not to disclose?
- How do consent, revocation and changing contexts interact with already-published Village Links?
- Which existing selective-disclosure and access-control technologies are sufficient?
- Is there any functionality here that is genuinely specific to Village Link?

## Working hypothesis

The Star Credential Manager is not presently a promised product.

It is a way of making a problem explicit:

> **A general mechanism for connecting a noun across contexts creates a corresponding need to think carefully about which contexts are presented together.**

The project should investigate that problem without assuming in advance that it must invent the solution.