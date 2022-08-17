#!/usr/bin/env python3

import utils.handler
import dateutil.parser
from email.utils import formatdate
from flask import Flask, Response, request, render_template, send_file, url_for
from waitress import serve


app = Flask(__name__)

@app.route("/")
def main():

    try:
        # If no URL args, return the URL builder page
        if (len(request.args.keys()) == 0):
            return render_template("index.html", baseUrl=url_for("main"), builderScript= url_for("static", filename="js/builder.js"), icon=url_for("static", filename="img/icon.svg"), stylesheet=url_for("static", filename="css/style.css"))

        # Get URL args
        url = request.args.get("url", None)
        feedDescription = request.args.get("feed-description", None)
        feedIcon = request.args.get("feed-icon", ("." + url_for("static", filename="img/icon.png")))
        feedIconAlt = request.args.get("feed-icon-alt", None)
        feedTitle = request.args.get("feed-title", "Untitled Feed")
        itemTitle = request.args.get("item-title", "Untitled Item")
        latest = request.args.get("latest", None)
        if (latest):
            latest = int(latest)

        # Define another Jinja arg
        pubDate = formatdate()

        # Fill in item title date wildcard
        itemTitle = itemTitle.replace("_date", pubDate[0:-15])

        # Get articles dictionary
        root = utils.handler.getRootFromRssUrl(url)
        articles = utils.handler.getArticlesFromRoot(root, dateutil.parser.parse(pubDate).timestamp(), latest)
        dates = sorted(list(articles.keys()))
        
        # Return RSS file
        return Response(render_template("rss.xml", articles=articles, dates=dates, feedDescription=feedDescription, feedIcon=feedIcon, feedIconAlt=feedIconAlt, feedTitle=feedTitle, itemTitle=itemTitle, latest=latest, pubDate=pubDate, rssUrl=url, url=url), mimetype="application/xml")
    except:
        # Request malformed or missing args
        return ("Request malformed or missing args!", 400)


@app.route("/.well-known/gpc.json")
def wellKnown():
    return send_file("static/gpc.json", mimetype="application/json")


if __name__ == "__main__":
    serve(app)
