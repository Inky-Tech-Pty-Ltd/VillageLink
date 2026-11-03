# Paired G0/G1 entity-resolution experiment (Research 002)

**Status:** exploratory, synthetic research fixture. Not a reference Trust Engine,
production service, independent interoperability result or claim of real-world
superiority. Tracks [Research 002](../../../../docs/research/002-modelling-g1.md)
and [issue #82](https://github.com/Inky-Tech-Pty-Ltd/VillageLink/issues/82).

## Proposition and scope

This minimal implementation tests whether adding explicitly attributable
pairwise assertions **under declared synthetic assumptions** changes identity
resolution outcomes when the underlying content observations are held fixed.
It implements only one part of Research 002: paired data, held-out tuning,
a matched G0/G1 algorithm, one identity-resolution task, and false-merge cost.

It is *not* the "strongest available G0" required for any broad performance
claim. G0 is a content-only name/region/topic matcher, intentionally simple.
G1 receives those exact same content fields plus fallible, provenance-bearing
assertions. It does **not** receive hidden entity labels. Publisher independence
is represented by a synthetic observable `origin` grouping attribute, not
measured or authenticated independence in a real network.

## Run (Python >= 3.11; standard library only)

From the repository root:

```sh
PYTHONPATH=prototype/research/g0_g1 python -m unittest discover \
  -s prototype/research/g0_g1/tests -v
python prototype/research/g0_g1/g1_comparison.py --regime mixed
python prototype/research/g0_g1/g1_comparison.py --regime hostile
python prototype/research/g0_g1/g1_comparison.py --regime none
python prototype/research/g0_g1/g1_comparison.py --regime mixed --output /tmp/g1-mixed.json
```

A report contains the world seeds, train-selected parameters, per-seed paired
results, aggregate correct matches/false merges/abstentions and decision loss.
The seed partitions are disjoint: training 0–29, held-out 100–179, 24
underlying entities in each world (1,920 held-out lookup decisions).

A synthetic trace ID is a random opaque identifier; the hidden pairing index
is not encoded in it. Ground truth is held in `World.truth` and referenced only
during scoring. The scorer labels a candidate as correct, a false merge, or
abstained. Abstention is not a correct match.

## Declared scoring assumptions

- G0 content score: `0.60 name + 0.24 region + 0.16 topic` exact matches.
- G1 adds a learned weight on up to two independent **declared origin groups**
  supporting a candidate pair. Repeated publishers with the same origin count
  once. This is not a claim to authenticate independent witnesses.
- Fixed search grid: G1 weights 0.05, 0.15, 0.30, 0.45; G0 weight 0; both
  abstention margins 0, 0.10, 0.20, 0.30, 0.40.
- Minimise training decision loss `4 * false_merge + abstain`, then test
  without retuning. This loss is an explicit illustrative risk preference,
  not an empirically established transaction-cost model.
- The mixed regime contains honest and mistaken claims, copied claims and an
  eight-publisher false bridge with one provenance origin.
- The hostile regime raises the rate of mistaken/malicious assertions.
- The no-link regime is a parity control. The hostile fixed-weight case
  deliberately uses an optimistic weight without hostile retuning to expose
  sensitivity to changed assumptions.

## Local held-out observations

These values come from the reproducible local implementation, on the
declared 80 held-out worlds. They are *not* external validation or evidence
that production Village Links outperform contemporary search.

| Regime | G0 loss | Tuned G1 loss | G1 minus G0 | Interpretation |
|---|---:|---:|---:|---|
| Mixed | 1,153 | 761 | -392 | Improvement under favourable synthetic signal mix |
| Hostile, separately tuned | 1,153 | 1,116 | -37 | Benefit is small under adverse assertions |
| Hostile, optimistic fixed weight | 1,153 | 1,337 | +184 | An overconfident G1 can **worsen** results |
| No links | 1,153 | 1,153 | 0 | Expected identical outcome without added assertions |

The hostile fixed-weight result shows that adding assertions is not uniformly
beneficial. Retuning *for* a hostile regime is a methodological upper bound
that may not be available to a real reader who cannot identify that regime.

## Assurance limits and future evidence

This experiment cannot establish the value of Village Links relative to
current entity-resolution systems. The generator's positive-label and publisher
rates are chosen assumptions, not estimated from data. Neither G0 nor G1
models realistic text embeddings, platform identity systems, authentication,
reviewer independence, privacy costs, source timestamps, transferred/reused
identifiers, or missing evidence. There is no causal identification beyond
these paired synthetic rules, no real-world calibration, and no claim of
statistical independence between individual decisions in a shared world.

Before architectural promotion: compare strong modern record-linkage and
provenance-aware baselines; measure true source dependence without relying
on supplied grouping labels; test longitudinal identifier transfer, dataset
shift and calibration; use independently reviewed data and privacy constraints.
A negative result or no benefit may be the correct outcome.

**No changes to VillageLink's equality semantics, Star Credential abstraction,
publisher custody model or Trust Engine concept are proposed.**

## Contribution and provenance

Prepared with AI assistance for review under the authenticated
`sankarshanmukhopadhyay` contributor identity. The VillageLink maintainers
retain acceptance and interpretation authority. Code and executable tests
follow the repository's Apache 2.0 implementation-material boundary; this
research README follows its CC BY-SA 4.0 documentation boundary.
