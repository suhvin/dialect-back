from utils.getDate import getDate
from utils.nextDate import nextDate
from .inActive import inActive
from .useTicket import useTicket

def do_day2():
    date = nextDate()
    # date= getDate()
    inActive('dating', date)
    inActive('meeting', date)
    useTicket('dating', date)
    useTicket('meeting', date)