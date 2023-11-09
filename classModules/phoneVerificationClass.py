from twilio.rest import Client

account_sid = 'AC6f952777b9d7ffa1433f7d575b96df67'
auth_token = '709d6f79dc520e1f8589e12de5398330'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14404244083',
  body='Hi, fuck you',
  to='+918147254312'
)

print(message.sid)