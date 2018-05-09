import time
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
sched = AsyncIOScheduler()

@sched.scheduled_job('interval',minutes=1)
def jobs():
    print(time.strftime('%H:%M:%S',time.localtime(time.time())))

sched.start()

count = 0
while True:
    time.sleep(10)
    count += 10
    print('已经过去了',count,'秒')