import slack
import os
from dotenv import load_dotenv
import time
import serial

# initialize serial port
serial1 = serial.Serial('/dev/ttyUSB0', 9600)

# load your API token
env_path = '.env'
load_dotenv(env_path)
client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])

# send message to channel
count = 0
while count <= 1e3:
    datastring = serial1.readline()
    try:
        client.chat_postMessage(channel="#test-channel", text=str(datastring))
    except Exception as e:
        print(e)
    count += 1
    time.sleep(2)
serial.close()
