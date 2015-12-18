======================
Sitemap Extractor 5000
======================

This is my training module for extracting links from site's sitemaps

Very useful in SEO, if you know what I mean. This is just for learning purposes.
So, this little ( ~100 lines of code) script takes any domain and returns links from it's sitemap xml-structure. It goes as deep as it need.
Feel free to write a codereview :)

Usage:
------

.. code-block:: python
    import sitemap_extractor as SE

    # init class
    extractor = SE()

    # get links
    links = extractor.get_links("http://mysite.com")

    # optional - save result
    extractor.save_to_file(links, "myfile.txt")

