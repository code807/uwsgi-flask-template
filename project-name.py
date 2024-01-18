#
# coding=utf-8

from flask import Flask
from flask import request, jsonify
import asyncio
import requests

app = Flask(__name__)

@app.route("<endpoint>", methods=['GET', 'POST'])
async def handle():
    if request.method == "POST":
        return "POST"
    if request.method == "GET":
        return "GET"


if __name__ == "__main__":
	app.run(host='0.0.0.0')
