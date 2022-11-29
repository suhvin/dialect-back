import os

import pandas as pd
import numpy as np
from datetime import datetime,timezone, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from twilio.rest import Client

def do_something1():
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/firebase-secret.json")

    try:
        firebase_admin.initialize_app(cred)
        print("berlin")
    except:
        print("Already Connected something1")
    
    db = firestore.client()
    data = db.collection(u'flag').document(u'control')
    # data.update({
    # 'count' : 1005
    # })
    

    account_sid = 'AC6f1bf6220f2b6b824aaaf910b6dceb91' #os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = '552e48ec67679192356ac38d0be2410f' #os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=data.get().to_dict()['count'],
        from_="+15618213937",#os.getenv('PHONE_NUMBER'),
        to='+821085319070'
    )

def do_something2():
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/firebase-secret.json")

    try:
        firebase_admin.initialize_app(cred)
        print("tokyo")
    except:
        print("Already Connected something2")

    db = firestore.client()
    data = db.collection(u'flag').document(u'control')
    # data.update({
    # 'before' : 1005
    # })

    account_sid = 'AC6f1bf6220f2b6b824aaaf910b6dceb91' #os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = '552e48ec67679192356ac38d0be2410f' #os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=data.get().to_dict()['count'],
        from_="+15618213937",#os.getenv('PHONE_NUMBER'),
        to='+821085319070'
    )
