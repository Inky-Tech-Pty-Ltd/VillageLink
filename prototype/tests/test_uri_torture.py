"""Adversarial regression tests for the Draft 0.1 Village Link serialization."""

import random
import string
import unittest

from villagelink.codec import make, marker_for, parse, parse_with_domain


class VillageLinkUriTortureTests(unittest.TestCase):
    def assert_round_trip(self, a: str, b: str, domain: str = "village.link") -> None:
        link = make(a, b, domain)
        self.assertEqual(link.count("!"), 1)
        self.assertEqual(parse(link), (a, b))
        self.assertEqual(parse_with_domain(link), (domain.lower().rstrip("."), a, b))

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
        self.assert_round_trip(
            "https://example.com/a",
            "https://example.net/b",
            "例え.テスト",
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

    def test_userinfo_is_rejected(self):
        with self.assertRaises(ValueError):
            parse("https://user@wab.village.link/a!b")
        with self.assertRaises(ValueError):
            parse("https://user:password@wab.village.link/a!b")

    def test_explicit_port_is_rejected(self):
        with self.assertRaises(ValueError):
            parse("https://wab.village.link:443/a!b")
        with self.assertRaises(ValueError):
            parse("https://wab.village.link:8443/a!b")

    def test_extra_leading_path_slashes_are_rejected(self):
        with self.assertRaises(ValueError):
            parse("https://wab.village.link//a!b")
        with self.assertRaises(ValueError):
            parse("https://wab.village.link///a!b")

    def test_malformed_percent_encoding_is_rejected(self):
        for payload in ("%ZZ!b", "%!b", "%2!b", "a!%GG"):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                parse(f"https://wab.village.link/{payload}")

    def test_invalid_utf8_percent_encoding_is_value_error(self):
        with self.assertRaises(ValueError):
            parse("https://wab.village.link/%E2%98!b")

    def test_invalid_dns_domains_are_rejected(self):
        invalid = (
            "example..com",
            ".example.com",
            "foo_bar.com",
            "-example.com",
            "example-.com",
            ("a" * 64) + ".example",
        )
        for domain in invalid:
            with self.subTest(domain=domain), self.assertRaises(ValueError):
                marker_for(domain)

    def test_trailing_dot_domain_is_canonicalised(self):
        self.assertEqual(marker_for("Example.COM."), "https://wab.example.com/")


if __name__ == "__main__":
    unittest.main()
