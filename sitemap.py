#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
" Sitemap parser
" by robotehnik
"""


import requests

from bs4 import BeautifulSoup


class Sitemap(object):

	""" Sitemap class """
	def __init__(self, url):
		super(Sitemap, self).__init__()
		self.url = url

	def get_xml(self, url):
		""" return an http response or status code """
		if url.startswith('http://'):
			r = requests.get(url)
		else:
			r = requests.get('http://' + url)
		if r.status_code == 200:
			return r.text
		else:
			return r.status_code

	def parse(self, content):
		""" parse xml with BS """
		if type(content) == int:
			return "Status code is: " + str(content)
		else:
			soup = BeautifulSoup(content, 'html.parser')
			loc = soup.find_all('loc')
			return tuple(item.text for item in loc)

	def links(self):
		"""
		main func returns tuple of all links
		or status code
		"""
		map_ = self.get_xml(self.url + "/sitemap.xml")
		if type(map_) == int:
			return "Status code: " + str(map_)
		else:
			list_of_links = self.parse(map_)
			if list_of_links[0].endswith('.xml'):
				result = tuple()
				for i, item in enumerate(list_of_links, 1):
					print("Parsing %d item: %s" % (i, item))
					item = self.get_xml(item)
					if type(item) == int:
						return "Status code is: " + str(item)
					else:
						result += self.parse(item)
				return result
			else:
				return list_of_links

	def exit(self, result):
		if 'Status' in result:
			print(result)
		else:
			print_result = input('Print all %d links to console?(y/n)' % len(result))
			if print_result == 'y':
				for love, u in enumerate(result, 1):
					print("%d. %s" % (love, u))
			save = input('Save result to file?(y/n)')
			if save == 'y':
				filename = input('Name your file: ')
				with open(filename, 'w') as f:
					f.write('\n'.join(result))

if __name__ == "__main__":
	inp = input("Domen for sitemap extraction: ")
	sm = Sitemap(inp)
	links = sm.links()
	sm.exit(links)