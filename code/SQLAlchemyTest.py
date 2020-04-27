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
	departureDate = db.Column(db.String(12), nullable=False)#, default=DateTime.utcnow) #dateTime / date was giving issues
	returnDate = db.Column(db.String(12), nullable=False)#, default=DateTime.utcnow) #dateTime / date was giving issues
	budget = db.Column(db.Integer, nullable=False)
	#user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __init__(self, origin, departureDate, returnDate, budget):
		self.origin = origin
		self.departureDate = departureDate
		self.returnDate = returnDate
		self.budget = budget

	def __repr__(self):
		return "<origin: {}, departureDate: {}, returnDate: {}, budget: {}>".format(self.origin, self.departureDate, self.returnDate, self.budget)


@app.route("/", methods=["GET", "POST"])
def info():
	searches = None
	if request.form:
		try:
			origin = request.form['origin']
			departureDate = request.form['departureDate']
			returnDate = request.form['returnDate']
			budget = request.form['budget']
			searches = Search(origin, departureDate, returnDate, budget)
			db.session.add(searches)
			db.session.commit()
		except Exception as e:
			print("Failed to add search")
			print(e)
	searches = Search.query.all()
	return render_template("info.html", searches = searches)

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)


"""
@app.route('/')
def Info():
	all_data = Search.query.all()
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




"""
class User(db.model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.column(db.String(35), nullable=False)
	password = db.Column(db.String(35), nullable=False)
	searches = db.relationship('Search', lazy=True)

	def __repr__(self):
		return "User('{self.email}')"
"""
