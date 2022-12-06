from utils.sendMessage import sendMessage
from utils.payUpdate import payUpdate


def pay(type, oid, date):

    phoneBoy = oid[-23:-12]
    phoneGirl = oid[-11:]
    print(phoneBoy)
    print(phoneGirl)

    payUpdate(type, phoneBoy, date)
    payUpdate(type, phoneGirl, date)
    sendMessage('pay', phoneBoy)