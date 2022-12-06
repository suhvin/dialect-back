import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils.payUpdate import payUpdate
from utils.sendMessage import sendMessage
from utils.diffDate import diffDate


def useTicket(type, date):

    cred = credentials.Certificate(os.getcwd() + "/scheduler/yeonpick0727-key.json")

    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Already Connected something1")

    db = firestore.client()
    mateDocs = db.collection(type+'Mate').stream()

    useTicketList = []
    for doc in mateDocs:
        data = doc.to_dict()
        # print(data['phone'])
        # print('dateProfile'+str(data['dateProfile'] != None and diffDate(data['dateProfile'], date) == 1))
        # print('dateCheck'+str(data['dateCheck'] != None and diffDate(data['dateCheck'], date) == 1))
        # print('dateChosen'+str(data['dateChosen'] != None and diffDate(data['dateChosen'], date) == 1))
        # print('isCheck'+str(data['isCheck'] != None and data['isCheck']))
        # print('isChosen'+str(data['isChosen'] != None and data['isChosen']))
        isProfile = data['dateProfile'] != None and diffDate(data['dateProfile'], date) == 1
        isCheck = data['dateCheck'] != None and diffDate(data['dateCheck'], date) == 1 and data['isCheck'] != None and data['isCheck']
        isChosen = data['dateChosen'] != None and diffDate(data['dateChosen'], date) == 1 and data['isChosen'] != None and data['isChosen']
        if ( isProfile and isCheck and isChosen ) :
            phone = data['phone']
            matePhone = data['matePhone']
            storeDoc = db.collection('store').document(phone)
            storeData = storeDoc.get().to_dict()
            plus = storeData['ticketPlus']
            minus = storeData['ticketMinus']
            if  plus - minus > 0 :
                useTicketList.append([phone, matePhone])
                storeDoc.update({ 'ticketMinus' : minus + 1 })

    for set in useTicketList :
        payUpdate(type, set[0][1:], date)
        payUpdate(type, set[1][1:], date)
        sendMessage('useTicket', set[0][1:])
