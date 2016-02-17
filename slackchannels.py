import time
from slackclient import SlackClient

token = "xoxp-16056318835-16059519302-21698417558-5250d51fec" # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"

