import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotenv import load_dotenv
from utils.getDate import getDate
from .pay.pay import pay
from .pay.payTicket import payTicket

load_dotenv()
@api_view(['POST'])
def send_sms(request):     
    if request.method == 'POST':
        
        goods = request.data['PCD_PAY_GOODS'] # success
        oid = request.data['PCD_PAY_OID'] # success
        date = getDate()
        if goods.find('티켓')==-1 :
            if goods.find('미팅')==-1 :
                pay('dating', oid, date)
            else :
                pay('meeting', oid, date)
        else :
            if goods.find('티켓1')!=-1 :
                payTicket(1, oid)
            elif goods.find('티켓3')!=-1 :
                payTicket(3, oid)
            elif goods.find('티켓5')!=-1 :
                payTicket(5, oid)
        
        return Response({"message": "Got some data!", "data": request.data})