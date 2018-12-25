from twilio.rest import Client
import os

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)

# making sure to use E.164 formatting:
# [+][country code][phone number including area code]
user_phone = input("Please input your phone number")

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15072600733',
                     to=user_phone
                 )

print(message.sid)