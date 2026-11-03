"""Star interchange boundary tests for the draft centred-set model.

These tests use the existing URI codec and structural graph utility.
They do not establish a Star wire format, proof of equality, or publisher policy.
"""
import unittest

from villagelink.codec import make, parse
from villagelink.utility import Graph, Publication

A, B, C, D = ("urn:star-test:" + x for x in "abcd")


def members_from_rays(centre, rays):
    """Recover unique members only when the centre is independently supplied."""
    members = set()
    for ray in rays:
        left, right = parse(ray)
        if left == centre and right != centre:
            member = right
        elif right == centre and left != centre:
            member = left
        else:
            raise ValueError("not a centre-member ray")
        if member in members:
            raise ValueError("duplicate member")
        members.add(member)
    return frozenset(members)


class StarInterchangeBoundaryTests(unittest.TestCase):
    def test_member_order_has_no_abstract_significance(self):
        first = (make(A, B), make(A, C), make(A, D))
        second = (make(D, A), make(B, A), make(C, A))
        self.assertEqual(members_from_rays(A, first), members_from_rays(A, second))

    def test_reversed_rays_reconstruct_with_explicit_centre(self):
        self.assertEqual(members_from_rays(A, (make(A, B), make(C, A))),
                         frozenset((B, C)))

    def test_reconstruction_rejects_nonstar_and_duplicate_rays(self):
        for rays in ((make(B, C),), (make(A, B), make(B, A)),
                     (make(A, A),)):
            with self.subTest(rays=rays), self.assertRaises(ValueError):
                members_from_rays(A, rays)

    def test_two_publishers_of_same_assertion_remain_distinct(self):
        one = Publication(make(A, B), "urn:publisher:one")
        two = Publication(make(B, A), "urn:publisher:two")
        edges = Graph((one, two)).adjacent(A)
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0].target, B)
        self.assertEqual(edges[0].publications, (one, two))

    def test_subset_changes_content_without_claiming_completeness(self):
        full = members_from_rays(A, (make(A, B), make(A, C), make(A, D)))
        subset = members_from_rays(A, (make(A, B), make(A, C)))
        self.assertTrue(subset < full)
        self.assertNotEqual(subset, full)
        # Neither representation asserts that these are all known rays.

    def test_serialized_order_is_not_abstract_equality(self):
        self.assertNotEqual(make(A, B), make(B, A))
        self.assertEqual(members_from_rays(A, (make(A, B),)),
                         members_from_rays(A, (make(B, A),)))


if __name__ == "__main__":
    unittest.main()
