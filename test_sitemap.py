import unittest
import types
from requests import URLRequired, RequestException
from sitemap_extractor import Sitemap, get_http_content

S = Sitemap()

with open("sitemap_for_test_v1.xml", "r") as f:
    test_xml_1 = S.get_elements_from_xml(f.read())
with open("sitemap_for_test_v2.xml", "r") as f:
    test_xml_2 = S.get_elements_from_xml(f.read())


class TestGetHttpContent(unittest.TestCase):
    def test_incorrect_url(self):
        try:
            _ = get_http_content("abc")
        except URLRequired:
            _ = False
        self.assertFalse(_)

    def test_bad_status_code(self):
        try:
            _ = get_http_content("http://yandex.ru")
        except RequestException:
            _ = False
        self.assertFalse(_)

    def test_returns_xml_content(self):
        try:
            content = get_http_content("http://tavil.ru")
        except Exception as e:
            content = False
        self.assertTrue(content)
        self.assertTrue(isinstance(content, str))
        self.assertTrue(len(content) > 100)
        self.assertTrue(".xml" in content)


class TestGetElementsFromXml(unittest.TestCase):
    def test_returned_content(self):
        result = S.get_elements_from_xml("http://tavil.ru")
        self.assertTrue(isinstance(result, types.GeneratorType))


class TestParseXML(unittest.TestCase):
    def SetUp(self):
        self.parse_xml_result_1 = S.parse_xml(test_xml_1)
        self.parse_xml_result_2 = S.parse_xml(test_xml_2)

    def test_returns_generator(self):
        self.assertTrue(
            isinstance(self.parse_xml_result_1, types.GeneratorType)
        )

    def test_xml_links_not_in_result(self):
        self.assertTrue(".xml" not in self.parse_xml_result_2)

    def test_splitted_sitemap(self):
        self.assertTrue(".xml" in self.parse_xml_result_1)

if __name__ == "__main__":
    unittest.main()
