from twilio.rest import Client
from .sendMessageText import sendMessageText

def sendMessage(type, phone):

    account_sid = 'AC0d50f72d5b699de30c6d2a7a84f823e5' #os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = '616c4481cbe4915ece4887ec54cd1203' #os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=sendMessageText(type),
        from_="+19498326476",#os.getenv('PHONE_NUMBER'),
        to=phone.replace('010','+8210')
    )