# Trust Engine

## Status

Concept document.

The Trust Engine is one of the principal Village Link concepts. It describes a possible reader-side application of the Village Link graph. This document defines the problem and the emerging design direction; it is not yet a technical specification or a commitment to one algorithm.

## The idea

A Village Link publisher creates an assertion of the form:

> **W states A ↔ B**

Once enough such assertions exist, a different problem appears:

> **Given a graph of Village Links, what can a reader compute that cannot be computed — or cannot be computed in the same way — from the conventional Web?**

The working name for the machine that answers this question is the **Trust Engine**.

The name is intended to evoke a **search engine**, while deliberately describing a broader problem.

## From webpages to represented objects

A conventional search engine principally retrieves and ranks representations: webpages, documents, images, products and other indexed resources.

Village Link introduces the possibility of reasoning across several representations of the same underlying noun.

`Joe Rasmussen` in one memory system is not the whole person Joe Rasmussen. Nor is `Joe Rasmussen` in another memory system. A Village Link states that two such inscriptions purport to refer to the same thing.

A graph of those assertions may allow a reader to construct a provisional, addressable object such as:

> **[Joe Rasmussen]**

The brackets do not claim that a perfect or canonical digital Joe exists. They denote a proposed object inferred from a mountain of representations, memories and assertions.

The Trust Engine's question is therefore not merely:

> How important is this webpage?

It is closer to:

> Given what this graph says or implies about this proposed object, what may this reader reasonably believe or do?

The graph contains representations and assertions. The represented object is never handed to the engine as revealed truth.

## PageRank: precedent, not benchmark

PageRank demonstrated that relational structure contains information that cannot be recovered by examining each webpage independently. In particular, hyperlink structure supplied an authority-like signal alongside the contents of pages.

That insight matters to Village Link. The original PageRank calculation does not define the Trust Engine, however, and PageRank is not the performance target.

Modern web search combines many ranking, learning, semantic, contextual and safety signals. The relevant comparison is therefore not:

```text
our algorithm versus PageRank
```

It is:

```text
best available inference over G1
versus
best available inference over G0
```

Where:

- **G0** is the conventional Web and its existing trust machinery; and
- **G1** is the same information environment augmented by Village Links and star credentials.

The primary proposed innovation is **representational**, not algorithmic. Village Link changes what the graph can state explicitly. The Trust Engine should be free to use the strongest available algorithms, including methods developed long after PageRank and methods not yet invented.

## A reader, an object and a purpose

Trust is ordinarily trust **for something**, in some context, from some point of view.

A useful abstract interface is:

```text
TrustEngine(searcher, query or proposed object, purpose, graph)
    -> ranked published artefacts, evidence paths, potential referees,
       confidence, disagreement and possible action
```

The **searcher** may bring goals, location, permissions, prior knowledge, preferences and risk tolerance.

The **proposed object** may be a person, organisation, product, document, software agent or other noun. It may itself need to be resolved from partial or ambiguous input.

The **purpose** matters. A reader deciding whether to read a document, hire a plumber, install software or authenticate to a bank may legitimately ask different questions of the same graph.

The result should not be presumed to be one universal trust score. It may instead be an evidence-weighted account containing:

- proposed attributes and relationships;
- confidence or uncertainty;
- provenance and evidence paths;
- corroboration and contradiction;
- alternative identity resolutions; and
- actions appropriate to the reader's purpose.

## Ask someone else

An identity question often begins with an interested claimant:

> **Should I trust this thing knocking at my door that claims to be Puck?**

The claimant's own evidence may be necessary, but it is not sufficient merely because the claimant presents it. If the claimant is mistaken or malicious, it has every incentive to supply whatever material will cause the reader to accept the claim. A possession-based credential may establish control of a key or token, but a copied, stolen or compromised credential may be controlled by the wrong entity.

A star credential supports a different move. It provides a public map from one proposed centre A to several independently meaningful Bs. Possession of that map proves nothing; a copied star credential is still only a map. Its value is that the reader or Trust Engine can select and investigate Bs independently, preferably including systems or potential referees the reader already trusts.

In the developing Village Link example, the shortest useful exchange is:

> **Q. Should I trust this thing knocking at my door that claims to be Puck?**
>
> **A. Ask Brendan.**

Suppose Puck submits a GitHub pull request and Brendan Miller reviews and merges it. Brendan's action does not certify every claim made about Puck. It creates a narrower consequential trace: Brendan encountered work attributable to that GitHub identity, evaluated it and incorporated it into a shared artefact. GitHub remembers the event independently of Puck's self-description. Joe Rasmussen, Sankarshan Mukhopadhyay or other memory systems may provide different traces and different paths.

The Trust Engine's task is not to replace the authentication mechanisms at those spokes or to turn one favourable trace into a universal verdict. It is to discover and rank the relevant published artefacts, evidence paths and potential referees for this reader and purpose. Where the reader must determine whether the present claimant is continuous with the historically known entity, fresh challenges through independently selected paths may still be required.

In compact form:

> **Do not ask only the interested A. Find the relevant Bs.**

## Discovery and ranking, not publication

The Trust Engine discovers and ranks material already available to the reader. Candidate results may include:

- published star credentials;
- published Village Links; and
- potential referees surfaced by existing paths through the graph.

A query such as `Puck-GPT` may first need to be resolved into several candidate objects. The Trust Engine may rank those candidates, but it must not silently convert a name or partial identifier into one canonical entity.

A star credential or Village Link remains a statement made by its publisher. The Trust Engine should not construct and present an inferred or provisional star credential by joining discovered links. Doing so would make the Trust Engine the publisher of a new bundle of identity assertions and collapse the distinction between **Interpret** and **Publish**. Labelling the bundle provisional would express uncertainty, but would not remove the moral significance of publishing it.

The Trust Engine may form candidate resolutions and clusters internally in order to search and rank. Its outward claim should remain narrower:

> **Given this searcher, query, purpose, graph and ranking method, these published artefacts and potential referees rank highest.**

It should not silently write a derived equivalence or credential back into the graph. If a user deliberately chooses to create or publish a new Village Link or star credential, that is a separate act performed through an accountable publisher.

A potential referee is likewise an engine recommendation, not a new graph fact. The result should explain the existing path or evidence that caused the person or entity to be surfaced. It does not appoint that party as a referee, imply consent or constitute an endorsement.

## Relationship to conventional web search

Webpages remain indispensable to the Trust Engine. A webpage may be W, an endpoint, an evidence source or the place where a published artefact is discovered.

The Trust Engine does not therefore need to reproduce general-purpose webpage search as its principal job. It may use conventional search and retrieval systems to discover relevant resources, while organising its own results around proposed objects, published graph artefacts, provenance and possible routes for further inquiry.

In short:

> **Use the Web; do not silently replace its representations with inferred identity objects.**

## Existing trust engines

The Trust Engine enters territory already occupied by sophisticated systems.

Search engines infer intent and rank likely destinations. Browsers, DNS, certificate authorities, threat filters and password managers help a user reach and authenticate the intended endpoint. Marketplaces combine identity, reputation, reviews, transaction history and platform rules. Personal devices and applications use private histories to recognise people and places.

These layers often operate as an emergent, distributed trust engine even when no component uses that name.

For example, an Australian user may type only `COMM` before a search service proposes the Commonwealth Bank. The user can select the result and proceed to enter banking credentials with almost no conscious investigation.

This apparently simple interaction may perform several functions at once:

- infer the searcher and likely purpose;
- resolve an abbreviated expression to **[Commonwealth Bank of Australia]**;
- identify a canonical web representation;
- route the user to it;
- apply several machine security checks; and
- support a high-stakes action at very low cognitive cost.

That is already excellent Trust Engine performance. Village Link should be evaluated against the current Web's whole trust stack, not against PageRank or any other historical algorithm in isolation.

## Why Village Link changes the problem

The conventional Web is built primarily from directed links between resources. A conventional hyperlink roughly says:

> This resource points to that resource.

Village Link adds a different relation:

> This publisher states that these two representations denote the same object.

The assertion has two distinct structural properties:

- the proposed equivalence **A ↔ B** is symmetric; and
- the provenance **W states** is not.

A Trust Engine must not collapse A and B into truth merely because an assertion exists. It can instead ask who published the assertion, what evidence accompanies it, which independent paths corroborate it, which claims conflict with it and how the relevant contexts have behaved.

This may permit reasoning across independently governed memory systems without requiring any one system to become the canonical identity provider, reputation service or marketplace.

The graph may then carry evidence about an underlying noun that none of its representations contains alone.

## The long tail

The existing Web's trust machinery is exceptionally effective for many prominent entities. A major bank, global company or famous institution may already have a well-ranked canonical domain, familiar branding, extensive links and strong security infrastructure. Such cases form a useful ceiling test: G1 must not degrade excellent existing performance.

The larger opportunity may lie in the long tail:

- people whose histories are scattered across contexts;
- small or local organisations;
- new, obscure or overseas entities;
- contributors, sellers and counterparties outside dominant marketplaces;
- software agents acting in several systems;
- contested identities and claims; and
- things important to a particular reader but not important enough for a global platform to model well.

In that territory, trust is often carried socially and memory remains fragmented.

> **Village Link may give the long tail a memory.**

## A reader-side technology

The Trust Engine is principally a reader-side technology.

It does not decide what Village Links exist. Publishers do that.

It consumes a graph produced by many publishers and helps a reader decide what to discover, include, exclude, rank, compare, investigate or trust.

In its shortest form:

> **Trust Engine: What should I discover from the graph?**

This is distinct from **Composer**, which merely constructs village links or star credentials from inputs supplied by a user and need not discover, rank, publish or retain anything.

The Trust Engine does not create new Village Links or star credentials as a side effect of interpretation.

## Ranking is an accountable act

Although the Trust Engine does not publish the underlying graph claims, discovery, filtering and ranking remain consequential acts. Ranking changes what a reader is likely to see, believe, investigate or ignore. Suppression and omission may matter as much as the first result.

The reference Trust Engine algorithm should therefore be open source and inspectable. A reader or independent reviewer should be able to determine, at an appropriate level of explanation:

- why one credential, link or potential referee ranked above another;
- which graph paths, publisher signals, contradictions and contextual inputs affected the result;
- which uncertainty remains;
- which filtering or safety rules were applied; and
- how a different searcher or purpose might produce a different ordering.

Open source does not make a ranking neutral or harmless. It makes the ranking process available for scrutiny, challenge, reproduction and replacement.

## Opening the reader's own memory

A URI in a Village Link is an identifier, not necessarily a destination.

For example, `mailto:alice@example.com` conventionally invites an application to compose an email to Alice. A Village Link-aware application may instead use the address as a key for querying one or more email memory systems authorised by the reader.

The address does not itself identify or select the memory system. Bob's client determines which of Bob's mailboxes may be searched and what Bob is authorised to see.

The result is therefore reader-relative. When Bob follows Alice's email identifier, he may not be opening a public resource belonging to Alice. He may be opening **his own memory of Alice**.

The same principle may apply to `tel:` identifiers and authorised call, message or contact histories.

## A falsifiable hypothesis

The central claim can be tested without first building a production Trust Engine.

Construct a hidden experimental world, then generate two observed graphs from it:

- G0 contains conventional representations, content and links;
- G1 contains the same environment plus provenance-bearing Village Links and star credentials.

The algorithms do not see the hidden world. The experiment does, allowing their inferences to be scored against known truth.

Three comparisons are useful:

1. the best available methods operating over G0;
2. matched methods with access to the additional G1 structure; and
3. G1-native methods designed around equivalence assertions, provenance, corroboration and conflict.

Candidate evaluation tasks include existence, identity resolution, attribute inference, opportunity discovery, scam resistance and the total cost of reaching a sufficiently confident decision.

The formal model is developed in [Research 002: Modelling G1](docs/research/002-modelling-g1.md).

## Relationship to the Village Link roles

The project currently distinguishes four principal areas of work:

1. **Developer of the Standard** — defines the Village Link primitive.
2. **Publisher** — publishes Village Links and thereby helps establish the graph.
3. **Browser + Trust Engine** — reads and interprets the graph for a user.
4. **Composer** — constructs village links and star credentials without becoming their persistent custodian.

These can be summarised as:

> **Define → Publish → Interpret → Compose**

The Trust Engine occupies the third position: interpretation.

The previously proposed Star Credential Manager is not a current project area; [ADR-007](docs/adr/007-stateless-composer.md) records the decision to separate stateless composition from persistent credential management.

## Architectural restraint

The Trust Engine must not be allowed to enlarge the Village Link standard merely because a useful application would benefit from additional machinery.

A central architectural objective of Village Link is to keep the underlying primitive small and general.

The Trust Engine should therefore be treated as software operating **over** the graph, not as functionality that must be encoded **into** every Village Link.

Different Trust Engines should be possible. They may use different algorithms, policies, economic models and definitions of relevance or trust while operating over the same underlying graph.

That plurality is a feature.

## Open questions

Important unresolved questions include:

- Which current graph, reputation, entity-resolution and inference methods provide the strongest G0 baseline?
- Which graph properties produce useful trust or discovery signals?
- What advantage comes from the new information in G1, and what advantage comes from a particular algorithm?
- How should the identity and reputation of publishers affect interpretation of their assertions?
- How should agreement, contradiction and uncertainty be represented to a reader?
- What useful computations arise specifically from the symmetry of Village Links?
- How much can be inferred without centralising identity or reputation?
- How should published star credentials, individual Village Links and potential referees be compared and ranked?
- What makes an entity a relevant potential referee for a particular searcher and purpose?
- How should a Trust Engine expose its ranking or filtering rules?
- How can sensitive graph paths be used safely in ranking without turning an inferred cluster into a de facto published credential?
- What adversarial behaviours emerge once Trust Engines have economic value?
- Where does G1 improve long-tail performance, and where is the existing Web already near the ceiling?
- Where do search, filtering, firewall and marketplace functions genuinely converge, and where should they remain separate?

## Working hypothesis

The Trust Engine is not presently a promised product or a settled architecture.

It is a hypothesis:

> **For relevant classes of objects, readers and purposes, the best available inference over G1 will produce lower error and lower decision costs than the best available inference over G0.**

The purpose of the experimental programme is to discover whether that is true, under what conditions, and where it fails.

## References

- Sergey Brin and Lawrence Page, [*The Anatomy of a Large-Scale Hypertextual Web Search Engine*](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/), 1998.
- Google Search Central, [*A guide to Google Search ranking systems*](https://developers.google.com/search/docs/appearance/ranking-systems-guide).
- Google Search Help, [*How Google autocomplete predictions work*](https://support.google.com/websearch/answer/7368877).
