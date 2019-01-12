from bird_api import bird_watch
import sched, time

b = bird_watch()
b.update_login_info()
print(b.email, b.guid)
b.login()
b.set_search(34.413112,-119.855395, 10, 1200)
# poll_scheduler = sched.scheduler(time.time, time.sleep)
# time_interval = 60
# poll_scheduler.setup(time_interval, b.pull_data())
b.pull_data()
