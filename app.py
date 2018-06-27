import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os

from flask import Flask, jsonify, render_template
app = Flask(__name__)

dbfile = os.path.join('drinkingdriving.sqlite')
engine = create_engine(f"sqlite:///{dbfile}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Crashes = Base.classes.CrashesDC
Police = Base.classes.PoliceperCapita
Sundays = Base.classes.Sundays

session = Session(engine)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/police")
def policeroute():
    return render_template('index.html')



if __name__ == "__main__":
        app.run()
