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

    import sitemap_extractor

    # class initialisation
    extractor = sitemap_extractor()

    # grab some links from desired domain
    links = extractor.get_links("http://mysite.com")

    # optional - saveresult to a file
    extractor.save_to_file(links, "myfile.txt")
