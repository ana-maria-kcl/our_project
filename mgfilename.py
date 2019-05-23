import requests

def send_simple_message(email):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxe33658a66c7d463a8855cc864355eaf1.mailgun.org/messages",
        auth=("api", "3525b933755ecceab47c9013a469ab4c-e566273b-25ecab3e"),
        data={"from": "Excited User <https://api.mailgun.net/v3/sandboxe33658a66c7d463a8855cc864355eaf1.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

send_simple_message("winnettestluce@gmail.com")
