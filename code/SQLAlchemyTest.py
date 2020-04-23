import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "infodatabase.db"))



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)



@app.route("/")


#this might be wrong
def info():
	if request.form:
	    origin = Search(title=request.form.get("origin"))
	    db.session.add(origin)
	    db.session.commit()
	    departureDate = Search(title=request.form.get("departureDate"))
	    db.session.add(departureDate)
	    db.session.commit()
	    returnDate = Search(title=request.form.get("returnDate"))
	    db.session.add(returnDate)
	    db.session.commit()
	    budget = Search(title=request.form.get("budget"))
	    db.session.add(budget)
	    db.session.commit()
	return render_template("info.html")

"""
class User(db.model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.column(db.String(35), nullable=False)
	password = db.Column(db.String(35), nullable=False)
	searches = db.relationship('Search', lazy=True)

	def __repr__(self):
		return "User('{self.email}')"
"""
class Search(db.Model):
	SearchID = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String(35), nullable=False)
	departureDate = db.Column(db.DateTime, nullable=False)#, default=DateTime.utcnow)
	returnDate = db.Column(db.DateTime, nullable=False)#, default=DateTime.utcnow)
	budget = db.Column(db.Integer, nullable=False)
	#user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Search('{self.origin}', '{self.departureDate}', '{self.returnDate}', '{self.budget}') "

