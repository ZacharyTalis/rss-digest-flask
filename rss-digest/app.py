#!/usr/bin/env python3

from flask import Flask, request, redirect, send_file
# from urllib import parse
from waitress import serve

app = Flask(__name__)

@app.route("/")
def main():

    # # If no URL args, return a non-error page
    # if (len(request.args.keys()) == 0):
    #     return ("<a href='https://github.com/ZacharyTalis/search-handler-flask/'>search-handler-flask</a>", 200)

    # # Get URL args
    # url = request.args.get("url", "")
    # rawSubs = parse.unquote(request.args.get("subs", "")).split(",")
    # subs = {}

    # try:
    #     # Split rawSubs into a dictionary
    #     for rawSub in rawSubs:
    #         rawSub = rawSub.split("~")
    #         subs[rawSub[0]] = rawSub[1]
    #     # Perform URL subs
    #     for sub in subs.keys():
    #         url = url.replace(sub, subs[sub])
    # except:
    #     # Request malformed or missing args
    #     return ("Request malformed or missing args!", 400)

    # print(rawSubs)
    # print(subs)
    # print(url)
    # return redirect(url, code=303)
    return "init"

@app.route("/.well-known/gpc.json")
def wellKnown():
    return send_file("static/gpc.json", mimetype="application/json")

if __name__ == "__main__":
    serve(app)
