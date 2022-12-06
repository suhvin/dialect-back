from utils.nextDate import nextDate
from .matchingDating import matchingDating
from .matchingMeeting import matchingMeeting
from .recordDating import recordDating
from .recordMeeting import recordMeeting

def do_day1():
    date = nextDate()
    matchingDating(date)
    matchingMeeting(date)
    recordDating(date)
    recordMeeting(date)
    
