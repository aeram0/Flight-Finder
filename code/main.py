#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template, request
import code
app = Flask(__name__)


# the good stuff
import currencies
def backend(country, location, weather, inbound, outbound, people, budget):
    # right now country is only one. We have to do something to change it into multiple countries
    print(currencies.finding_currency(location, country))
    crr = currencies.finding_currency(location, country)
    actual_budget = crr * int(budget)
    return crr, int(actual_budget)

@app.route("/")
def home():
    return render_template("loginform.html")

@app.route("/register/")
def register():
    return render_template("registerform.html")


@app.route("/info/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        ct = request.form["countries"]
        lc = request.form["location"]
        wt = request.form["weather"]
        inb = request.form["inbound"]
        out = request.form["outbound"]
        ppl = request.form["people"]
        bud = request.form["budget"]
        total = backend(ct, lc, wt, inb, out, ppl, bud)
        return redirect((url_for("user", loc = lc, country = ct, crr = total[0], budget = total[1])))
        #return redirect(url_for("user", loc = lc, country = ct))
    else:
        return render_template("info.html")

@app.route("/results/<string:loc>/<string:country>/<float:crr>/<int:budget>")
def user(loc, country, crr, budget):
    return f"<p> You are in {loc} and you want to go to {country} </p> <p> The currency of {country} is at {crr}, so your budget is: {budget}</p>"
if __name__ == "__main__":
    app.run()


