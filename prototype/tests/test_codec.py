import unittest

from villagelink.codec import make, parse


class VillageLinkCodecTests(unittest.TestCase):
    def assert_round_trip(self, a: str, b: str) -> None:
        link = make(a, b)
        self.assertTrue(link.startswith("vl:"))
        self.assertEqual(parse(link), (a, b))

    def test_asha_bhosle_demo(self):
        self.assert_round_trip(
            "https://village.link/wiki/index.php/Asha_Bhosle",
            "https://en.wikipedia.org/wiki/Asha_Bhosle",
        )

    def test_no_publisher_domain_or_encoded_operator(self):
        self.assertEqual(make("https://github.com/Joe-Rasmussen", "urn:person:joe"),
                         "vl:https%3A%2F%2Fgithub.com%2FJoe-Rasmussen!urn%3Aperson%3Ajoe")

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
        self.assert_round_trip("https://example.com/bang!here", "urn:example:foo/bar?x=!")
        link = make("https://example.com/bang!here", "urn:example:x!")
        self.assertEqual(link.count("!"), 1)
        self.assertIn("%21", link)

    def test_unicode(self):
        self.assert_round_trip("https://例え.テスト/路径?q=雪#片", "https://example.com/नमस्ते")

    def test_nested_uri_material(self):
        self.assert_round_trip(
            "https://example.com/nested?u=https://other.example/a?b=c#d",
            "urn:example:embedded:https://example.net/a/b?c=d",
        )

    def test_endpoint_order_is_preserved(self):
        a, b = "https://example.com/a", "https://example.com/b"
        self.assertEqual(parse(make(a, b)), (a, b))
        self.assertEqual(parse(make(b, a)), (b, a))
        self.assertNotEqual(make(a, b), make(b, a))

    def test_malformed_payloads_are_rejected(self):
        for link in ("vl:no-separator", "vl:a!b!c", "vl:!b", "vl:a!", "vl:",
                     "https://wab.village.link/a!b", "VL:a!b"):
            with self.subTest(link=link), self.assertRaises(ValueError):
                parse(link)
        for a, b in (("", "urn:b"), ("urn:a", "")):
            with self.assertRaises(ValueError):
                make(a, b)


if __name__ == "__main__":
    unittest.main()
