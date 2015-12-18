======================
Sitemap Extractor 5000
======================

This is my training module for extracting links from site's sitemaps

Very useful in SEO, if you know what I mean. This is just for learning purposes.
So, this little ( ~120 lines of code ) script takes any domain and returns links from it's sitemap xml-structure.

Feel free to write a codereview :)

Usage:
------

Import module
    >>> from sitemap_extractor import Sitemap()

Class initialisation
    >>> extractor = Sitemap()

Grab some links from desired domain
    >>> links = extractor.get_links("http://mysite.com")

Optional - save result to a file
    >>> extractor.save_to_file(links, "myfile.txt")
