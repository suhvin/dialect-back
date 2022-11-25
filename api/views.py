import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
@api_view(['POST'])
def send_sms(request):     
    if request.method == 'POST':
        
        print("test")
        print(request.data) # PCD_PAY_RST
        data = request.data['PCD_PAY_RST'] # success
        print(data)
        # data = request.data['PCD_PAY_MSG'] # 카드승인완료

        account_sid = "AC0d50f72d5b699de30c6d2a7a84f823e5" # os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = "616c4481cbe4915ece4887ec54cd1203" #os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        client.messages.create(
            # body="Hi there!",
            body=data,
            from_="+19498326476",#os.getenv('PHONE_NUMBER'),
            to='+821085319070'
        )

        # print(request.data)
        # print(message._properties)
        
        return Response({"message": "Got some data!", "data": request.data})