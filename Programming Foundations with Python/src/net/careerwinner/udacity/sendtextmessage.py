'''
Created on Aug 15, 2016

@author: Andy Zhang
'''
from twilio.rest import TwilioRestClient


account_sid = "{{ ACcd1745caea39a5ce57647515f9fdfef4 }}" # Your Account SID from www.twilio.com/console
auth_token  = "{{ 7bf4017694b1c4d90e1fdf5e00597c8c }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",to="+8618518905369",from_="+13158832586") # Replace with your Twilio number

# print(message.sid)
