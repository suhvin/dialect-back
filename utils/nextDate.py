import os
from datetime import datetime,timezone, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def nextDate():
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")
    
    db = firestore.client()
    data = db.collection(u'admin').document(u'control')
    before = data.get().to_dict()['date']
    after = before + timedelta(days=1)
    data.update({
    'date' : after
    })
    return(after)
    