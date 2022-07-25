from twilio.rest import Client
accountSID = 'XXXXXXXXXXXXXXXXX'
authToken = 'XXXXXXXXXXX'

twilioCli= Client(accountSID, authToken)
myTwilioNumber = '+1205XXXXXXX'
myCellPhone = '+1315XXXXXXX'

message = twilioCli.messages.create(body='Good morning Nathaniel. This message was sent to you through an app I built with code. This message was typed on my laptop lol.', from_=myTwilioNumber, to=myCellPhone)