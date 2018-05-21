from Scheduler.scheduler import scheduled
import time
def fun(user,password):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('user:',user,'password:',password)
if __name__ == "__main__":
    scheduled.borrowSched.add_job(fun,'interval',seconds=1,args=('sjm','16240011'))
    scheduled.borrowSched.start()
    time.sleep(3)
    scheduled.borrowSched.pause()
    time.sleep(3)
    scheduled.borrowSched.resume()
    time.sleep(3)
    scheduled.borrowSched.resume()
    while True:
        pass
