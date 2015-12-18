import unittest
import types
from requests import RequestException
from sitemap_extractor import Sitemap, get_http_content

S = Sitemap()


class TestGetHttpContent(unittest.TestCase):
    def test_incorrect_url(self):
        try:
            _ = get_http_content("abc")
        except SystemExit:
            _ = False
        self.assertFalse(_)

    def test_bad_status_code(self):
        try:
            _ = get_http_content("http://yandex.ru/404/")
        except RequestException:
            _ = False
        self.assertFalse(_)

    def test_returns_xml_content(self):
        try:
            content = get_http_content("http://tavil.ru/sitemap.xml")
        except Exception as e:
            content = False
        self.assertTrue(content)
        self.assertTrue(isinstance(content, str))
        self.assertTrue(len(content) > 100)
        self.assertTrue(".xml" in content)


class TestGetElementsFromXml(unittest.TestCase):
    def test_returned_content(self):
        result = S.get_elements_from_xml("http://tavil.ru/sitemap.xml")
        self.assertTrue(isinstance(result, types.GeneratorType))


class TestParseXML(unittest.TestCase):
    def setUp(self):
        self.result = S.parse_xml(get_http_content('http://tavil.ru'))

    def test_returns_generator(self):
        self.assertTrue(
            isinstance(self.result, types.GeneratorType)
        )

if __name__ == "__main__":
    unittest.main()
