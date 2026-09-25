import unittest

from villagelink.codec import make, parse, parse_with_domain


class VillageLinkCodecTests(unittest.TestCase):
    def assert_round_trip(self, a: str, b: str, domain: str = "village.link") -> None:
        link = make(a, b, domain)
        self.assertEqual(parse(link), (a, b))
        self.assertEqual(parse_with_domain(link), (domain, a, b))

    def test_asha_bhosle_demo(self):
        a = "https://village.link/wiki/index.php/Asha_Bhosle"
        b = "https://en.wikipedia.org/wiki/Asha_Bhosle"

        link = make(a, b)

        self.assertEqual(
            link,
            "https://wab.village.link/https://village.link/wiki/index.php/Asha_Bhosle"
            "!https://en.wikipedia.org/wiki/Asha_Bhosle",
        )
        self.assertEqual(parse(link), (a, b))

    def test_alternate_domain(self):
        a = "https://example.com/a"
        b = "https://example.net/b"
        link = make(a, b, "example.org")
        self.assertTrue(link.startswith("https://wab.example.org/"))
        self.assertEqual(parse_with_domain(link), ("example.org", a, b))

    def test_query_fragment_and_reserved_characters(self):
        self.assert_round_trip(
            "https://example.com/a/b?x=1&y=two#frag",
            "mailto:joe@example.com",
        )

    def test_existing_percent_encoding(self):
        self.assert_round_trip(
            "https://example.com/%2Falready%20encoded",
            "tel:+61-438-342-332",
        )

    def test_literal_separator_character(self):
        self.assert_round_trip(
            "https://example.com/bang!here",
            "urn:example:foo/bar?x=!",
        )
        link = make("https://example.com/bang!here", "urn:example:x!")
        self.assertEqual(link.count("!"), 1)
        self.assertIn("%21", link)

    def test_unicode(self):
        self.assert_round_trip(
            "https://例え.テスト/路径?q=雪#片",
            "https://example.com/नमस्ते",
        )

    def test_nested_uri_material(self):
        self.assert_round_trip(
            "https://example.com/nested?u=https://other.example/a?b=c#d",
            "urn:example:embedded:https://example.net/a/b?c=d",
        )

    def test_endpoint_order_is_preserved(self):
        a = "https://example.com/a"
        b = "https://example.com/b"
        self.assertEqual(parse(make(a, b)), (a, b))
        self.assertEqual(parse(make(b, a)), (b, a))
        self.assertNotEqual(make(a, b), make(b, a))

    def test_malformed_payloads_are_rejected(self):
        with self.assertRaises(ValueError):
            parse("https://wab.village.link/no-separator")
        with self.assertRaises(ValueError):
            parse("https://wab.village.link/a!b!c")
        with self.assertRaises(ValueError):
            parse("https://wab.village.link/!b")

    def test_invalid_domain_is_rejected(self):
        with self.assertRaises(ValueError):
            make("https://example.com/a", "https://example.com/b", "https://village.link")


if __name__ == "__main__":
    unittest.main()
