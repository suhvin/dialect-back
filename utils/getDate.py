import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def getDate():
    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")
    
    db = firestore.client()
    data = db.collection(u'admin').document(u'control')
    return(data.get().to_dict()['date'])
    