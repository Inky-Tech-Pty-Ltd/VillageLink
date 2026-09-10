# Research 002: Modelling G1

## Status

Research proposal. The notation and experimental design are provisional.

## Purpose

This note defines a testable model for the central Trust Engine hypothesis:

> **Does adding Village Links and star credentials to an information environment enable better inference about represented objects?**

The object of comparison is not PageRank. PageRank is an important precedent for extracting information from relational structure, but modern search and trust systems use much richer methods.

The intended comparison is between the strongest available performance over:

- **G0** — the conventional Web and its existing trust machinery; and
- **G1** — the same environment augmented by Village Links and star credentials.

The experiment must distinguish the value of the added representation from the value of any particular algorithm.

## 1. A hidden world

Let the experimental world be:

\[
\Omega = \{o_1, o_2, \ldots, o_n\}
\]

Each \(o_i\) is a simulated underlying object: a person, organisation, product, document, software agent or other noun.

For experimental purposes, each object may have hidden properties:

\[
\theta(o_i) =
\{\text{existence},\text{type},\text{attributes},\text{relationships},\text{history}\}
\]

The simulation knows \(\Omega\) and \(\theta\). Algorithms under test do not.

This hidden layer does not assert that perfect knowledge of real objects is available in the actual world. It supplies ground truth only so that experimental errors can be measured.

## 2. Representations

Let \(R\) be a set of observed representations distributed across contexts:

\[
R = \{r_1, r_2, \ldots, r_m\}
\]

A hidden mapping records which underlying object, if any, each representation denotes:

\[
\pi : R \rightarrow \Omega \cup \{\varnothing\}
\]

The value \(\varnothing\) permits fabricated, invalid or unresolvable representations.

One object may have many representations. A representation may be stale, inaccurate, ambiguous or fraudulent. The engine sees the representation and its observable contents, not \(\pi\).

Examples include:

- an account in a social or software system;
- a company or professional record;
- an email address or telephone number;
- a wiki page;
- a marketplace identity;
- a conference biography; or
- a page mentioning an object without being controlled by it.

## 3. G0: the conventional information environment

Let:

\[
G_0 = (V_0, E_0, X_0)
\]

where:

- \(V_0\) contains representations, pages, contexts and other observable resources;
- \(E_0\) contains conventional hyperlinks and any other relationships available to the baseline system; and
- \(X_0\) contains observable content and metadata.

G0 should be interpreted broadly. It is not a caricature of the 1998 Web. A credible baseline may use modern search, entity resolution, knowledge graphs, content models, threat intelligence, browser protections and reader history where those inputs are legitimately available.

G0 may already perform exceptionally well for prominent and strongly defended entities.

## 4. G1: the augmented environment

G1 begins with the same hidden world and the same observable G0 environment:

\[
G_1 = G_0 \cup L \cup H
\]

where:

- \(L\) is a set of Village Link assertions; and
- \(H\) is a set of star credentials.

### 4.1 Village Link assertions

A Village Link is best represented in the experimental graph as an assertion node:

\[
\ell = (w, \{a,b\}, t, e)
\]

where:

- \(w\) is the publishing resource or context;
- \(\{a,b\}\) is an unordered pair of endpoint identifiers;
- \(t\) is relevant temporal information; and
- \(e\) is optional evidence or metadata available at the publishing resource.

This preserves a crucial distinction:

- **A ↔ B is symmetric.** The assertion has no privileged endpoint direction.
- **W states is asymmetric.** Responsibility and provenance flow from the publisher to the assertion.

The hidden world records whether \(\pi(a)=\pi(b)\). The observed graph records only that W made the assertion.

An algorithm that automatically collapses A and B has confused assertion with truth and should be expected to fail under noise or attack.

### 4.2 Star credentials

A star credential can be represented as a hyperedge or, in an ordinary graph implementation, as a credential node connected to its center and unordered arms:

\[
h = (w, a, \{b_1,b_2,\ldots,b_k\}, t, e)
\]

The center \(a\) has its conventional role in the credential syntax. The set of arms is unordered. Provenance, signature, evidence and lifecycle information remain properties of the credential or its publication context rather than proof that the endpoints are equivalent.

## 5. The Trust Engine task

Let a reader or searcher be described by:

\[
S = \{g, l, p, k, \rho\}
\]

where the components may represent goals, location, permissions, prior knowledge and risk tolerance.

Let \(q\) be an input that proposes or seeks an object, and let \(u\) be the reader's purpose.

A general Trust Engine can then be written:

\[
T(S,q,u,G) \rightarrow B
\]

where \(B\) is a belief or decision state that may contain:

- one or more proposed underlying objects;
- inferred attributes and relationships;
- confidence and uncertainty;
- provenance and evidence paths;
- corroboration and disagreement; and
- a recommended action or ranked set of possibilities.

The proposed object need not be fully specified at input. Resolving `COMM` to **[Commonwealth Bank of Australia]** may itself be part of the task.

## 6. Generating paired graphs

Each experimental run should generate G0 and G1 from exactly the same \(\Omega\).

A generator may vary:

1. the number and types of underlying objects;
2. the number of contexts in which each object appears;
3. the number, age and accuracy of representations;
4. conventional content and hyperlink structure;
5. publisher competence, honesty and independence;
6. the probability that a publisher creates an assertion;
7. the probability that an assertion is true, mistaken, stale or malicious;
8. correlation between apparently separate claims;
9. what private memory is authorised for a particular reader; and
10. the costs and harms attached to decisions.

G0 and G1 must differ only by controlled additions. Their paired origin allows an observed performance change to be attributed to the additional G1 information rather than to an easier simulated world.

## 7. Comparisons

Three levels of comparison are required.

### 7.1 Current-frontier G0

Establish the strongest credible baseline available from G0. A weak historical baseline would exaggerate Village Link's value.

### 7.2 Matched augmentation

Where possible, provide substantially the same inference pipeline with and without G1 features. This is an ablation test of the information added by Village Link.

### 7.3 G1-native methods

Test methods designed to exploit symmetric equivalence assertions, asymmetric provenance, publisher history, independent paths, contradiction and credential structure.

This separates two discoveries:

- Village Link adds useful information; and
- a particular algorithm extracts that information well.

The first is the foundational claim. The second is replaceable engineering.

## 8. Loss and performance

For a task instance \((S,q,u)\), define a loss function comparing the engine's result with the hidden world:

\[
\mathcal{L}(T(S,q,u,G), \Omega)
\]

The principal hypothesis is:

\[
\mathbb{E}[\mathcal{L}(T^*_1(S,q,u,G_1),\Omega)]
<
\mathbb{E}[\mathcal{L}(T^*_0(S,q,u,G_0),\Omega)]
\]

for at least some important classes of objects, readers, purposes and information environments, where \(T^*_0\) and \(T^*_1\) denote the strongest credible methods available for their respective graphs.

The qualification matters. G1 need not improve every task or every part of the distribution.

## 9. Evaluation tasks

### 9.1 Existence

Does the proposed object exist, or is it fabricated, duplicated, synthetic or insufficiently supported?

Candidate measures include classification error, precision and recall, Brier score and confidence calibration.

### 9.2 Identity resolution

Which representations refer to the same underlying object?

Measure false mergers, false splits, pairwise precision and recall, and cluster-level measures such as B-cubed or adjusted Rand index where appropriate.

### 9.3 Attribute and relationship inference

What can reasonably be said about the proposed object?

Measure correctness, calibration, provenance recovery, contradiction detection and the engine's willingness to abstain when evidence is inadequate.

### 9.4 Opportunity discovery

Given a particular reader and purpose, which objects, relationships or actions should become visible?

Measure recall of suitable opportunities, ranking quality and realised reader utility. This task is necessarily reader-relative.

### 9.5 Trusted action and transaction cost

How much effort, time, money and risk does the reader incur before reaching an adequately confident decision?

A combined cost may include:

- queries and keystrokes;
- resources inspected;
- identities manually reconciled;
- verification fees or delays;
- false leads;
- losses caused by fraud or mistaken identity; and
- legitimate transactions declined because confidence could not be established.

Scam resistance is an important special case of reducing risk-adjusted transaction costs.

## 10. Head and tail cases

The evaluation set should deliberately contain both head and tail cases.

### Head or ceiling cases

Prominent banks, companies and institutions may already be resolved and protected extremely well by G0. For example:

```text
Searcher: Australian bank customer
Input: COMM
Likely object: [Commonwealth Bank of Australia]
Purpose: authenticate to my bank
Successful outcome: correct official endpoint with negligible friction
```

Such cases test whether G1 avoids degrading excellent existing performance.

### Long-tail cases

These should include people, small organisations, new entities, cross-border counterparties, marketplace identities, contributors and software agents whose memories are fragmented across contexts.

The hypothesis is not merely that G1 adds another signal to already famous objects. It may make otherwise disconnected long-tail memory traversable.

## 11. Adversarial conditions

The generator should include at least:

- a mistaken but honest publisher;
- one publisher creating many false assertions;
- colluding publishers;
- copied claims that appear to be independent corroboration;
- identity hijacking;
- stale or transferred identifiers;
- compromised credentials;
- one false bridge joining two otherwise correct identity clusters;
- honest disagreement; and
- selective disclosure by an interested object.

The aim is not to assume that graph structure is reputationally valuable. It is to discover when it is valuable and how that value breaks.

## 12. Ablations and upper bounds

Useful experimental variants include:

- G0 with no Village Links;
- G1 with perfectly accurate assertions, as an information upper bound;
- noisy G1;
- G1 with publisher provenance removed;
- G1 with endpoint symmetry ignored;
- pairwise Village Links without star credentials;
- star credentials expanded into independent pairs;
- public information only;
- public information plus authorised reader memory; and
- varying degrees of publisher independence and adversarial coordination.

These tests should reveal which structural properties produce any measured advantage.

## 13. Candidate algorithm families

No algorithm family is selected by this note. Candidates for investigation include:

- contemporary entity-resolution and record-linkage methods;
- probabilistic graphical models and belief propagation;
- signed, temporal or provenance-aware graph methods;
- personalised graph ranking;
- graph representation learning;
- neural retrieval and learned ranking using graph features; and
- transparent rule-based methods as interpretable baselines.

Ordinary PageRank may be included as a historical or sanity-check baseline. It should not stand in for the strongest methods available over G0.

## 14. Minimal executable experiment

The first implementation need not model the whole Web.

A useful minimum would:

1. generate a reproducible hidden world from a random seed;
2. emit paired G0 and G1 datasets;
3. include honest, mistaken and adversarial publishers;
4. run at least one simple identity baseline and one provenance-aware method;
5. score existence and identity resolution against \(\Omega\);
6. record decision cost for a small set of purposes; and
7. produce enough diagnostic output to explain individual successes and failures.

The simulator should keep world generation, graph serialization, algorithms and scoring separate so that each can be replaced independently.

## 15. What would count as failure?

The model is useful only if it can hurt the hypothesis.

Material negative findings would include:

- modern G0 methods recover nearly all useful information without Village Links;
- realistic Village Link noise overwhelms their additional signal;
- provenance cannot adequately distinguish independent evidence from coordinated assertion;
- G1 improves average accuracy while increasing severe tail risks;
- benefits occur only when a central authority supplies the truth the architecture sought to avoid; or
- publication and privacy costs exceed the reduction in transaction costs.

Partial or domain-specific success is also possible. G1 may help some long-tail identity and discovery tasks while adding little to prominent, well-organised entities.

## 16. Immediate research questions

- What is the strongest practical and reproducible G0 baseline for each task?
- Which mathematical corpus since PageRank is most relevant to provenance-bearing equivalence claims?
- Should the primary implementation be a graph, hypergraph, factor graph or several equivalent projections?
- How should correlated evidence and publisher independence be modelled?
- Which result formats permit explanation and contestability rather than opaque scoring?
- Which public datasets can supplement synthetic data without creating privacy or consent problems?
- What distribution of errors matters most when a false merge may be more harmful than a false split?

## References

- Sergey Brin and Lawrence Page, [*The Anatomy of a Large-Scale Hypertextual Web Search Engine*](https://research.google/pubs/the-anatomy-of-a-large-scale-hypertextual-web-search-engine/), 1998.
- Google Search Central, [*A guide to Google Search ranking systems*](https://developers.google.com/search/docs/appearance/ranking-systems-guide).
- [Trust Engine](../../trust-engine.md).
