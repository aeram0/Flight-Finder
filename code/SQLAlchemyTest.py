import os

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "infodatabase.db"))



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Search(db.Model):
	SearchID = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String(35), nullable=False)
	departureDate = db.Column(db.DateTime, nullable=False)#, default=DateTime.utcnow)
	returnDate = db.Column(db.DateTime, nullable=False)#, default=DateTime.utcnow)
	budget = db.Column(db.Integer, nullable=False)
	#user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __init__(self, origin, departureDate, returnDate, budget):
		self.origin = origin
		self.departureDate = departureDate
		self.returnDate = returnDate
		self.budget = budget


@app.route('/')
def Info():
	all_data = Search.query.all()
#check this
	return render_template("info.html", searches = all_data)


#inserting data to sql database via html forms
@app.route('/insert', methods=['POST'])

def insert():
	if request.method == 'POST':
		origin = request.form('origin')
		departureDate = request.form('departureDate')
		returnDate = request.form('returnDate')
		buget = request.form('budget')

		mySearches = Search(origin, departureDate, returnDate, budget)
		db.session.add(mySearches)
		db.session.commit()

		return redirect(url_for('Info'))

if __name__ == "__main__":
    app.run(debug=True)

"""
def info():
	if request.form:
	    origin = Search(origin=request.form.get("origin"))
	    db.session.add(origin)
	    db.session.commit()

	    departureDate = Search(title=request.form.get("departure_date"))
	    db.session.add(departureDate)
	    db.session.commit()

	    returnDate = Search(title=request.form.get("return_date"))
	    db.session.add(returnDate)
	    db.session.commit()

	    budget = Search(title=request.form.get("budget"))
	    db.session.add(budget)
	    db.session.commit()
	return render_template("info.html")


"""



"""
class User(db.model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.column(db.String(35), nullable=False)
	password = db.Column(db.String(35), nullable=False)
	searches = db.relationship('Search', lazy=True)

	def __repr__(self):
		return "User('{self.email}')"
"""
