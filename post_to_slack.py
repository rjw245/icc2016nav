import time
import threading
import socket
from slackclient import SlackClient

time.sleep(10) #Wait for network to come up

token = "xoxp-16056318835-16059519302-21698417558-5250d51fec" # found at https://api.slack.com/web#authentication
sc = SlackClient(token)

tesla_channel = "C0MLP2U6S"

def send_ip():
	myip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in 
[socket.socket(socket.AF_INET, $
        ipstr = "TESLA'S IP: "+myip
        sc.rtm_send_message(tesla_channel,ipstr)

if sc.rtm_connect():
	send_ip()
	#Respond to user input in teslamsgs channel
	while True:
		events = sc.rtm_read()
		for e in events:
			if u'channel' in e and e[u'channel']==tesla_channel:
				if u'text' in e:
					send_ip()
		time.sleep(1)
else:
	print "Connection Failed, invalid token?"

