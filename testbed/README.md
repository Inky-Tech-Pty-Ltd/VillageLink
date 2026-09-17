# Village Link testbed

The Village Link testbed exists to test the primitive against deliberately different implementations rather than allowing the first implementation to define the architecture by accident.

The project imagines many independent publishers of Village Links and Star Credentials. No publisher, storage technology, user interface, or publication platform is privileged by the primitive.

## Test implementations

### Type 1 — MediaWiki (Anna)

**Anna** is the project's first publisher implementation. It uses MediaWiki and has been useful for learning how Village Links and Star Credentials behave when represented as human-readable wiki pages, backed by an existing publication and revision system.

Anna should now be treated as a **testbed artefact and reference implementation**, not as required Village Link infrastructure and not as the canonical publisher.

The existing Anna source material remains in `anna/` for now. A later mechanical cleanup may move implementation-specific material under this testbed once doing so will not unnecessarily disturb the working publication bridge.

### Type 2 — deliberately unlike Anna

The next useful experiment is a publisher that is intentionally unlike MediaWiki. A candidate is a minimal relational/SQL-backed publisher with very little presentation furniture, potentially operated under an Inky Tech testbed domain rather than `village.link`.

The point is not to build a second polished publication product. The question is:

> Can the same Village Link and Star Credential semantics survive a substantially different publication system without special pleading?

If behaviour or semantics must change, that is evidence that something believed to belong to the primitive may actually belong to an implementation.

### Type 3 and beyond — independent implementations

Independent implementations are especially valuable. Contributors should be encouraged to satisfy the publication requirements in whatever small architecture seems natural to them rather than reproducing Anna or Type 2. A static site, document store, graph database, bespoke service, or another design may reveal different assumptions.

## What the testbed is for

The testbed should help distinguish:

- properties of the Village Link primitive from properties of a particular publisher;
- required semantics from convenient presentation choices;
- interoperable publication behaviour from implementation-specific behaviour;
- useful invariants from accidental architecture.

A useful recurring question is:

> What remains invariant across unlike implementations?

Those invariants are candidates for the Village Link standard.

## Anna learnings

The MediaWiki experiment has already shown that:

- Village Links and Star Credentials can be published as ordinary human-readable web resources;
- an established publication system supplies useful revision history, authorship and page-level provenance without those mechanisms needing to be invented by Village Link;
- the GitHub repository can act as source material for an automated publication bridge into another system;
- presentation choices such as tables, namespaces, images and page naming are useful implementation experiments but should not silently become requirements of the primitive;
- operational and privacy details of a publisher can obstruct publication of an otherwise useful test corpus and should be separated from the primitive itself.

These observations are provisional. They should be expanded and corrected as the Anna experiment is reviewed, including in response to contributor discussion.

## Near-term work

1. Record the Anna/MediaWiki learnings more completely.
2. Remove or replace personal data that unnecessarily prevents the Anna test corpus from being openly inspectable.
3. Specify the smallest useful Type 2 experiment before building it.
4. Invite independent contributors to propose unlike Type 3 implementations.
5. Keep publisher experimentation bounded: the larger project needs reader-side experiments, including the Trust Engine, rather than an ever-growing family of publisher products.

## Related experiments

The **Trust Engine** also tests the usefulness of the primitive: it is one imagined consumer/interpreter of a Village Link graph, and other consumers should be possible. Unlike Anna, however, it is a substantial application rather than merely a publication fixture. Its eventual repository boundary should therefore be considered separately from the publisher testbed.
