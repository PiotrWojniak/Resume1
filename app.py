"""Imports"""
import os

from flask import (
    Flask, flash, redirect, render_template,
    request, session, url_for)
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/get_course")
def get_course():
    course = list(mongo.db.course.find().sort("added", 1))
    course.reverse()
    return render_template("course.html", course=course)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "8000")),
            debug=False)
