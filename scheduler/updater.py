from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import do_something


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(do_something, 'interval', days=2)
    scheduler.add_job(do_something, 'interval', days=2)
    scheduler.start()