import email.utils
import urllib.request
import xml.etree.ElementTree as ET


# An individual article for the digest
class Article:
    
    def __init__(self, updated=None, link=None, title=None, summary=None):
        self.updated = updated
        self.link = link
        self.title = title
        self.summary = summary

    def __repr__(self) -> str:
        return f"< Article \"{self.title}\" >"


# Take an XML root and return a date->Article dictionary
def getArticlesFromRoot(root):

    subchildTags = ["updated", "link", "title", "summary"]
    subchildAlts = {"pubDate": "updated", "description": "summary"}

    for child in root:
        tempArticle = {}
        if (list(filter(child.tag.endswith, ["entry", "item"]))):
            for subchild in child:
                match = list(filter(subchild.tag.endswith, subchildTags + list(subchildAlts.keys())))

                if (match):

                    # We can safely snag the first (presumably only) item in the match list
                    match = match[0]

                    # If match is XML-style link, grab the href as link
                    if (match == "link" and subchild.tag != "link"):
                        tempArticle[match] = subchild.attrib["href"]
                    # If match is RSS-style tag, grab for the appropriate Article attribute
                    elif (match in subchildAlts.keys()):
                        # Before grabbing a pubDate, convert to a sortable timestamp string
                        if (match == "pubDate"):
                            tempArticle["updated"] = str(email.utils.parsedate_to_datetime(subchild.text).timestamp())
                        else:
                            tempArticle[subchildAlts[match]]= subchild.text
                    # Grab normally
                    else:
                        tempArticle[match] = subchild.text

            # Splatty-splat expansion
            article = Article(**tempArticle)
            articles[article.updated] = article


contents = urllib.request.urlopen("https://zacharytalis.com/blog/feed.xml").read()
root = ET.fromstring(contents)

# Handle XML vs RSS hierarchy difference
if (list(root)[0].tag == "channel"):
    root = list(root)[0]

# Get articles dictionary
articles = getArticlesFromRoot(root)

# Print list of articles
for date in sorted(list(articles.keys())):
    print(articles[date])
