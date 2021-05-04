import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

SLACK_TOKEN = os.getenv('SLACK_OAUTH_TOKEN')        # read SLACK OAUTH TOKEN value from .env

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

post_message(SLACK_TOKEN,"#crypto","HI")