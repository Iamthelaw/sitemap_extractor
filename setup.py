from setuptools import setup


def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(
    name="sitemap extractor",
    version="0.1a",
    description="small script for extracting links from website sitemap.xml",
    long_description=readme(),
    keywords='sitemap',
    url="https://github.com/Iamthelaw/sitemap_extractor",
    author="Robotehnik",
    author_email="robotehnik@me.com",
    license="MIT",
    packages=["sitemap_extractor"],
    install_requires=['requests', 'beautifulsoup4'],
    include_package_data=True,
    zip_safe=False
)