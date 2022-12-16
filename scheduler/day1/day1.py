from utils.getDate import getDate
from utils.nextDate import nextDate
from .matchingDating import matchingDating
from .matchingMeeting import matchingMeeting
from .recordDating import recordDating
from .recordMeeting import recordMeeting
import time

def do_day1():
    # date = nextDate()
    date = getDate()
    matchingDating(date)
    time.sleep(60)
    matchingMeeting(date)
    recordDating(date)
    recordMeeting(date)
    
    
