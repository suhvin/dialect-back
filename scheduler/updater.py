# from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
# from .jobs import do_something1, do_something2
# from day1.day1 import do_day1

def start():
    
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # # 이틀 차이나게 start_date 수정
    # scheduler.add_job(do_something1, 'cron', start_date=datetime(2022, 11, 25), day="*/2", hour="15", minute='5', id='job1')
    # scheduler.add_job(do_something2, 'cron', start_date=datetime(2022, 11, 26), day="*/2", hour="15", minute='5', id='job2')

    scheduler.start()