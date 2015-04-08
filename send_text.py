from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "{{}}"
auth_token  = "{{}}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Ron Burgandy?",
    to="+#########",    # Replace with your phone number
    from_="+#########") # Replace with your Twilio number
print message.sid
