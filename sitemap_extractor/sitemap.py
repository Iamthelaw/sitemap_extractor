#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module SitemapExtractor

:copyright: robotehnik@me.com
:license:
"""

import requests
from bs4 import BeautifulSoup

# TODO:
# - place get_xml_from_url outside main content
# - recursive xml parsing is insecure, make limits
# - grab_links needs refactoring


class Sitemap(object):
    """
    Class for OOP skills test
    """

    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_xml_from_url(url):
        """
        Get content of xml file by url

        :param url: url of xml file
        :return: content of xml file or status code
        """
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            print("""Possible DNS failture or connection was refused.
                  Connection Error""")
        except requests.HTTPError:
            print("""Invalid HTTP response. HTTPError""")
        except requests.Timeout:
            print("""Connection Timeout!""")
        except requests.TooManyRedirects:
            print("""Too Many Redirects Error""")
        except Exception as e:
            print("During execution error was revealed:\n{}".format(e))
        else:
            if r.status_code == 200:
                return r.text
            else:
                print("Bad Status Code: {}\n{}".format(r.status_code, url))
        exit(1)

    def parse_links(self, content):
        """
        Recursive extracting urls from xml files

        :param content: content of first xml file
        :return: generator of links
        """
        soup = BeautifulSoup(content, "html.parser")
        xml_elements = soup.find_all("loc")
        for el in xml_elements:
            url = el.text
            if '.xml' in url:
                print("\x1b[32m✓\x1b[0m {}".format(url))
                content = self.get_xml_from_url(url)
                sub = self.parse_links(content)
                for _ in sub:
                    yield _
            else:
                yield url

    def grab_links(self):
        """
        Main loop of this class

        :return: result generator
        """
        xml_content = self.get_xml_from_url(self.url + "/sitemap.xml")
        return self.parse_links(xml_content)

    @staticmethod
    def prompt_to_save(result):
        """
        Prompt user to save the result to a file

        :param result: result of program execution
        :return: nothing
        """
        save_result = input("Save result to file?(y/n)")
        if save_result == "y":
            filename = input("Name your file: ")
            with open(filename, "w") as f:
                f.write("\n".join(result))
        exit(0)

if __name__ == "__main__":
    user_input = input("Domain for sitemap extraction: ")
    s = Sitemap(user_input)
    links = s.grab_links()
    s.prompt_to_save(links)
