import os
from datetime import datetime,timezone, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils.sendMessage import sendMessage


def payTicket(num, oid):
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")

    phone = oid[-11:]
    print(phone)
    db = firestore.client()
    data = db.collection(u'store').document(u'u'+phone)
    ticketNum = data.get().to_dict()['ticketPlus']
    ticketNum = ticketNum + num
    data.update({
    'ticketPlus' : ticketNum
    })
    sendMessage('payTicket', phone)