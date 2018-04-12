from flask import Flask
from flask import render_template
from flask import url_for

import os.path

import classes

print (os.getcwd())
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/static/')

app = Flask(__name__)

@app.route("/")
def welcome():

    page = classes.Page("Welcome")
    page.add_keywords(["Tsumo", "Proverbs","Nyasha Bryan"])
    page.add_css(url_for("static", filename = "css/main.css"))
    return render_template('base.html', page= page)

@app.route("/tsumo/<int:tsumo_no>", methods = ['POST', 'GET'] )
def get_tsumo(tsumo_no):
    pass

