import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils.diffDate import diffDate


def payUpdate(type, phone, date):

    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")

    db = firestore.client()

    dataMate = db.collection(type+'Mate').document('u'+phone)
    dataUser = db.collection('user').document('u'+phone)

    dataMate.update({
    'datePay' : date
    })
    mateList = dataUser.get().to_dict()['mateList'] 

    # print(mateList)
    for i, mate in enumerate(mateList, start=0) :
        if diffDate(mate['date'], date) == 0 and mate['type'] == type:
            # temp = mate
            # temp['isPay'] = True
            # mateList[i] = temp
            mateList[i]['isPay'] = True

    dataUser.update({
    'mateList' : mateList
    })