from flask import render_template, session
import psycopg2
from psycopg2.extras import DictCursor

import serverTest


def display():
    return render_template("root.html", title="Hellow")
