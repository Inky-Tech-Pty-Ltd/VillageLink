# Documentation map

**Status:** Maintained
**Last updated:** 3 September 2026

This page identifies the natural home of each Village Link concept. Other documents may summarise a concept and link to its source, but should not silently redefine it.

| Subject | Source of truth | Purpose |
| --- | --- | --- |
| Project overview | [README.md](README.md) | Short explanation of the proposal, its boundaries and current status |
| Terms | [Glossary.md](Glossary.md) | Current project vocabulary and deprecated usages |
| Normative project requirements | [Requirements.md](Requirements.md) | Requirements for the standard, reference publisher and consuming applications |
| Primitive semantics and syntax | [Specification.md](Specification.md) | Conformance rules for an individual Village Link |
| Accepted architectural decisions | [docs/adr/](docs/adr/) | Decision, rationale, alternatives and consequences |
| Sequence of committed work | [Roadmap.md](Roadmap.md) | Targets, gates and work already chosen |
| Uncommitted ideas and experiments | [Wishlist.md](Wishlist.md) | Possibilities that have not entered the roadmap |
| Reference publisher | [ADR-003](docs/adr/003-mediawiki-reference-role-2-publisher.md) | MediaWiki publication and governance architecture |
| Reader-side interpretation | [trust-engine.md](trust-engine.md) | Trust Engine problem and design space |
| Audience-specific disclosure | [star-credential-manager.md](star-credential-manager.md) | Star Credential Manager problem and design space |
| Governance across memory systems | [emergent-governance.md](emergent-governance.md) | Exploratory consequences, not protocol requirements |
| AI governance | [ai-governance.md](ai-governance.md) | Possible application of the wider model to artificial agents |
| Adoption and explanation | [docs/responses/01-pathway-to-relevance.md](docs/responses/01-pathway-to-relevance.md) | Audience-specific explanation and pathway to relevance |
| Prior art | [docs/research/](docs/research/) | Research notes and comparisons |
| Prototype behaviour | [prototype/README.md](prototype/README.md) and code | Current implementation, including deliberately temporary plumbing |

## Four project areas

The current project model is:

1. **Define** — Developer of the Standard.
2. **Publish** — Publisher, with MediaWiki as the reference implementation.
3. **Interpret** — Trust Engine.
4. **Disclose** — Star Credential Manager.

These areas can influence one another, but requirements from a later area should not be added to the primitive without a separate architectural decision.

## Document rules

- The README summarises; it does not carry unique architectural commitments.
- The specification states current normative behaviour. An ADR explains why a decision was made.
- Requirements state constraints, not implementation detail.
- The roadmap contains chosen work. The wishlist contains work not yet chosen.
- Concept documents may explore consequences and hypotheses, but must label them as such.
- Historical README candidates in `docs/` are records of development, not current alternatives.
- When a concept changes, update its source of truth first and then repair summaries and links.
