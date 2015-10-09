#!/usr/bin/env python3
from flask import Flask, render_template, request
from core.comparer import compare
from core import board
from core.oj.oj import get_url
import json
app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/comparer")
def comparer():
	return render_template("comparer.html")

@app.route("/comparer/<expression>")
def comparer_api(expression):
	result = list(compare(expression))
	result.sort()
	process = lambda prob: {"judge":prob[0], "pname":str(prob[1]), "url":get_url(prob)}
	result = list(map(process, result))
	return json.dumps(result)

@app.route("/board/api",methods=["POST","GET"])
def board_api():
	users = json.loads(request.values.get("users"))
	probs = json.loads(request.values.get("probs"))
	timeout = int(request.values.get("timeout"))
	force_fetch = request.values.get("force_fetch")
	return json.dumps(board.fetch_auto((users,probs),timeout,force_fetch))

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0",port=49808)
