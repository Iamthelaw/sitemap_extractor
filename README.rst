======================
Sitemap Extractor 5000
======================

This is my training module for extracting links from site's sitemaps

Very useful in SEO, if you know what I mean. This is just for learning purposes.
So, this little ( ~100 lines of code) script takes any domain and returns links from it's sitemap xml-structure. It goes as deep as it need.
Feel free to write a codereview :)

Usage:
------

Import module
.. code-block:: python
    >>> import sitemap_extractor

Initialize class
.. code-block:: python
    >>> extractor = sitemap_extractor()

Grab links from desired domain
.. code-block:: python
    >>> links = extractor.get_links("http://mysite.com")

Optional - save results to file
.. code-block:: python
    >>> extractor.save_to_file(links, "myfile.txt")
