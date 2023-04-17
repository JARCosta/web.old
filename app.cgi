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
import utils
import prices

app = Flask(__name__)

@app.route("/")
def root_display():
    return root.display()

@app.route("/inventory", methods=["GET"])
def inventory_display():
    steamid = request.args.get('steamid') or None
    return inventory.test(steamid)

@app.route("/inventory/update", methods=['POST'])
def inv_update():
    try:
        steamid = request.form["steamid"]
        json = request.form["json"] or None
        return inventory.update(steamid, json)
    except Exception as e:
        return str(e)

@app.route("/prices")
def prices_display():
    try:
        return prices.display()
    except Exception as e:
        return str(e)

CGIHandler().run(app)
