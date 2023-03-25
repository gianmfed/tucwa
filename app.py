from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    """Show basic information about today's time spent on devices"""
    with sqlite3.connect("time.db") as con:
        db = con.cursor()
        # Load time from database
        time = db.execute("SELECT seconds FROM time_table WHERE date = ?", (date.today(),))
        time = time.fetchone()

        # Case if time.py is not activated
        if time == None:
            time = 0
        else:
            time = int(time[0]/60)
        
        return render_template("index.html", time=time)

rdays = 0 # Range of days to show in history
@app.route("/history", methods=["GET", "POST"])
def history():
    """Show history of device usage"""
    global rdays
    if request.method == "POST":
        rdays = request.form.get("drange")
        return redirect("/history")
    else:
        with sqlite3.connect("time.db") as con:
            db = con.cursor()
            # Check haw many days there are in the database
            nentries = db.execute("SELECT count(date) FROM time_table")
            nentries = nentries.fetchone()[0]

            if rdays == 0:
                rdays = nentries
            else:
                rdays = int(nentries) - int(rdays) + 1

            hist = db.execute("SELECT * FROM time_table ORDER BY date DESC LIMIT ?", (rdays,))
            hist = hist.fetchall()
            hist.reverse()
            rdays = 0
            return render_template("history.html", history = hist, nentries = nentries)