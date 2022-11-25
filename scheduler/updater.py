
RawBlame


from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import do_something1, do_something2


def start():
    
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # 이틀 차이나게 start_date 수정
    scheduler.add_job(do_something1, 'cron', start_date=datetime(2022, 11, 25), day="*/2", hour="16", minute='50', id='job1')
    scheduler.add_job(do_something2, 'cron', start_date=datetime(2022, 11, 26), day="*/2", hour="16", minute='50', id='job2')

    scheduler.start()