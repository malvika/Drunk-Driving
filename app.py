import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from flask_sqlalchemy import SQLAlchemy

from flask import (Flask, jsonify, render_template, request, redirect)

# Flask Setup
app = Flask(__name__)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Dataset/drinkingdriving.sqlite"

db = SQLAlchemy(app)

# Define our classes


# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# Crashes = Base.classes.CrashesDC
# Police = Base.classes.PoliceperCapita
# Sundays = Base.classes.Sundays

# session = Session(engine)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/police")
def policeroute():

    return 



if __name__ == "__main__":
        app.run()
