import os

import pandas as pd
import numpy as np
from datetime import datetime,timezone, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
    data.update({
    'count' : 1004
    })

def do_something2():
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/firebase-secret.json")

    try:
        firebase_admin.initialize_app(cred)
        print("tokyo")
    except:
        print("Already Connected something2")
