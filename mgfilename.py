import requests
from apiret import generate_key

api_key = generate_key()

def send_simple_message(email):
    print(f"I SENT YOU AN EMAIL {email}")
    print(api_key)
    return requests.post(
      "https://api.mailgun.net/v3/sandbox2e97bfad21db449b811b676424e904c2.mailgun.org/messages",
       #auth=("api", "3525b933755ecceab47c9013a469ab4c-e566273b-25ecab3e"),
       auth=("api", api_key),
       data={"from": "Your travel advisor <sunshine@sun.com>",
             "to": [email],
             "subject": "Your perfect holiday!",
             "text": "Thank you for subscribing for our newsletter. We will keep you up-to-date with all hot deals, trendy travel destinations and inspiring ideas for your vacation."})
