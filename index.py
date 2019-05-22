from flask import Flask, render_template, request, redirect
import requests

from quiz import choose_country

app = Flask("travelling")


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/quiz", methods=["POST"])
def travel_quiz():
    quiz_data = request.form
    country = choose_country(quiz_data)
    return render_template(f"{country}.html")

@app.route("/email", methods=["POST"])
def send_email():
    # actually send the email somehow
    # to test: print(f"I SENT YOU AN EMAIL {request.form['email']}")
    return redirect(request.referrer)

app.run(debug=True)
