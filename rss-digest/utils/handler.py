#!/usr/bin/env python3

import email.utils
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

import dateutil.parser
import requests


# An individual article for the digest
class Article:
    def __init__(self, updated=None, link=None, title=None, summary=None):
        self.updated = updated
        self.link = link
        self.title = title
        self.summary = summary

    def __repr__(self) -> str:
        return f'< Article "{self.title}" >'


# Parser used for cleaning up RSS summaries
class HandlerHtmlParser(HTMLParser):
    def __init__(self):
        self._body = None
        HTMLParser.__init__(self)

    def handle_data(self, data):
        if not self._body:
            self._body = data

    def getBody(self):
        return self._body

    body = property(getBody, handle_data)


# Take the URL of some RSS file and return its XML root
def getRootFromRssUrl(url):
    contents = requests.get(url, headers={"User-Agent": "rss-digest-flask/1.0.0"}).text
    root = ET.fromstring(contents)
    # Handle XML vs RSS hierarchy difference
    if list(root)[0].tag == "channel":
        root = list(root)[0]
    return root


# Clean up any RSS summary that happens to be HTML
def cleanSummaryIfHtml(summary):
    try:
        parser = HandlerHtmlParser()
        parser.feed(summary)
        summary = parser.body
    except BaseException:
        # Summary isn't HTML
        pass
    return summary


# Take an XML root and return the corresponding date->Article dictionary
def getArticlesFromRoot(root, currentTime, latest):
    subchildTags = ["updated", "link", "title", "summary"]
    subchildAlts = {"pubDate": "updated", "description": "summary"}
    articles = {}

    for child in root:
        if list(filter(child.tag.endswith, ["entry", "item"])):
            tempArticle = {}
            for subchild in child:
                # Check if tag pertains to an Article property we'd like to store
                match = list(
                    filter(
                        subchild.tag.endswith, subchildTags + list(subchildAlts.keys())
                    )
                )
                if match:
                    # We can safely snag the first (presumably only) item in the match list
                    match = match[0]

                    # If match is XML-style link, grab the href as link
                    if match == "link" and subchild.tag != "link":
                        tempArticle[match] = subchild.attrib["href"]
                    # If match is RSS-style tag, grab for the appropriate Article attribute
                    elif match in subchildAlts.keys():
                        # Before grabbing a pubDate, convert to a sortable timestamp string
                        if match == "pubDate":
                            tempArticle["updated"] = str(
                                email.utils.parsedate_to_datetime(subchild.text)
                            )
                        else:
                            tempArticle[subchildAlts[match]] = subchild.text
                    # Grab normally
                    else:
                        tempArticle[match] = subchild.text

            # Clean up summary
            if "summary" in tempArticle.keys():
                tempArticle["summary"] = cleanSummaryIfHtml(tempArticle["summary"])

            # Check if updated time is within latest - if so, add to articles dictionary
            article = Article(**tempArticle)
            if not latest or (
                currentTime - dateutil.parser.parse(article.updated).timestamp()
                <= latest
            ):
                # Splatty-splat expansion
                articles[article.updated] = article

    return articles
