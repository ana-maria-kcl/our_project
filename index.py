from flask import Flask, render_template, request, redirect
import requests

from quiz import choose_country
from mgfilename import send_simple_message
from apiret import generate_key

app = Flask("travelling")

api_key = generate_key()

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
    personal_data = request.form
    send_simple_message(personal_data["email"])
    return redirect(request.referrer)

def send_simple_message(email):
    print(f"I SENT YOU AN EMAIL {request.form['email']}")
    print(api_key)
    return requests.post(
      "https://api.mailgun.net/v3/sandbox2e97bfad21db449b811b676424e904c2.mailgun.org/messages",
       #auth=("api", "3525b933755ecceab47c9013a469ab4c-e566273b-25ecab3e"),
       auth=("api", api_key),
       data={"from": "Excited User <aunahine@sun.ru>",
             "to": [email],
             "subject": "Your perfect holiday!",
             "text": "Thank "})

app.run(debug=True)
