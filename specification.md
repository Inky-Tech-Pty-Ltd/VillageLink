# Village Link Specification

**Version:** Working Draft 0.2  
**Date:** 29 October 2026  
**Status:** Experimental; alignment with accepted [ADR-008](docs/adr/008-traces-referent-and-independent-uri.md), not a ratified standards release

## 1. Scope and authority

This working draft describes the Village Link primitive, the current draft URI codec, and the abstract **Star Credential** model. It supersedes the terminology and serialization *in this document's previous Draft 0.1*, which predated ADR-008.

The core proposition is narrow: a **Village Link asserts strict equality of referent between two traces understood in their respective memory systems**. It does not prove the assertion.

The current direction follows [ADR-002](docs/adr/002-equivalence-only.md) (equality only), [ADR-004](docs/adr/004-star-credential-data-model.md) (centred Star Credential), [ADR-005](docs/adr/005-endpoint-identifiers-and-naming.md) (URI endpoints), [ADR-007](docs/adr/007-stateless-composer.md) (stateless Composer), and especially [ADR-008](docs/adr/008-traces-referent-and-independent-uri.md) (trace semantics and publication-independent URI). [ADR-001](docs/adr/001-two-ended-uri.md) retains its two-ended, self-contained design; [ADR-006](docs/adr/006-village-link-serialization.md) retains useful encoding rationale but its earlier publisher-domain HTTPS format was superseded in part by ADR-008.

The [README](README.md) introduces the current conceptual model; the [glossary](glossary.md) gives working definitions. If another document still presents the earlier model as current, that is documentation debt, not a second simultaneous definition of the primitive.

**MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT** and **MAY** indicate proposed requirements within this working draft. Their use here does not imply that all wire-format and conformance questions have been settled.

## 2. Model: two traces, two memory systems, one proposed referent

A memory system retains traces of memes. A trace has meaning in the circumstances and conventions of the memory system in which it occurs. A **meme** is the referent expressed through traces; it need not be a human, an account, a document, or even a physical object.

Let:

- **X** and **Y** be memory systems (they need not be of the same technological kind).
- **A** be a trace in X; **B** be a trace in Y.
- **P** be a URI identifying the trace *A in X*; **Q** be a URI identifying *B in Y*.
- **M** be the proposed common referent, or meme.

The conceptual Village Link is:

```text
vl:[A in X]=[B in Y]
```

The asserted referential equality is:

```text
M = [A in X] = [B in Y]
```

This notation does **not** assert that A and B are identical strings, that X and Y are the same system, or that everything said in one context can be imported into the other. It asserts one thing only: *the two expressions have the same referent*.

The `=` is **hard**, not an approximate similarity measure. A particular Village Link's assertion can be true or false. Its publication does not establish which; a consuming system may also remain uncertain. Mere shared vocabulary, co-occurrence or topical resemblance is insufficient to establish equality.

Village Link has no operator for *is employed by*, *owns*, *resembles*, *trusts*, *is a member of*, or *is not equal to*. Such information may form evidence in memory systems or in applications, but it is not a second type of Village Link.

## 3. Equality and the graph

### 3.1 Symmetry

Referential equality is symmetric. Neither endpoint is inherently a source, destination, issuer, subject or superior authority. The order of P and Q can be retained in the serialized URI for exact round trips and presentation, but cannot be used to assign truth or authority.

### 3.2 Transitivity requires valid premises

If **both** assertions `A = B` and `B = C` are true of their referents, then `A = C` follows. But the existence of two *published claims* does not establish the truth of either premise. An application MUST NOT silently promote chains of uncertain or conflicting assertions into verified equivalence.

A graph may contain false, disputed or contradictory links without invalidating the URI syntax or requiring a central adjudicator. A source's availability and a link's truth are different questions.

## 4. Endpoint identifiers

The current codec uses **two URI endpoints** P and Q. Each MUST be independently meaningful outside the Village Link itself; the identifying memory system determines how to interpret it. An endpoint need not be HTTP(S), publicly dereferenceable, or hosted by an implementation of Village Link.

A publisher or application may mint a stable URI for a selected passage or other trace within a larger source. An endpoint URI identifies the intended trace; it need not expose the source content to everyone who knows the identifier. Access, retention and source integrity are separate responsibilities.

[ADR-005](docs/adr/005-endpoint-identifiers-and-naming.md) records the optional `gc.` and `vc.` HTTPS/DNS naming conventions for some minted identifiers. They are **not** required, privileged endpoint types or a universal context hierarchy. Existing independently meaningful trace URIs MAY be used directly. URI addressability does not imply a central directory of meaning or reliable online retrieval.

Alternative memory-native addressing is a research question for applications such as Cobble; it has not replaced URI endpoints in the current Village Link codec.

## 5. Draft serialization

The current experimental codec uses a self-contained, publication-independent URI:

```text
vl:<percent-encoded-P>!<percent-encoded-Q>
```

The URI above is the *serialized assertion*. The expression `vl:[A in X]=[B in Y]` in Section 2 is its **conceptual meaning**, not literal wire syntax.

The reference [codec](prototype/villagelink/codec.py) currently:

1. encodes each endpoint as UTF-8 percent escapes, leaving only RFC 3986 unreserved characters `A-Z a-z 0-9 - . _ ~` unescaped;
2. joins the encoded endpoints with **one literal `!`**;
3. uses `vl:` as the outer scheme;
4. parses by splitting at the sole literal `!` and decoding each endpoint **once**; and
5. preserves endpoint order and literal percent-encoded material in the recovered input strings.

A literal `!` inside an endpoint becomes `%21`; a literal `%20` inside an endpoint must be embedded as `%2520` so that parsing once recovers `%20`, not a space.

For example:

```text
P = https://example.org/memory/A
Q = mailto:someone@example.org

vl:https%3A%2F%2Fexample.org%2Fmemory%2FA!mailto%3Asomeone%40example.org
```

The construction criterion is:

```text
parse(make(P, Q)) == (P, Q)
```

This is the implemented **draft** encoding, not a declaration that every URI-library, internationalisation, canonicalisation and interoperability question has been settled. The prototype codec checks non-empty endpoints and percent-encoding structure; it is not yet a comprehensive URI conformance or authentication validator.

**Historical note:** `https://wab.<domain>/...` was an earlier candidate in ADR-006. A `wab.` host can still serve as a publisher or ordinary web resource, but its domain does not identify the Village Link itself. No publication host is required to recover P and Q. URI scheme registration and interoperable handler behaviour remain work for the draft protocol.

## 6. Publication, provenance and truth

A Village Link and an act of **publishing** that link are different objects of interest.

- The Village Link carries the proposed equality of the two traces.
- A **publisher** chooses to make that assertion available.
- A publication context (historically called **W**) can supply authorship, time, evidence, location, governance and opportunities for challenge.
- Multiple publishers MAY independently publish the same Village Link. Their publication histories remain distinct even when the underlying URI is the same.

Publication may occur on a web page, in a wiki, an application store, a signed document or another medium. Neither W nor a publisher identifier is an additional endpoint of the `vl:` primitive. No particular publisher's assertion is privileged merely by the syntax.

A conforming assertion does **not** establish truth, consent, authentication, endorsement, provenance integrity, or the continued existence of its endpoints. Readers and Trust Engines MAY inspect external evidence but MUST NOT treat syntax alone as verification.

The protocol does not prescribe a publisher reputation score or Trust Engine ranking algorithm. Publication identity, retraction, copying, quotation, signatures and evidence integrity remain application or future-standard questions.

## 7. Star Credentials

A **Star Credential** is a distinguished **centre trace URI** P0 and a finite, **unordered set** S of member trace URIs. Its meaning is the collection of constituent Village Link assertions:

```text
SC(P0, S)
S = {P1, P2, ... Pn}
assertions = { P0 = Pi | Pi in S }
```

The centre is commonly called the **hypothesis**: a proposed meme expressed as an ordinary trace, not a new primitive or privileged identity key. Each constituent Village Link is called a **ray**.

- P0 MUST remain distinguishable as the centre.
- Members of S MUST be unique. Their ordering conveys no meaning or extra weight.
- The centre's structural distinction MUST NOT give one end of any constituent Village Link greater truth or authority.
- Two Star Credentials with the same centre and member set have the same **content** even if separately published; publications and provenance remain distinct.
- The credential asserts an invariant referent across its rays, but **does not prove** any ray, membership, identity or claim about the centre.

An illustrative representation used in experiments is:

```json
{
  "type": "StarCredential",
  "A": "<centre-trace-URI>",
  "B": ["<member-trace-URI>", "<member-trace-URI>"]
}
```

This JSON is **not** a ratified normative serialization. The current abstract centred-set model is defined by [ADR-004](docs/adr/004-star-credential-data-model.md); canonical encoding, publisher provenance, subsets and signing need separate work.

## 8. Roles and boundaries

The following roles use or interpret Village Links but are not additional parts of the primitive:

- **Standard:** defines the minimal equality assertion and abstract Star Credential.
- **Publisher:** makes assertions available under its own governance and provenance.
- **Composer:** constructs Village Links or Star Credentials from supplied inputs without automatically retaining a persistent private credential collection ([ADR-007](docs/adr/007-stateless-composer.md)).
- **Browser / Trust Engine:** reader-side software that discovers, interprets, ranks and checks evidence around published objects, without silently becoming their publisher.
- **Cobble:** an experimental application that retains and organises memory, with possible Cobbler services, arenas and multiple intelligence processes. It does not redefine the Village Link primitive.

Claims about **governance through consequences**, **self-sovereign entities**, **social value functions**, **hemispheres** or **emergent identity** are project hypotheses, not conformance requirements.

## 9. Safety and lifecycle

An equality assertion can disclose a connection that the respective memory systems never disclosed themselves. Risks include unintended correlation of identities, stalking, impersonation, deanonymisation, coercion and inaccurate attribution. Standards conformance is not an authorisation to publish sensitive links.

Endpoint content can change, disappear or become inaccessible. Assertions may be retracted or disputed. A publisher or application SHOULD preserve appropriate provenance and observation history where it is lawful and safe to do so, without treating observations as proof of truth or requiring permanent custody of private material.

The current primitive does not specify universal consent, revocation, deletion, expiry, access control or conflict adjudication.

## 10. Provisional conformance and open work

For this draft model, a **Village Link**:

1. expresses strict equality of referent between two addressable traces in their memory-system contexts;
2. contains two independently meaningful URI endpoints that are recoverable without dereferencing a publisher or separate link resource;
3. permits false and disputed assertions without changing the meaning or shape of the relation; and
4. does not encode the publisher, evidentiary score or governance policy as a third endpoint.

A **Star Credential** designates one centre and a finite unordered set of unique member URIs and asserts an ordinary Village Link from the centre to each member. These are **provisional draft conformance statements**, not certification of implementations.

Open work includes: URI and percent-encoding interoperability tests; canonicalisation and comparison of reversed serializations; practical size limits; Star Credential canonical wire format and signing; attribution, preservation and republication of assertions; safety controls; trace selection and persistent addressing; and changing or inaccessible source material.

**Documentation debt:** [requirements.md](requirements.md) and some earlier accepted ADR texts still retain `W states A ↔ B`, `wab.` or same-*entity*-only terminology. Their historical decisions should be retained and reconciled through explicit review rather than silently rewritten as if they had always said `vl:[A in X]=[B in Y]`.

The current small centre of the experiment is:

```text
vl:[A in X]=[B in Y]
```

**Two traces. Two memory systems. One asserted meme.**
