#!/usr/bin/python3
from urllib.robotparser import RequestRate
from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request


import psycopg2
import psycopg2.extras
import root
import inventory
import serverTest

app = Flask(__name__)

@app.route("/")
def root_display():
    return root.display()

@app.route("/inventory", methods=["GET"])
def inventory_display():
    steamid = request.args.get('steamid') or None
    return inventory.test(steamid)

CGIHandler().run(app)
