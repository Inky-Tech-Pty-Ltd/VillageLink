"""Paired synthetic G0/G1 entity-resolution benchmark; not a Trust Engine.

Ground truth is used ONLY for scoring, not inference. No external data,
live network, personal identities or non-standard Python dependencies.
"""
import argparse
import json
import random
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

NAMES = ('Arun', 'Mira', 'Sam', 'Nora', 'Kai', 'Riya')
REGIONS = ('north', 'south', 'east', 'west')
TOPICS = ('music', 'health', 'civic', 'software', 'trade')


@dataclass(frozen=True)
class Trace:
    identifier: str
    context: str
    name: str
    region: str
    topic: str


@dataclass(frozen=True)
class Claim:
    left: str
    right: str
    publisher: str
    origin: str  # observable provenance group, not a statement of honesty


@dataclass(frozen=True)
class World:
    left: tuple[Trace, ...]
    right: tuple[Trace, ...]
    claims: tuple[Claim, ...]
    truth: frozenset[tuple[str, str]]  # scoring ONLY; never passed to infer()


def generate(seed: int, n: int = 24, *, regime: str = 'mixed') -> World:
    """Paired observed contexts from one world; identical G0 data for G1."""
    if n < 8 or regime not in {'mixed', 'hostile', 'none'}:
        raise ValueError('n >= 8 and supported regime required')
    rng = random.Random(seed)
    left, right = [], []
    for i in range(n):
        name = NAMES[i % len(NAMES)]
        region = REGIONS[(i // 2) % len(REGIONS)]
        topic = TOPICS[(i * 3) % len(TOPICS)]
        left.append(Trace(f'urn:g0:left:{rng.getrandbits(120):030x}',
                          'left', name, region, topic))
        right.append(Trace(f'urn:g0:right:{rng.getrandbits(120):030x}',
                           'right',
                           name if rng.random() > .18 else rng.choice(NAMES),
                           region if rng.random() > .28 else rng.choice(REGIONS),
                           topic if rng.random() > .30 else rng.choice(TOPICS)))
    indexed_right = dict(enumerate(right))  # hidden-world pairing; not inference input
    rng.shuffle(right)
    claims = []
    if regime != 'none':
        for i, a in enumerate(left):
            if rng.random() < .74:
                honest = rng.random() > (.30 if regime == 'mixed' else .72)
                j = i if honest else rng.choice([j for j in range(n) if j != i])
                b = indexed_right[j]
                claims.append(Claim(a.identifier, b.identifier,
                                    f'issuer:{i}:primary', f'origin:{i}'))
                if rng.random() < .35:
                    claims.append(Claim(a.identifier, b.identifier,
                                        f'issuer:{i}:mirror', f'origin:{i}'))
            if rng.random() < .28:
                honest = rng.random() > (.19 if regime == 'mixed' else .73)
                j = i if honest else rng.choice([j for j in range(n) if j != i])
                claims.append(Claim(a.identifier, indexed_right[j].identifier,
                                    f'other:{i}', f'independent:{i}'))
        # A false bridge with many apparently separate but copied claims.
        i = rng.randrange(n)
        j = (i + 1) % n
        for k in range(8):
            claims.append(Claim(left[i].identifier, indexed_right[j].identifier,
                                f'sybil:{seed}:{k}', f'shared-campaign:{seed}'))
    truth = frozenset((a.identifier, indexed_right[i].identifier)
                      for i, a in enumerate(left))
    return World(tuple(left), tuple(right), tuple(claims), truth)


def content_score(a: Trace, b: Trace) -> float:
    return (.60 * (a.name == b.name) + .24 * (a.region == b.region)
            + .16 * (a.topic == b.topic))


def link_signal(claims: tuple[Claim, ...]) -> dict[tuple[str, str], int]:
    # Count declared origins, never duplicated publisher handles.
    origins = defaultdict(set)
    for claim in claims:
        origins[(claim.left, claim.right)].add(claim.origin)
    return {key: min(len(value), 2) for key, value in origins.items()}


def rank(world: World, *, augmented: bool, link_weight: float):
    """No use of world.truth or hidden generator pairing."""
    signal = link_signal(world.claims) if augmented else {}
    result = {}
    for a in world.left:
        scored = [(b.identifier,
                   round(content_score(a, b) +
                         link_weight * signal.get((a.identifier, b.identifier), 0), 8))
                  for b in world.right]
        result[a.identifier] = sorted(scored, key=lambda x: (-x[1], x[0]))
    return result


def evaluate(world: World, *, augmented: bool, link_weight: float, margin: float):
    """Abstain unless top candidate exceeds second-place candidate by margin."""
    ranks = rank(world, augmented=augmented, link_weight=link_weight)
    correct = false_merge = abstain = 0
    for left, candidates in ranks.items():
        top, runner_up = candidates[:2]
        if top[1] - runner_up[1] < margin:
            abstain += 1
        elif (left, top[0]) in world.truth:
            correct += 1
        else:
            false_merge += 1
    return {'correct': correct, 'false_merge': false_merge,
            'abstain': abstain, 'count': len(world.left),
            'loss': false_merge * 4 + abstain}


def tune(seeds: range, *, augmented: bool, n: int, regime: str):
    """Explicit training-only grid: no held-out threshold selection."""
    choices = [(w, m) for w in ((0,) if not augmented else (.05, .15, .30, .45))
               for m in (.0, .10, .20, .30, .40)]
    worlds = [generate(seed, n, regime=regime) for seed in seeds]
    return min(({'weight': w, 'margin': m,
                 'training_loss': sum(evaluate(world, augmented=augmented,
                                               link_weight=w, margin=m)['loss']
                                      for world in worlds)}
                for w, m in choices),
               key=lambda x: (x['training_loss'], x['weight'], x['margin']))


def experiment(train=range(30), test=range(100, 180), *, n=24, regime='mixed'):
    if set(train) & set(test):
        raise ValueError('train and test seeds must be disjoint')
    if not train or not test:
        raise ValueError('nonempty partitions required')
    tuned = {k: tune(train, augmented=(k == 'G1'), n=n, regime=regime)
             for k in ('G0', 'G1')}
    summary = {k: {'correct': 0, 'false_merge': 0, 'abstain': 0, 'loss': 0}
               for k in ('G0', 'G1')}
    paired = []
    for seed in test:
        world = generate(seed, n, regime=regime)
        record = {'seed': seed}
        for kind in ('G0', 'G1'):
            result = evaluate(world, augmented=(kind == 'G1'),
                              link_weight=tuned[kind]['weight'],
                              margin=tuned[kind]['margin'])
            record[kind] = {key: result[key] for key in summary[kind]}
            for metric in summary[kind]:
                summary[kind][metric] += result[metric]
        paired.append(record)
    decisions = n * len(test)
    aggressive = {'correct': 0, 'false_merge': 0, 'abstain': 0, 'loss': 0}
    if regime == 'hostile':
        # Negative control: carry optimistic fixed G1 weight into hostile data.
        for seed in test:
            fixed = evaluate(generate(seed, n, regime=regime), augmented=True,
                             link_weight=.45, margin=.10)
            for key in aggressive:
                aggressive[key] += fixed[key]
    return {'method': 'paired synthetic entity resolution, not full-Web baseline',
            'regime': regime,
            'train_seeds': [train.start, train.stop, train.step],
            'test_seeds': [test.start, test.stop, test.step],
            'n_entities_per_world': n,
            'loss_definition': '4 * false_merge + abstain',
            'training': tuned, 'heldout': summary, 'decisions': decisions,
            'delta_loss_G1_minus_G0': summary['G1']['loss'] - summary['G0']['loss'],
            'hostile_fixed_optimistic_weight': aggressive if regime == 'hostile' else None,
            'paired_runs': paired}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--regime', choices=['mixed', 'hostile', 'none'],
                        default='mixed')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = experiment(regime=args.regime)
    output = json.dumps(result, sort_keys=True, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding='utf-8')
    else:
        print(json.dumps({k: v for k, v in result.items()
                          if k != 'paired_runs'}, indent=2))


if __name__ == '__main__':
    main()
