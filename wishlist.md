# Village Link Wishlist

Ideas, experiments, questions and possible things to build.

**Nothing in this document is a commitment.** Items move into the roadmap only when we deliberately decide to pursue them.

## [#1 — Pathway to relevance](docs/responses/01-pathway-to-relevance.md)

- [ ] **As the primary promoter of the project, Joe should have at his disposal our best efforts at a succinct, compelling set of elevator-pitch answers to the question: _"What is the pathway to relevance for this technology?"_** He should be able to produce those answers at a moment's notice, without fumbling, retreating into abstraction, or escaping into interesting but secondary ideas.
- [ ] Treat this explicitly as a **marketing capability** the project must build, not merely as an architectural or philosophical question.
- [ ] Develop versions of the answer for different levels of available attention: one sentence, 30 seconds, two minutes, and a deeper discussion.
- [ ] Treat this as a scaling problem, not merely a statement of public benefit: **How do we get 100 people interested and involved? 1,000? 100,000? 10,000,000?**
- [ ] Identify what motivates participation at each scale. The reasons the first 100 or 1,000 people care may be very different from the reasons a million people use the technology.
- [ ] In particular, explore the bridge between **public-good motivation** and **tangible private advantage**. AI alignment, governance, provenance and healthier public infrastructure may be capable of attracting an early community; mass adoption probably requires Village Link to solve concrete problems for individual people, organisations or products.
- [ ] Look for the case-by-case opportunities through which Village Link could spread in a massively contested attention environment: situations where adopting or creating a Village Link produces an immediate benefit for the adopter, without requiring the rest of the world to adopt first.
- [ ] Revisit our existing documents and conversations and assemble the strongest pathways to relevance we have proposed so far, including identity/reputation portability, search and discovery, third-party verification, provenance, AI/alignment applications, marketplaces, and the possibility that the more general **double-headed hyperlink** has useful applications beyond Village Link itself.
- [ ] Turn this eventually into a plausible adoption ladder: early collaborators → useful niche → repeatable private advantage → network effects → large-scale relevance.

## Data and examples

- [ ] Define a manageable, low-risk subset of Wikipedia and Wikidata from which to derive initial entity pages and equivalence assertions.
- [ ] Record the source, evidence, publisher and observation time for imported assertions without treating those fields as part of the core primitive.
- [ ] Begin with public institutional entities, software agents and clearly labelled mock examples; avoid unnecessary correlation of ordinary people's identities.
- [ ] Retain selected Steve Byrnes, Joe Rasmussen and Puck examples where they exercise a distinct technical case.
- [ ] Construct small triangles, contradictions, stale identifiers and ambiguous cases to test interpretation rather than presenting only clean equivalences.

## Architecture and standards

- [ ] Return to Brendan Miller's email and test his assertion that the objects we need already exist within DTG.
- [ ] Have a focused architectural discussion about the **star credential**, similar to the discussion that produced the current Village Link primitive.
- [ ] Untangle the relationship between the Village Link primitive and the star credential: the star credential may now be *one important thing built using the primitive*, rather than the primitive itself.
- [ ] Do a focused piece of thinking on whether what we have really developed is the **double-headed hyperlink**, with Village Link as just one instance of what can be built using that more general primitive.
- [ ] Work through the architecture far enough to create some actual star credentials.
- [ ] Investigate whether a **star credential ceremony** needs to be specified by Village Link, substantially demonstrated by us, or deliberately left to adopting systems.
- [ ] Explore the implications of the double-headed hyperlink for search, filtering and ranking.
- [ ] Explore the implications of the primitive for marketplaces and reputation portability.

## Demo

- [ ] Explore a Village Link browser as the centrepiece of the demo.
- [ ] Make ordinary hyperlinks behave conventionally.
- [ ] When the browser encounters a Village Link, display a split-screen view showing the two endpoints encapsulated by the link, left and right.
- [ ] Demonstrate third-party verification using small triangles of linked entities.
- [ ] Consider whether search/filter behaviour can be demonstrated without allowing it to blow out the scope of the first demo.
- [ ] Eventually explore a marketplace demonstration showing what portable, cross-system identity/reputation could do to incumbent marketplace models.

## Near-term implementation

- [ ] Settle a prototype URI syntax, including escaping, reserved characters, round-trip parsing and comparison rules.
- [ ] Install the reference MediaWiki on the available server.
- [ ] Define the first entity-page and star-credential representation.
- [ ] Build and document a controlled Wikipedia/Wikidata import process.
- [ ] Populate the MediaWiki with the initial sandbox corpus.
- [ ] Update the prototype browser to resolve Village Links through the MediaWiki and display both endpoints.
- [ ] Use the working graph to investigate the first Trust Engine computations.
- [ ] Build the first stateless **Composer** for constructing village links and machine-readable star credentials without retaining user inputs or outputs.

## People and discovery

- [ ] Search systematically for more people like Steve Byrnes: people who have effectively cobbled together their own star credential.
- [ ] Particularly look for people who are:
  - technically literate;
  - maintaining identities across several systems;
  - interested in provenance, reputation, identity or trust;
  - concerned about AI/alignment/governance.
- [ ] Explore whether this population could provide Village Link's first collaborators, users and champions.
- [ ] Think about a deliberate outreach experiment — perhaps finding ~100 plausible "Byrneses" and seeing who actually responds to the idea.

## Wild ambitions

- [ ] Dare to think seriously about what a double-headed hyperlink does to search.
- [ ] Dare to think seriously about what portable cross-system reputation does to marketplaces.
- [ ] Ask whether Village Link could enable alternatives to the vertically integrated trust/reputation systems of Amazon, eBay, Uber, Facebook Marketplace and others.
- [ ] Keep these ideas alive **without allowing them to contaminate the scope of the first implementation.**

---

## Promotion rule

An unchecked item in this document means only:

> **This seems interesting enough that we don't want to forget it.**

It does **not** mean:

> We have decided to do this.

When we consciously decide that an item should actually be done, it can graduate into the roadmap.
