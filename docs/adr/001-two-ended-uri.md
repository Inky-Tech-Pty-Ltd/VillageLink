# ADR-001: Village Link is a self-contained, two-ended hyperlink

**Status:** Accepted  
**Date:** 20 August 2026

## Context

Village Link needs a minimal way for a publisher, P, to assert a connection between two independently meaningful identifiers, A and B.

Three broad architectures were considered:

1. **A self-contained Village Link URI containing both endpoint URIs.**
2. **A URI identifying a Village Link resource**, which must be dereferenced to discover the two endpoints.
3. **Two independent endpoint URIs plus a separate mechanism** establishing that they form a pair.

The design objective is to make the Village Link primitive as small as possible and to impose as few requirements as possible on publishers and on the systems being connected.

## Decision

A Village Link will be a **single, self-contained, two-ended hyperlink**.

Conceptually:

`[Village Link identifier] [separator] [URI A] [separator] [URI B]`

For example, the two endpoints might be ordinary identifiers already controlled by unrelated systems:

`https://github.com/Joe-Rasmussen`

and

`https://www.facebook.com/joe.rasmussen.70/`

The Village Link contains both endpoint URIs. It therefore carries the substance of the assertion without requiring the link to be dereferenced to another resource.

The publisher, P, is not encoded as a third endpoint. **P is established by the publication context:** whoever publishes the Village Link is asserting the connection between A and B.

In its simplest conceptual form:

**P asserts A ↔ B.**

## Rationale

This architecture keeps the primitive unusually small.

The endpoint systems do not need to know about Village Link or modify their existing identifiers.

The publisher does not need to operate an additional resource that must remain available and dereferenceable.

The assertion remains intelligible from the Village Link itself rather than depending on information stored elsewhere.

The object also preserves an important property of the conventional hyperlink: **the act of publication carries information about the publisher.** Multiple publishers may independently make the same or conflicting assertions, allowing larger systems to interpret the resulting pattern without Village Link itself adjudicating between them.

An ordinary hyperlink can be understood as:

**P points to A.**

A Village Link extends this idea:

**P connects A and B.**

## Consequences and open questions

This decision deliberately leaves several implementation questions unresolved, including:

- the exact syntax identifying a URI as a Village Link;
- how arbitrary endpoint URIs are escaped or encoded within the Village Link URI;
- practical limits arising from very long endpoint URIs;
- precisely how publication context establishes the identity of P, particularly where links are copied, quoted, syndicated or archived;
- browser behaviour when a Village Link is activated;
- how search, reputation and other memory systems discover, index and interpret Village Links.

These questions should be addressed separately. They do not form part of the architectural decision recorded here.
