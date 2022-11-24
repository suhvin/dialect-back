import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
@api_view(['POST'])
def send_sms(request):     
    if request.method == 'POST':
        
        # pay_msg = request.PCD_PAY_MSG
        data = request.data
        # print(request.data['PCD_PAY_MSG'])

        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        client.messages.create(
            # body="Hi there!",
            body=data,
            from_=os.getenv('PHONE_NUMBER'),
            to='+821040302748'
        )

        # print(request.data)
        # print(message._properties)
        
        return Response({"message": "Got some data!", "data": request.data})