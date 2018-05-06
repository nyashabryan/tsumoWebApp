from flask import Flask
from flask import render_template
from flask import url_for

import os.path

import classes
import db

print (os.getcwd())
STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/static/')

app = Flask(__name__)

# The Welcome to Page Method
@app.route("/")
def welcome():

    """
    The Route Method to produce the Welcome page.
    :return: returns the rendered Welcome page. 
    """

    page = classes.Page("Welcome")
    return render_template('base.html', page= page)

# The Tsumo routing Method for showing a single tsumo

@app.route("/tsumo/<int:tsumo_no>")
def get_tsumo(tsumo_no):
    """
    Route Method to render any of the Tsumo pages depending on the 
    tsumo number. It calls the database from the db module to pull a tsumo at a particular
    number. It then renders a tsumo page using the defined templates. 

    :param tsumo_no: number of the tsumo in the database.
    :type tsumo_no: int
    :return: returns the rendered page with the tsumo. 
    """

    page = classes.Page("Tsumo {0}".format(tsumo_no))
    
    page.tsumo = db.get_tsumo(tsumo_no)

    return render_template('tsumo.html', page = page)


