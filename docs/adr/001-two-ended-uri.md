# ADR-001: Village Link is a self-contained, two-ended hyperlink

**Status:** Accepted  
**Date:** 20 August 2026  
**Terminology updated:** 6 September 2026

## Context

Village Link needs a minimal way for a web resource, W, to state a connection between two independently meaningful identifiers, A and B.

Three broad architectures were considered:

1. **A self-contained Village Link URI containing both endpoint URIs.**
2. **A URI identifying a Village Link resource**, which must be dereferenced to discover the two endpoints.
3. **Two independent endpoint URIs plus a separate mechanism** establishing that they form a pair.

The design objective is to make the Village Link primitive as small as possible and to impose as few requirements as possible on webpages and on the systems being connected.

## Decision

A Village Link will be a **single, self-contained, two-ended hyperlink**.

Conceptually:

`[Village Link identifier] [separator] [URI A] [separator] [URI B]`

For example, the two endpoints might be ordinary identifiers already controlled by unrelated systems:

`https://github.com/Joe-Rasmussen`

and

`https://www.facebook.com/joe.rasmussen.70/`

The Village Link contains both endpoint URIs. It therefore carries the substance of the statement without requiring the link to be dereferenced to another resource.

The webpage, W, is not encoded as a third endpoint. **W is the web resource in which the Village Link is found.**

In its simplest conceptual form:

**W states A ↔ B.**

## Rationale

This architecture keeps the primitive unusually small.

The endpoint systems do not need to know about Village Link or modify their existing identifiers.

The webpage does not need to operate an additional resource that must remain available and dereferenceable.

The statement remains intelligible from the Village Link itself rather than depending on information stored elsewhere.

The object also preserves an important property of the conventional hyperlink: **the web resource in which a link occurs carries information.** Multiple webpages may independently contain the same or conflicting statements, allowing larger systems to interpret the resulting pattern without Village Link itself adjudicating between them.

An ordinary hyperlink can be understood as:

**W → A.**

A Village Link extends this idea:

**A ← W → B.**

The semantic statement carried by that structure is:

**W states A ↔ B.**

## Consequences and open questions

This decision deliberately leaves several implementation questions unresolved, including:

- the exact syntax identifying a URI as a Village Link;
- how arbitrary endpoint URIs are escaped or encoded within the Village Link URI;
- practical limits arising from very long endpoint URIs;
- precisely how the identity, provenance and history of W are established, particularly where pages or links are copied, quoted, syndicated or archived;
- browser behaviour when a Village Link is activated;
- how search, reputation and other memory systems discover, index and interpret Village Links.

These questions should be addressed separately. They do not form part of the architectural decision recorded here.
