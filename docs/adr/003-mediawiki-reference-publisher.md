# ADR-003: Implement the reference publisher as a MediaWiki

**Status:** Accepted  
**Date:** 28 August 2026

## Context

Village Link publishers publish collections of Village Links. Publication creates the possibility of harm: a publisher may publish mistaken, misleading or malicious equivalence assertions; evidence may change; assertions may become outdated; and aggregation itself may expose information about people or other entities in harmful ways.

The Village Link project should not attempt to invent from first principles the governance of a large, collaboratively maintained public information system.

Wikipedia and the wider Wikimedia movement have accumulated approximately twenty-five years of software, institutions, policies, norms and practical experience addressing closely related problems: open contribution, provenance, vandalism, bots, edit conflicts, dispute resolution, page protection, deletion, notability, disambiguation, verification, contributor behaviour and the treatment of information about living people.

MediaWiki embodies much of the technical machinery supporting that governance: revision histories, talk pages, user accounts, permissions, watchlists, recent changes, bots, redirects, disambiguation mechanisms, page protection and administrative tools.

The opportunity is therefore stronger than using Wikipedia merely as inspiration. The reference publisher can be built directly as a MediaWiki and can inherit Wikimedia governance practices by default.

## Decision

The reference Village Link publisher will be implemented as a **MediaWiki**.

Its fundamental organisational rule will be:

**one noun, one page.**

A page represents an entity. Its principal content is that entity's **star credential**: a collection of Village Link assertions connecting representations of the same entity across different contexts.

Conceptually, a page headed:

`Ford Motor Company`

might contain assertions equivalent to:

`Ford Motor Company = [Ford identity in Instagram]`

`Ford Motor Company = [Ford identity in Facebook]`

`Ford Motor Company = [Ford legal entity in a government registry]`

and so on.

The page is therefore not primarily an encyclopaedic article about the entity. It is a human-governed publication surface for the entity's star credential.

## Entity pages and Link pages

The reference publisher may provide two complementary views of the same Village Link graph.

An **Entity page** is a node-centred view. It presents the star credential formed by published Village Links involving that entity.

A **Link page** is an edge-centred view. It presents one Village Link assertion together with material surrounding that assertion, which may include evidence, provenance, revision history, discussion and other publication metadata.

An Entity page should therefore be understood principally as a **projection of published Link assertions**, rather than as an independently maintained credential document.

In concise form:

> **An Entity page is a node-centred projection of the graph; a Link page is an edge-centred projection of the same graph.**

This distinction keeps the publication model close to the Village Link primitive. Editors may add, remove, challenge, correct or qualify individual equivalence assertions, while the star credential presented on an Entity page can be assembled from those governed assertions.

The Link page is also the natural place for evidence supporting or challenging an edge. MediaWiki's revision history, discussion and governance machinery can therefore apply directly to the assertion itself rather than only to an aggregate entity page.

## Dereferencing Village Links

ADR-001 does not require a Village Link URI to dereference. That remains unchanged.

A publisher may nevertheless choose to make a Village Link URI dereference to a human- or machine-readable representation of the assertion. In the reference MediaWiki publisher, that representation may be the corresponding Link page.

This is a publication-layer convenience, not an enlargement of the Village Link primitive. The canonical Village Link remains the identifier of the assertion; the MediaWiki page is a representation supplied by a particular publisher.

The reference implementation need not use the literal Village Link URI as a MediaWiki page title. It may map canonical Village Link URIs to internal Link-page identifiers where this is more practical.

## Publication and authority

Village Link does not define an ultimate repository of truth.

Publication is assertion. When a Village Link is published, the assertion exists. People, agents and consuming systems decide what weight to give it according to its publisher, evidence, provenance, corroboration, contradiction and the larger graph in which it appears.

A successful Wikimedia-governed Village Link publisher may become a highly trusted publisher. That is desirable rather than architecturally problematic. Village Link's role is to make assertions and their provenance legible; it does not prescribe how much epistemic authority a consumer should assign to any publisher.

MediaWiki's support for third-party verification, citation, revision history and dispute is therefore directly useful to the quality and weight of the resulting graph.

## Wikimedia governance by default

The reference publisher will inherit Wikimedia governance practices **by default**, rather than merely treating them as examples from which to design a new governance system.

Relevant inherited practices include mechanisms and norms concerning:

- open contribution;
- revision history and provenance;
- reversibility;
- talk pages and dispute resolution;
- vandalism and spam;
- bots and bot governance;
- page protection and administrative powers;
- redirects and disambiguation;
- verification and sourcing;
- notability and inclusion;
- deletion and suppression;
- contributor conduct, including principles such as being bold and assuming good faith; and
- heightened care around information concerning living people.

Not every Wikimedia rule will map unchanged to Village Link. Some exist because Wikipedia is specifically an encyclopaedia. The governing principle is therefore:

> **Inherit Wikimedia governance by default. Depart only where the different nature of Village Link requires it, and document the departure.**

This is particularly important for harms mitigation. The fact that an identity can technically be discovered and linked does not imply that it should be aggregated into a public star credential. Wikimedia's long-developed distinctions around notability, privacy, sourcing and living people provide a starting governance framework for deciding what belongs in a public memory system.

## Human governance and human or machine consumption

Village Link entity pages may be useful to human readers as well as machines.

Unlike a Wikipedia article, an Entity page is not principally intended to provide a narrative account of its subject. Its principal function is to expose a structured, governed set of identity assertions. That need not make the page visually uninteresting: implementations may present the rays of a star credential alongside recognisable representations, previews or other useful views of their target resources.

The page and its history provide a surface through which humans can add evidence, correct errors, challenge assertions, revert vandalism and govern the graph. Link pages allow that governance to be focused on individual assertions. Talk pages provide a natural location for the human discussion surrounding those decisions.

The resulting star credentials are also expected to be useful to machine consumers, including AI agents and systems such as a future Village Link Trust Engine.

## Disambiguation and entity boundaries

MediaWiki's mature treatment of naming, redirects and disambiguation is particularly valuable to Village Link.

A string such as `Ford` need not be prematurely collapsed into a single entity. It may instead lead to distinct entity pages such as Ford Motor Company, Gerald Ford or other entities represented by the same name.

Disambiguation therefore becomes part of graph governance: a mechanism for preventing ambiguous names from causing false identity equivalence.

Similarly, redirects and aliases can express naming choices without requiring duplicate star credentials for the same entity.

## One multilingual instance

The reference Village Link publisher will intentionally depart from Wikipedia's architecture of separate wiki instances for different languages.

Village Link treats representations in different languages as representations of entities in different contexts. Language therefore does not require duplication of the underlying entity or star credential.

Conceptually:

`(Entity A in German context) = (Entity B in Chinese context)`

may itself be expressed through Village Links.

The reference publisher should therefore aim to operate as **one multilingual MediaWiki instance**, with language-specific names and representations connected through the same underlying graph.

The practical implications for canonical page names, aliases, scripts, search, localisation and culturally contested entity boundaries remain implementation questions.

## Wikimedia identity interoperability

Compatibility with existing Wikimedia contributor identity is a design objective.

Where technically and institutionally possible, existing Wikimedia logins should ultimately be usable with the Village Link MediaWiki. The project should avoid unnecessary identity or governance architecture that would make future integration with the Wikimedia ecosystem harder.

This objective does not assume access to Wikimedia Foundation authentication infrastructure or imply present endorsement by the Foundation.

## Bootstrapping the graph

Wikipedia and Wikidata are natural candidate sources for seeding the Village Link graph.

The world's Wikipedias already embody a vast body of human-curated decisions about nouns, naming, disambiguation, sources and links to external resources. Wikidata contains structured entity identifiers and mappings to many external identifier systems.

The reference implementation should investigate how these resources can be mined or imported, subject to their licences, provenance requirements and the need to preserve the distinction between source assertions and Village Link publication.

Particular attention should be given to the relationship between Village Link and Wikidata so that existing capabilities are reused rather than unnecessarily duplicated.

## Long-term Wikimedia Foundation adoption

The long-term aspiration for the reference publisher is:

1. build it as a MediaWiki;
2. establish useful standing, content and community in the world; and
3. if warranted by that experience, seek adoption as a Wikimedia Foundation project and integration into Wikimedia governance and infrastructure.

This is an aspiration, not an assumption or dependency. No present endorsement or future adoption by the Wikimedia Foundation is implied.

Design choices should nevertheless favour compatibility with that possible future rather than creating gratuitous technical or institutional divergence from Wikimedia practice.

## Consequences

This decision substantially narrows the implementation space for the reference publisher. It deliberately trades freedom to invent a bespoke publication platform for access to a mature technical and governance ecosystem.

It also makes governance part of the implementation architecture rather than an external policy document added later.

Important work remains, including:

- defining the exact representation of Entity pages and Link pages within MediaWiki;
- determining how Village Link assertions, evidence and provenance are stored and exposed to human and machine consumers;
- defining the mapping between canonical Village Link URIs and optional dereferenceable Link-page representations;
- investigating Wikidata overlap and interoperability;
- designing multilingual naming and search;
- determining which Wikimedia policies transfer unchanged and documenting necessary departures;
- designing import and bot processes for graph bootstrapping;
- considering privacy, deletion, suppression and persistent history in the context of identity aggregation; and
- defining interfaces through which AI agents and the future Trust Engine consume the graph.

These are implementation and governance questions arising from the decision. They do not alter the architectural choice recorded here.

## Relationship to ADR-001, ADR-002 and ADR-007

ADR-001 defines Village Link as a self-contained, two-ended hyperlink.

ADR-002 restricts the primitive to equivalence between representations of the same entity.

This ADR defines the reference Publisher architecture around that deliberately small primitive.

ADR-007 subsequently replaced the proposed persistent Star Credential Manager role with a stateless Composer. The current project is therefore organised into four principal components:

1. **Standard** — defines the Village Link primitive;
2. **Publisher** — publishes and governs collections of Village Links;
3. **Browser + Trust Engine** — consumes and interprets the resulting graph; and
4. **Composer** — constructs village links and star credentials without becoming their persistent custodian.

MediaWiki does not enlarge the Standard. It provides a mature human governance environment around publication.
