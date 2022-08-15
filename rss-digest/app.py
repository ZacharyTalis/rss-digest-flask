#!/usr/bin/env python3

import utils.handler
from flask import Flask, Response, request, render_template, send_file
from waitress import serve

app = Flask(__name__)

@app.route("/")
def main():

    # If no URL args, return a non-error page
    if (len(request.args.keys()) == 0):
        return ("<a href='https://github.com/ZacharyTalis/rss-digest-flask/'>rss-digest-flask</a>", 200)

    # Get URL args
    url = request.args.get("url", "")

    # Get articles dictionary
    root = utils.handler.getRootFromRssUrl(url)
    articles = utils.handler.getArticlesFromRoot(root)

    dates = sorted(list(articles.keys()))
    title = "TK"
    
    # Return RSS file
    return Response(render_template("rss.xml", articles=articles, dates=dates, title=title), mimetype="application/xml")


@app.route("/.well-known/gpc.json")
def wellKnown():
    return send_file("static/gpc.json", mimetype="application/json")


if __name__ == "__main__":
    serve(app)
