"""Adversarial regression tests for the Draft 0.1 Village Link serialization."""

import random
import string
import unittest

from villagelink.codec import make, parse


class VillageLinkUriTortureTests(unittest.TestCase):
    def assert_round_trip(self, a: str, b: str) -> None:
        link = make(a, b)
        self.assertEqual(link.count("!"), 1)
        self.assertEqual(parse(link), (a, b))
        self.assertTrue(link.startswith("vl:"))

    def test_reserved_characters_and_existing_escapes(self):
        cases = [
            ("urn:test:/?:#[]@!$&'()*+,;=", "https://example.net/%2F%20%21%25"),
            ("mailto:joe+vl@example.com?subject=A!B", "tel:+61-2-5550-0100"),
            ("data:text/plain;charset=utf-8,hello%20world!", "tag:example.org,2026:village/link"),
            ("https://example.com/a?next=https://nested.example/x?y=z#f", "urn:x:https://a/b?c=d#e"),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                self.assert_round_trip(a, b)

    def test_unicode_and_internationalised_material(self):
        self.assert_round_trip(
            "https://例え.テスト/路径/雪?q=नमस्ते#片🙂",
            "urn:例:Δοκιμή:مرحبا:🚲",
        )

    def test_asymmetric_hierarchies(self):
        self.assert_round_trip(
            "https://vc.village.link/a/b/c/d/e/f",
            "https://other.example/one",
        )

    def test_nested_village_link_is_opaque_endpoint_material(self):
        inner = make("https://example.com/a!x", "urn:example:b%20c")
        self.assert_round_trip(inner, "https://example.net/outer")

    def test_long_round_trip(self):
        a = "https://example.com/" + ("a/b?x=1&bang=!#frag" * 1000)
        b = "urn:example:" + ("雪🙂%20" * 1000)
        self.assert_round_trip(a, b)

    def test_deterministic_generated_round_trips(self):
        rng = random.Random(20260915)
        alphabet = string.ascii_letters + string.digits + ":/?#[]@!$&'()*+,;=%._~- " + "雪🙂Δ"
        for _ in range(1000):
            a = "urn:torture:" + "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 120)))
            b = "x-test:" + "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 120)))
            self.assert_round_trip(a, b)

    def test_malformed_percent_encoding_is_rejected(self):
        for payload in ("%ZZ!b", "%!b", "%2!b", "a!%GG"):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                parse(f"vl:{payload}")

    def test_invalid_utf8_percent_encoding_is_value_error(self):
        with self.assertRaises(ValueError):
            parse("vl:%E2%98!b")



if __name__ == "__main__":
    unittest.main()
