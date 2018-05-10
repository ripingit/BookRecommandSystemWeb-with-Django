from apscheduler.schedulers.background import BackgroundScheduler

class Scheduled:
    def __init__(self):
        self.sched = BackgroundScheduler()