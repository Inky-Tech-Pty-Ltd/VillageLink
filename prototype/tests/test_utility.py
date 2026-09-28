import unittest

from villagelink.codec import make
from villagelink.utility import Graph, Publication, inspect, parse, validate

A, B, C, D = (f"urn:example:{letter}" for letter in "abcd")


def pub(left, right, source):
    return Publication(make(left, right), source, "2026-09-28T00:00:00Z", source)


class UtilityTests(unittest.TestCase):
    def setUp(self):
        self.ab1 = pub(A, B, "https://publisher.example/one")
        self.ab2 = pub(B, A, "https://publisher.example/two")
        self.bc = pub(B, C, "https://publisher.example/three")
        self.cd = pub(C, D, "https://publisher.example/false-claim")
        self.graph = Graph((self.ab1, self.ab2, self.bc, self.cd))

    def test_parse_inspect_and_syntax_only_validation(self):
        self.assertEqual(parse(self.ab1.link), (A, B))
        self.assertEqual(inspect(self.ab1.link).right, B)
        for uri in (make("not-a-uri", B), make("https:///no-host", B),
                    "vl:urn%3Aexample%3Aa!urn%3Aexample%3A%ZZ"):
            with self.subTest(uri=uri):
                self.assertFalse(validate(uri))
        self.assertTrue(validate(make("mailto:user@example.org", "urn:example:x")))

    def test_duplicate_and_reversed_assertion_retains_each_publication(self):
        steps = self.graph.adjacent(A)
        self.assertEqual(len(steps), 1)
        self.assertEqual(steps[0].target, B)
        self.assertEqual(steps[0].publications, (self.ab1, self.ab2))
        self.assertEqual(self.graph.adjacent(B)[0].target, A)

    def test_bound_cycle_safety_and_structural_only_path(self):
        self.assertFalse(self.graph.connected(A, D, 2))
        self.assertTrue(self.graph.connected(A, D, 3))
        path, = self.graph.paths(A, D, 3)
        self.assertEqual(tuple(step.target for step in path), (B, C, D))
        self.assertEqual(path[-1].publications, (self.cd,))
        self.assertEqual(self.graph.component(A, 2), frozenset((A, B, C)))
        self.assertEqual(len(self.graph.traverse(A, 10)), 3)
        self.assertEqual(self.graph.paths(A, A, 0), ((),))

    def test_multiple_simple_paths_and_unknown_trace(self):
        graph = Graph((self.ab1, self.bc, pub(A, C, "urn:publication:four")))
        self.assertEqual(len(graph.paths(A, C, 2)), 2)
        self.assertEqual(graph.adjacent("urn:unknown"), ())
        self.assertEqual(graph.component("urn:unknown", 2), frozenset(("urn:unknown",)))

    def test_requires_valid_provenance_and_depth(self):
        with self.assertRaises(ValueError):
            Publication(make(A, B), "not a URI")
        for depth in (-1, 1.5, True):
            with self.subTest(depth=depth), self.assertRaises(ValueError):
                self.graph.traverse(A, depth)


if __name__ == "__main__":
    unittest.main()
