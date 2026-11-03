"""Assurance checks for the bounded paired G0/G1 research fixture."""
import unittest

from g1_comparison import Claim, World, Trace, generate, rank, link_signal, evaluate, experiment


class G1BenchmarkTests(unittest.TestCase):
    def test_world_reproducible_and_truth_not_implicitly_public(self):
        self.assertEqual(generate(31), generate(31))
        self.assertNotEqual(generate(31), generate(32))

    def test_g0_is_unchanged_by_g1_claims(self):
        world = generate(5)
        same = World(world.left, world.right, (), world.truth)
        self.assertEqual(rank(world, augmented=False, link_weight=.3),
                         rank(same, augmented=False, link_weight=.3))

    def test_copied_claims_do_not_count_as_independent(self):
        a, b = 'urn:left', 'urn:right'
        c = tuple(Claim(a, b, 'copy:' + str(i), 'origin:same')
                  for i in range(10))
        self.assertEqual(link_signal(c)[(a, b)], 1)
        other = Claim(a, b, 'independent', 'origin:other')
        self.assertEqual(link_signal(c + (other,))[(a, b)], 2)

    def test_evaluation_abstains_on_ambiguous_lookups(self):
        world = World(
            (Trace('a', 'left', 'same', 'north', 'health'),),
            (Trace('b', 'right', 'same', 'north', 'health'),
             Trace('c', 'right', 'same', 'north', 'health')),
            (), frozenset({('a', 'b')}))
        self.assertEqual(evaluate(world, augmented=False, link_weight=0,
                                  margin=.1)['abstain'], 1)

    def test_false_bridge_not_promoted_to_ground_truth(self):
        world = generate(25)
        self.assertTrue(all(not q.publisher.startswith('verified:')
                            for q in world.claims))
        false_bridges = [q for q in world.claims
                         if q.publisher.startswith('sybil:')
                         and (q.left, q.right) not in world.truth]
        self.assertEqual(len(false_bridges), 8)
        self.assertEqual(len({q.origin for q in false_bridges}), 1)

    def test_identifiers_do_not_expose_ground_truth_indices(self):
        world = generate(11)
        traces = (*world.left, *world.right)
        self.assertTrue(all(t.identifier.startswith('urn:g0:') for t in traces))
        self.assertTrue(all(len(t.identifier.rsplit(':', 1)[1]) == 30
                            for t in traces))
        self.assertEqual(len({t.identifier for t in traces}), 48)

    def test_zero_link_parity(self):
        result = experiment(range(3), range(100, 103), regime='none')
        self.assertEqual(result['heldout']['G0'], result['heldout']['G1'])

    def test_train_test_disjoint(self):
        with self.assertRaises(ValueError):
            experiment(range(10), range(9, 15))

    def test_paired_report_deterministic(self):
        self.assertEqual(experiment(range(4), range(100, 105)),
                         experiment(range(4), range(100, 105)))

    def test_adversarial_negative_regime_present(self):
        hostile = experiment(range(6), range(100, 110), regime='hostile')
        self.assertEqual(hostile['decisions'], 240)
        self.assertIn('hostile_fixed_optimistic_weight', hostile)


if __name__ == '__main__':
    unittest.main()
