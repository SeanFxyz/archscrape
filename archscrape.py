#!/bin/env python3

import sys
from bs4 import BeautifulSoup
from urllib import request

# Give an archive.org url, return an array of all download options
# for the document.
def scrape_page(url):
    with request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, features="html5lib")
        formats = soup.find_all("a", class_="format-summary download-pill")
        return [tag["href"] for tag in formats]

# Given a url, finds the download options, outputs file links as
# indicated by ftypes
def dl(url, ftypes=()):
    links = scrape_page(url)
    for l in links:
        if l.split(".")[-1] in ftypes:
            print("https://archive.org" + l)


if __name__ == "__main__":
    ftypes = ("pdf", "txt", "epub")
    for arg in sys.argv[1:]:
        dl(arg, ftypes)
