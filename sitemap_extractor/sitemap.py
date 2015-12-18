#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
SitemapExtractor Module

:Author:
    robotehnik@me.com
:License:
    MIT

:Usage:
    # import module
    import sitemap_extractor as SE

    # init class
    extractor = SE()

    # get links
    links = extractor.get_links("http://mysite.com")

    # optional - save result
    extractor.save_to_file(links, "myfile.txt")
"""

import requests
from bs4 import BeautifulSoup

# TODO: replace bs4 lib with something more lightweight


def get_http_content(url):
    """
    Get content from any url

    :param url: domain like 'http://site.com', without '/' and 'sitemap.xml'
    :return: web content or throw error
    """
    try:
        r = requests.get(url)
    except requests.URLRequired:
        print("Is it a correct url? - {}".format(url))
    except requests.ConnectionError:
        print("Possible DNS failure or connection was refused.")
    except requests.HTTPError:
        print("Invalid HTTP response")
    except requests.Timeout:
        print("Connection Timeout")
    except requests.TooManyRedirects:
        print("Too Many Redirects")
    except Exception as e:
        print("During execution error was revealed:\n{}".format(e))
    else:
        if r.status_code == 200:
            return r.text
        else:
            raise requests.RequestException(
                "Bad Status Code: {}\n{}".format(r.status_code, url)
            )
    exit(1)


class Sitemap(object):
    """Class for OOP skills test"""

    def __init__(self):
        pass

    @staticmethod
    def save_to_file(result, filename="sitemap.txt"):
        """
        SAve file with results to disk

        :param result: generator object
        :param filename: optional, name of a file
        """
        with open(filename, 'w') as f:
            f.write('\n'.join(tuple(result)))

    @staticmethod
    def get_elements_from_xml(url):
        """
        Get xml elements from url if url is to xml file

        :param url: string, like http://site.com
        :return: xml elements that contains urls
        """
        content = get_http_content(url)
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find_all("loc")
        return (_.text for _ in elements)

    def parse_xml(self, xml_elements):
        """
        Parse xml elements from get_elements_from_xml func

        :param xml_elements: elements containing urls
        :return: generator of urls
        """
        for url in xml_elements:
            if ".xml" in url:
                print("\x1b[32m✓\x1b[0m {}".format(url))
                sub_elements = self.get_elements_from_xml(url)
                for sub_url in sub_elements:
                    yield sub_url
            else:
                yield url

    def get_links(self, url):
        """
        Main loop. Takes domain url

        :param url: domain url
        :return: generator of site urls
        """
        xml_elements = self.get_elements_from_xml(url + '/sitemap.xml')
        return self.parse_xml(xml_elements)


if __name__ == "__main__":

    def prompt_to_save(result):
        """
        Prompts user to save the result to a file

        :param result: result of program execution
        """
        save_result = input("Save result to file?(y/n) ")
        if save_result in ("y", "Y"):
            filename = input("Name your file: ")
            with open(filename, "w") as f:
                f.write("\n".join(tuple(result)))

    user_input = input("Domain for extraction ('http://site.com'):\n")
    extractor = Sitemap()
    links = extractor.get_links(user_input)
    prompt_to_save(links)
