from unittest import TestCase

import sitemap_extractor


class TestRequests(TestCase):
    def http_in_url(self):
        s = sitemap_extractor.Sitemap('http://tavil.ru')
        self.assertEqual(s, 100)
