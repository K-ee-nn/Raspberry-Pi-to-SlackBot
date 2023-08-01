import slack
import os
from dotenv import load_dotenv
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# load your API token
env_path = '.env'
load_dotenv(env_path)
client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])

# send message to channel for 1000 times before breaking
count = 0
while count <= 1e3:
    datastring = "Hi"
    try:
        print(f"Try Writing {datastring} to channel...")
        client.chat_postMessage(channel="#test-channel", text=datastring)
    except Exception as e:
        print(e)
    count += 1
    time.sleep(2)

print("Program exited...")
