from scheduledFunctions import runSocialMediaScheduler, runPostScheduler
import schedule
import pytz
import time

# for python packages
# pip freeze > requirements.txt

schedule.every(0.1).minutes.do(runSocialMediaScheduler)
schedule.every(0.1).minutes.do(runPostScheduler)

# schedule.every().hour.at(":53").do(runSocialMediaScheduler)

# schedule.every().day.at("17:15", "Asia/Dubai").do(runSocialMediaScheduler)
# schedule.every().day.at("17:45", "Asia/Dubai").do(runSocialMediaScheduler)

while True:
    schedule.run_pending()
    time.sleep(1)
