# Village Link Roadmap

**Status:** Working draft  
**Roadmap horizon:** August 2026 to February 2027  
**Last updated:** 3 September 2026

## Purpose

This roadmap describes the intended sequence of work for taking Village Link from an initial concept to a credible open project with a working reference implementation, a useful demonstration and a clear basis for institutional support.

It is a planning document, not a specification or a promise. Dates are target windows and should change when evidence, contributors or constraints change.

By February 2027, Village Link should have:

- a comprehensible draft specification;
- documented requirements and architectural decisions;
- a working reference implementation;
- a meaningful test graph and graph publisher;
- a polished demonstration;
- credible open-source licensing, contribution and governance arrangements; and
- materials suitable for conversations with standards bodies, academia, public-interest funders and commercial investors.

## Project areas

Village Link currently contains four related areas of work. Inky Tech and the early contributors may work across them initially, but their responsibilities should remain visible and may require different institutional homes.

### 1. Developer of the Standard

Develops and maintains the open Village Link standard, its terminology, conformance materials and public technical process.

The intended direction is neutral, openly governed infrastructure. No publisher or application developer should receive privileged control of the standard merely because it helped initiate the project.

### 2. Publisher

Publishes and governs collections of Village Links. The reference Role 2 implementation is a MediaWiki, chosen to reuse mature publication, revision and community-governance machinery.

A published assertion is not made true merely by appearing in the graph. Provenance, evidence, time and publisher identity remain relevant. Multiple independent publishers should remain possible.

### 3. Trust Engine

Reads and interprets Village Link graphs for a user. Possible functions include discovery, filtering, ranking, comparison and trust assessment.

Different Trust Engines may apply different policies and algorithms over the same published assertions. Their requirements must not be loaded into the core primitive.

### 4. Star Credential Manager

Helps an entity or publisher construct and disclose audience-appropriate subsets of a broader star credential.

This is the least mature area. Existing identity, access-control and selective-disclosure technologies may supply much or all of the required machinery. The Village Link primitive should not be enlarged merely to create a product in this area.

The four areas can be summarised as **Define → Publish → Interpret → Disclose**.

## Operating principles

- **Public infrastructure first.** The standard, reference materials and technical discussion should develop with impeccable open-source credentials.
- **Separate standard from implementation.** The specification defines expected behaviour; the reference implementation demonstrates one way to achieve it.
- **Separate assertion from truth.** A Village Link records that a publisher made an assertion. Its credibility depends on provenance, evidence and the surrounding graph.
- **Working software should test ideas.** Early implementations are experiments and may be discarded.
- **Scope stays deliberately small.** The initial project does not need to solve identity, governance, search, AI alignment or online trust in full.
- **Roles should delineate over time.** Organisational separation is a planned outcome, not an inconvenience to address after commercial value emerges.
- **Decisions should remain inspectable.** Material architectural and governance decisions should be recorded in ADRs or equivalent documents.

## Documentation map

The foundation documents have distinct jobs:

| Document | Question answered |
| --- | --- |
| `README.md` | What is Village Link, and why might it matter? |
| `Roadmap.md` | In what order do we intend to learn, decide and build? |
| `Requirements.md` | What must the system and project enable or constrain? |
| `Specification.md` | What exactly is a conforming Village Link and how does it behave? |
| `Wishlist.md` | What ideas should we preserve without committing to them? |
| Path to an audience | Who might care, why would they participate, and how could relevance grow? |
| ADRs | Why were particular architectural decisions made? |

An item belongs in this roadmap only after the project has deliberately chosen to pursue it. Uncommitted possibilities belong in `Wishlist.md`.

## Workstreams

The roadmap is organised into six concurrent workstreams.

### A. Standard and technical governance

- Define the minimal Village Link primitive.
- Maintain requirements, specification, terminology and ADRs.
- Specify provenance and evidence fields without prematurely expanding the primitive.
- Develop examples, invalid examples and conformance tests.
- Establish an open contribution and decision-making process.

### B. Reference technology and demonstration

- Build a minimal database and API.
- Build a lightweight browser or browser-like interface.
- Resolve a Village Link into a side-by-side view of its two endpoints.
- Produce a repeatable, progressively polished demonstration.
- Keep reference code distinct from prospective commercial products.

### C. Graph publication and test data

- Create a small, inspectable corpus of Village Links.
- Record publisher, source or evidence, and sampling time.
- Begin with consented, public and mock examples.
- Demonstrate first-party, reciprocal and third-party assertions.
- Test small triangles and contradictory claims.

### D. Safety, privacy and misuse

- Develop a threat and misuse model.
- Examine transfer, compromise, abandonment, revocation and change over time.
- Identify privacy, harassment, impersonation and unwanted-correlation risks.
- Set data-publication rules for the test graph.
- Ensure the demo does not imply that graph assertions are authoritative facts.

### E. Community and audience

- Develop concise explanations for technical and non-technical audiences.
- Recruit a small group of technically serious early contributors.
- Create contribution guidance and approachable starter work.
- Test the proposition with people concerned about AI alignment, governance, provenance, identity and public digital infrastructure.
- Prepare for engagement with Linux, IETF, W3C, IIW and adjacent communities without prematurely claiming standards status.

### F. Organisation, IP and resources

- Complete Inky Tech constitution and AGM work.
- Establish IP provenance for existing documents, diagrams, code and data.
- Select provisional licences before inviting substantial outside contribution.
- Define the intended boundary between public infrastructure and commercial activity.
- Develop credible resourcing cases for the public-interest and commercial roles.

## Milestones

### Phase 0 — Origins and initial architectural choice

**Status:** substantially complete before 21 August 2026

- Original core paper drafted.
- GPT enlisted as a project assistant.
- Key features of the primitive explored.
- Private GitHub repository established.
- Initial README, Wishlist and architectural decision record created.
- Initial decision made to prototype a one-URI edge object, while retaining alternative models for review.

**Evidence of completion:** the project has a shared repository, an articulated problem and a recorded initial architectural direction.

### Phase 1 — Establish the project foundation

**Target:** 21 August–15 September 2026

- Create the foundation-document set: README, Roadmap, Wishlist, Requirements, Specification and Path to an Audience.
- State the four project areas consistently across the documents.
- Reconcile the README's conceptual history with the current primitive.
- Record unresolved architectural questions rather than hiding them in prose.
- Establish minimal repository conventions: contribution guide, issue templates, decision process and document status labels.
- Inventory the ownership and provenance of existing text, diagrams, examples and code.
- Select a provisional open-source licence strategy, including whether specifications, code and data need different licences.
- Define explicit exclusions for the first implementation.

**Exit criteria:** a serious developer can understand the proposition, distinguish commitments from ideas, identify open questions and see how to contribute without first receiving a private oral history.

### Phase 2 — Minimal end-to-end implementation

**Target:** September–October 2026

- Establish lightweight test-bed server infrastructure, initially using the spare laptop where practical.
- Implement the first database schema for Village Links.
- Store at least the link, publisher, source or evidence, and sampling datetime.
- Implement create, retrieve and display operations.
- Build a minimal browser interface in which conventional links behave conventionally and a Village Link opens its endpoints side by side.
- Populate a small test graph using Steve Byrnes examples, Joe examples, the Puck example and clearly labelled mock entities.
- Add automated tests for the simplest valid and invalid cases.
- Document how another developer can run the system locally.

**Exit criteria:** a fresh developer environment can run a documented demonstration that creates, stores, retrieves and displays a small set of Village Links.

### Phase 3 — Test the model, not merely the software

**Target:** October–November 2026

- Construct examples of first-person, reciprocal and third-party assertions.
- Construct small verification triangles and at least one contradictory-claim example.
- Revisit whether the primitive is best understood as a Village Link, a general double-headed hyperlink, or one application of a more general object.
- Revisit the alternative assertion-object architecture raised by Sankarshan.
- Test Brendan Miller's assertion that required objects may already exist within DTG.
- Conduct a focused architectural review of the star credential.
- Decide which attributes belong in the primitive, which belong in a dereferenced representation and which remain external evidence.
- Begin a machine-readable conformance corpus.

**Exit criteria:** the project can explain what its primitive adds to existing web objects, show competing claims without collapsing them into truth, and identify the principal remaining architectural decisions.

### Phase 4 — Credibility, safety and separation

**Target:** November–December 2026

- Produce an initial threat, privacy and misuse model.
- Address lifecycle cases including change, expiry, transfer, compromise, abandonment and revocation.
- Define publication rules for consented, public, inferred and mock data.
- Decide the initial status of the graph publisher: bootstrap experiment, continuing public infrastructure or precursor to multiple publishers.
- Draft governance arrangements for the standards-steward role.
- Define how Inky Tech may participate as a commercial implementer without privileged control of the standard.
- Confirm licences and contribution terms before widening participation.
- Separate repositories or repository areas where organisational clarity requires it.

**Exit criteria:** prospective contributors can determine what is open, who decides, who owns their contributions, how harms are considered and where commercial activity begins.

### Phase 5 — Small contributor community and public-release candidate

**Target:** December 2026–January 2027

- Recruit and support a regular contributing group of approximately 2–7 developers.
- Turn architectural unknowns into reviewable issues and small contributions.
- Improve installation, test coverage, examples and documentation from contributor feedback.
- Develop one-sentence, 30-second, two-minute and technical explanations.
- Produce an adoption ladder from early collaborators to useful niche and wider network effects.
- Prepare the repository or repositories for public release.
- Seek external review from relevant technical, standards, academic and public-interest communities.

**Exit criteria:** contribution no longer depends exclusively on Joe and Puck transmitting project context, and at least two independent contributors can run, critique and improve the work.

### Phase 6 — Six-month demonstration and resourcing readiness

**Target:** February 2027

- Publish the appropriate standards, reference-code and test-material repositories once governance, licensing and safety gates are met.
- Deliver a polished, repeatable demonstration with a meaningful sample graph.
- Publish a clear draft specification and conformance examples.
- Provide a packaged resource that others can use to run the demonstration or explain it accurately.
- Present a proposal for assigning and, where necessary, formally separating the four project areas.
- Prepare a public-interest resourcing case for the standards and shared-infrastructure work.
- Prepare a separate commercial opportunity case for Inky Tech and prospective investors.
- Begin targeted engagement with suitable forums such as IETF, W3C, IIW, Linux-related communities, academia and AI governance or alignment communities.

**Exit criteria:** Village Link can be evaluated without relying on faith in its founders: the object is specified, the software runs, the graph demonstrates its behaviour, the risks and unknowns are visible, and the public-interest and commercial propositions are distinguishable.

## Beyond the six-month horizon

The following are directional goals rather than scheduled commitments:

- A larger group of approximately 10–30 developers contributes regularly.
- Stewardship of the standard moves toward an appropriately neutral body or foundation.
- Multiple independent graph publishers demonstrate that the system is not dependent on a single source.
- The reference implementation and commercial implementations clearly diverge.
- The project participates constructively in relevant standards and public-interest forums.
- Infrastructure work is resourced through a foundation, academia, philanthropy or a similar source, ideally without dependence on a single government or company.
- Commercial work is separately resourced, potentially through venture investment, revenue or strategic partnerships.

## Decision gates

Dates alone do not trigger these transitions.

### Gate 1 — Invite outside contribution

Proceed when contribution terms, repository conventions, project roles and the status of contributions are clear.

### Gate 2 — Publish the repository

Proceed when IP provenance, licences, privacy risks and public documentation are sufficiently resolved. Publication may occur in stages rather than as a single unveiling.

### Gate 3 — Present as a draft standard

Proceed when the primitive has stable terminology, testable conformance statements, worked examples and documented alternatives. Until then, describe it as an experimental proposal.

### Gate 4 — Separate organisational roles

Proceed before public-interest contributors or funders could reasonably believe their work is being captured by a privileged commercial participant. Legal separation may follow functional and governance separation, but the intended boundary must already be visible.

### Gate 5 — Seek substantial funding

Proceed when the relevant role has a defined custodian, programme of work, budget, decision process and evidence of demand. Public-interest and commercial cases should be presented separately even when they share a history.

## Known dependencies and risks

- The primitive may change materially after technical review.
- Privacy and abuse concerns may constrain graph publication and demonstration data.
- A useful graph may require more publisher diversity than the bootstrap project can initially supply.
- Community credibility depends on early and enforceable separation between open infrastructure and private advantage.
- Joe's availability and health are project constraints; the roadmap should support sustainable progress rather than depend on continuous founder effort.
- A small contributor base creates key-person risk for both technical work and project memory.
- Standards engagement has long time horizons and should not be confused with product validation.
- Venture funding may create incentives that conflict with neutral stewardship of the standard.

## Explicitly deferred

Unless promoted through a deliberate decision, the first six months do not commit the project to:

- crawling or publishing billions of links;
- building a production-scale distributed graph;
- proving the truth of identity or equivalence claims;
- delivering a production browser, search engine, firewall or marketplace;
- finalising the star credential;
- selecting a permanent standards institution;
- solving AI alignment or internet governance generally; or
- deploying production infrastructure suitable for mass use.

These ideas remain legitimate parts of the project's ambition and Wishlist. The purpose of the roadmap is to create the smallest credible path by which they can be investigated.

## Updating this roadmap

Review this document at least monthly during the six-month horizon and whenever a major architectural or organisational decision is made.

Each review should ask:

1. What did we learn?
2. Which assumptions failed?
3. What has moved between Wishlist, Roadmap, Requirements and Specification?
4. Are the four project areas becoming clearer or more entangled?
5. Is the next milestone still the smallest credible step toward a public, testable Village Link standard?
