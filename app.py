from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Dataset/drinkingdriving.sqlite"

db = SQLAlchemy(app)


class Danger(db.Model):
    __tablename__ = 'CrashesDC'

    LATITUDE = db.Column(db.Text, primary_key=True)
    LONGITUDE = db.Column(db.Text)
    REPORT_DATE = db.Column(db.Text)
    REPORT_TIME = db.Column(db.Text)
    DRIVERS_IMPAIRED = db.Column(db.Text)

    def __repr__(self):
        return '<CrashesDC %r>' % (self.name)

class Sunday(db.Model):
    __tablename__ = 'Sundays'

    SundayLaw = db.Column(db.Text, primary_key=True)
    Fatality = db.Column(db.Text)
    DUI = db.Column(db.Text)

    def __repr__(self):
        return '<Sundays %r>' % (self.name)


class LawEnforcement(db.Model):
    __tablename__ = 'PoliceperCapita'
    Year = db.Column(db.Text)
    State = db.Column(db.Text, primary_key=True)
    Police = db.Column(db.Text)
    Fatalities = db.Column(db.Text)

    def __repr__(self):
        return '<PoliceperCapita %r>' % (self.name)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/crash")
def crash_data():
    """test"""

    # query for the top 10 emoji data
    results = db.session.query(Danger.LATITUDE, Danger.LONGITUDE, Danger.REPORT_DATE, Danger.REPORT_TIME, Danger.DRIVERS_IMPAIRED).\
        order_by(Danger.REPORT_TIME.desc()).all()

    # Select the top 10 query results
    crash_data = {}

    for result in results:
        crash_data["State"] = result[0]
        crash_data["Police"] = result[1]
        crash_data["Fatalities"] = result[2]

    return jsonify(results)




@app.route("/police")
def police_data():
    """test"""

    # query for the top 10 emoji data
    results = db.session.query(LawEnforcement.State, LawEnforcement.Police, LawEnforcement.Fatalities).\
        order_by(LawEnforcement.Fatalities.desc()).all()

    # Select the top 10 query results
    police_data = {}

    for result in results:
        police_data["State"] = result[0]
        police_data["Police"] = result[1]
        police_data["Fatalities"] = result[2]

    return jsonify(results)


@app.route("/sunday")
def sunday_data():
    """test"""

    # query for the top 10 emoji data
    results = db.session.query(Sunday.SundayLaw, Sunday.Fatality, Sunday.DUI).\
        order_by(Sunday.Fatality.desc()).all()

    # Select the top 10 query results
    sunday_data = {}

    for result in results:
        sunday_data["State"] = result[0]
        sunday_data["Police"] = result[1]
        sunday_data["Fatalities"] = result[2]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
