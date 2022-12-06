def sendMessageText(type) :
    if type == 'matchingDating' :
        return('matchingDating')
    elif type == 'matchingMeeting' :
        return('matchingMeeting')
    elif type == 'inActive' :
        return('inActive')
    elif type == 'success' :
        return('success')
    elif type == 'useTicket' :
        return('useTicket')
    elif type == 'payTicket' :
        return('payTicket')
    elif type == 'pay' :
        return('pay')
    else :
        return('no type')