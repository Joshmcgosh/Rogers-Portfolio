from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
import os
import sqlite3

app = Flask(__name__)

db = SQL("sqlite:///container.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_PERMANENT"] = "filesystem"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def participants():
    rows = db.execute("SELECT * FROM participants")
    return render_template("participants.html", rows=rows)

@app.route("/contact-me", methods=["GET", "POST"]) 
def contact():
    if request.method == "GET":
        return render_template("contact-me.html")
    return redirect("/")

@app.route("/about-me")
def about():
    return render_template("about-me.html")