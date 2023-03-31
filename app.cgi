#!/usr/bin/python3
from urllib.robotparser import RequestRate
from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request

import psycopg2
import psycopg2.extras
import root
import inventory

## SGBD configs
DB_HOST = "db.tecnico.ulisboa.pt"
DB_USER = "istnumber"
DB_DATABASE = DB_USER
DB_PASSWORD = "password"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (
    DB_HOST,
    DB_DATABASE,
    DB_USER,
    DB_PASSWORD,
)

app = Flask(__name__)

@app.route("/")
def root_display():
    try:
        return root.display()
    except Exception as e:
        return str(e)  # Renders a page with the error.

@app.route("/inventory", methods=["GET"])
def inventory():
    steamid = request.args.get('steamid') or None
    return inventory.display(steamid)

CGIHandler().run(app)
