from apscheduler.schedulers.background import BackgroundScheduler
from .update_api import UpdateApi
from datetime import datetime


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(UpdateApi().end_today_game, 'interval', seconds=10)
    scheduler.add_job(UpdateApi().start_today_game, 'interval', seconds=10)
    scheduler.add_job(UpdateApi().alter_slip, 'interval', seconds=10)
    scheduler.add_job(UpdateApi().add_raffle_members, 'interval', seconds=10)
    scheduler.add_job(UpdateApi().end_raffle_draw, 'interval', seconds=10)
    scheduler.add_job(UpdateApi().init_game_setting, 'interval', hours=3)
    scheduler.add_job(UpdateApi().check_payments, 'interval', seconds=15)
    scheduler.add_job(UpdateApi().remove_limit, 'interval', hours=24, start_date='2020-07-15 00:00:00')
    scheduler.start()
