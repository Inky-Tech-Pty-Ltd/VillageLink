# Village Link Wishlist

Ideas, experiments, questions and possible things to build.

**Nothing in this document is a commitment.** Items move into the roadmap only when we deliberately decide to pursue them.

## Data and examples

- [ ] Create a simple Village Link database, initially one table, containing at least:
  - Village Link
  - source
  - date/time the source was sampled
- [ ] Populate it with the examples from Steve Byrnes's home page.
- [ ] Add Joe Rasmussen examples.
- [ ] Add the Puck example.
- [ ] Create some mock entities backed, where useful, by real accounts on existing systems.
- [ ] Construct one or more small triangles between entities to explore/demonstrate third-party verification.

## Architecture and standards

- [ ] Return to Brendan Miller's email and test his assertion that the objects we need already exist within DTG.
- [ ] Have a focused architectural discussion about the **star credential**, similar to the discussion that produced the current Village Link primitive.
- [ ] Untangle the relationship between the Village Link primitive and the star credential: the star credential may now be *one important thing built using the primitive*, rather than the primitive itself.
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

## Infrastructure

- [ ] Examine the existing cPanel/Linux VM environment.
- [ ] Determine whether it is sufficient to host the early database and browser application.
- [ ] Decide what additional infrastructure, if any, the first working demo actually requires.

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
