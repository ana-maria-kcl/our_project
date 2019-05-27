from flask import Flask, render_template, request, redirect
import requests

from quiz import choose_country
from mgfilename import send_simple_message
from weather import get_weather

app = Flask("travelling")

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/quiz", methods=["POST"])
def travel_quiz():
    quiz_data = request.form
    country = choose_country(quiz_data)
    return redirect(f"/country/{country}")

@app.route("/country/<country>")
def display_country(country):
    return render_template(f"{country}.html", weather=get_weather(country))


@app.route("/email", methods=["POST"])
def send_email():
    personal_data = request.form
    send_simple_message(personal_data["email"])
    return redirect(request.referrer)

app.run(debug=True)
