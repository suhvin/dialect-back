import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils.sendMessage import sendMessage
from utils.diffDate import diffDate


def inActive(type, date):

    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")

    db = firestore.client()
    docs = db.collection(type+'Mate').stream()

    inActiveList = []
    for doc in docs:
        data = doc.to_dict()
        isProfile = data['dateProfile'] != None and diffDate(data['dateProfile'], date) == 1
        noCheck = data['dateCheck'] == None or diffDate(data['dateCheck'], date) != 1
        # print(data['phone'])
        # print(isProfile)
        # print(noCheck)
        if ( isProfile and noCheck ) :
            inActiveList.append(data['phone'])

    for phone in inActiveList :
        db.collection(type).document(phone).update({ 'isActive' : -2 })
        sendMessage('inActive', phone[1:])
