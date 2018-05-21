from apscheduler.schedulers.background import BackgroundScheduler

class Scheduled:
    borrowSched = BackgroundScheduler()
    def start(self):
        self.borrowSched.start()
# 单例
scheduled = Scheduled()