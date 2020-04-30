#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template, request
import code

import api_calls
import functools
import json
import os

import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import googleOauth

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(googleOauth.app)

# the good stuff

@app.route("/")
def home():
    if googleOauth.is_logged_in():
        return redirect('/main/')
    else:
        return redirect('/login/')

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/preferences/")
def pref():
    return render_template("preference_page.html")

@app.route("/main/")
def main_page():
    return render_template("main_page.html")

@app.route("/register/")
def register():
    return render_template("result_page.html")


@app.route("/info/", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        location = request.form["origins"]
        departure = request.form["departureDate"]
        duration = request.form["duration"]
        budget = request.form["budget"]
        # function for location -> ISO code
        # departure: mm-dd-yyyy -> yyyy-mm-dd
        # return date -> departure-return
        # 2d_list = api_call(loc, dep, dur, budget) 
        departureYear = departure[6:]
        departureMonth = departure[0:2]
        departureDay = departure[3:5]
        departure = "" + departureYear + "-" + departureMonth + "-" + departureDay
        # output = api_calls(location, departure, duration, budget)
        arr = [["2020-08-23"], ["$300"], ["Hello"]]
        return render_template("result_page.html", data=arr)
        # return redirect((url_for("user", loc = location, country = location, crr = 300, budget = 500)))
        #return redirect(url_for("user", loc = lc, country = ct))
    
    else:
        return render_template("info.html")

@app.route("/results/<string:loc>/<string:country>/<float:crr>/<int:budget>")
def user(loc, country, crr, budget):
    return "<p> You are in {loc} and you want to go to {country} </p> <p> The currency of {country} is at {crr}, so your budget is: {budget}</p>"
if __name__ == "__main__":
    app.run()