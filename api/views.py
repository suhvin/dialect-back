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

        account_sid = 'AC6f1bf6220f2b6b824aaaf910b6dceb91' #os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = '552e48ec67679192356ac38d0be2410f' #os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=data,
            from_="+15618213937",#os.getenv('PHONE_NUMBER'),
            to='+821085319070'
        )

        print(message)

        # print(request.data)
        # print(message._properties)
        
        return Response({"message": "Got some data!", "data": request.data})