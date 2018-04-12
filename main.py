from flask import Flask
from flask import render_template
from flask import url_for

import os.path

import classes
import db

print (os.getcwd())
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/static/')

app = Flask(__name__)

@app.route("/")
def welcome():

    page = classes.Page("Welcome")
    page.add_keywords(["Tsumo", "Proverbs","Nyasha Bryan"])
    page.add_css("css/main.css")
    return render_template('base.html', page= page)

@app.route("/tsumo/<int:tsumo_no>")
def get_tsumo(tsumo_no):

    a_tsumo = db.get_tsumo(tsumo_no)

    page = classes.Page("Tsumo {0}".format(tsumo_no))
    page.add_css("css/main.css")
    page.tsumo = a_tsumo
    return render_template('tsumo.html', page = page)


