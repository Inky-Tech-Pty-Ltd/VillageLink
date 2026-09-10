# Documentation map

**Status:** Maintained  
**Last updated:** 10 September 2026

This page identifies the natural home of each Village Link concept. Other documents may summarise a concept and link to its source, but should not silently redefine it.

| Subject | Source of truth | Purpose |
| --- | --- | --- |
| Project overview | [README.md](README.md) | Short explanation of the proposal, its boundaries and current status |
| Contribution and participation | [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute, how decisions are made and the current stewardship boundary |
| Terms | [glossary.md](glossary.md) | Current project vocabulary and deprecated usages |
| Normative project requirements | [requirements.md](requirements.md) | Requirements for the standard, reference publisher and consuming applications |
| Primitive semantics and syntax | [specification.md](specification.md) | Conformance rules for an individual Village Link |
| Endpoint prefixes `gc.` and `vc.` | [ADR-005](docs/adr/005-endpoint-identifiers-and-naming.md) | Adopted endpoint naming conventions |
| Two-ended marker `wab.` and serialization | [ADR-006](docs/adr/006-village-link-serialization.md) | Adopted marker prefix and proposed endpoint separator/escaping |
| Accepted architectural decisions | [docs/adr/](docs/adr/) | Decision, rationale, alternatives and consequences |
| Sequence of committed work | [roadmap.md](roadmap.md) | Targets, gates and work already chosen |
| Uncommitted ideas and experiments | [wishlist.md](wishlist.md) | Possibilities that have not entered the roadmap |
| Reference publisher | [ADR-003](docs/adr/003-mediawiki-reference-publisher.md) | MediaWiki publication and governance architecture |
| Reader-side interpretation | [trust-engine.md](trust-engine.md) | Trust Engine problem and design space |
| Trust Engine experimental model | [Research 002](docs/research/002-modelling-g1.md) | Paired G0/G1 model, evaluation tasks and falsifiable hypothesis |
| Stateless construction | [composer.md](composer.md) and [ADR-007](docs/adr/007-stateless-composer.md) | Composer and the decision not to make it a persistent credential manager |
| Governance across memory systems | [emergent-governance.md](emergent-governance.md) | Exploratory consequences, not protocol requirements |
| AI governance | [ai-governance.md](ai-governance.md) | Possible application of the wider model to artificial agents |
| Adoption and explanation | [docs/responses/01-pathway-to-relevance.md](docs/responses/01-pathway-to-relevance.md) | Audience-specific explanation and pathway to relevance |
| Prior art | [docs/research/](docs/research/) | Research notes and comparisons |
| Prototype behaviour | [prototype/README.md](prototype/README.md) and code | Current implementation, including deliberately temporary plumbing |

## Four project areas

The current project model is:

1. **Define** — Developer of the Standard.
2. **Publish** — Publisher, with MediaWiki as the reference implementation.
3. **Interpret** — Browser + Trust Engine.
4. **Compose** — Composer, a small stateless reference tool for constructing village links and star credentials.

The previously proposed **Star Credential Manager** is not a current project area. ADR-007 records why persistent management of private identity relationships was separated from composition and left outside the current architecture.

These areas can influence one another, but requirements from a later area should not be added to the primitive without a separate architectural decision.

## Adopted prefix family

The project currently adopts three conventional DNS prefixes:

- `wab.` — two-ended Village Link marker; mnemonic for **A ← W → B**;
- `gc.` — global-context endpoint naming; and
- `vc.` — village-context endpoint naming.

These conventions use ordinary HTTPS/DNS naming. `wab.` is intentionally not derived from the Village Link project name so that the marker is suitable for adoption by independent or competing implementations.

## Document rules

- The README summarises; it does not carry unique architectural commitments.
- The specification states current normative behaviour. An ADR explains why a decision was made.
- Requirements state constraints, not implementation detail.
- The roadmap contains chosen work. The wishlist contains work not yet chosen.
- Concept documents may explore consequences and hypotheses, but must label them as such.
- Historical README candidates in `docs/` are records of development, not current alternatives and are not rewritten merely for terminology consistency.
- When a concept changes, update its source of truth first and then repair summaries and links.
