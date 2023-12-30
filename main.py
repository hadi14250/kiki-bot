from scheduledFunctions import runSocialMediaScheduler, runPostScheduler
import schedule
import time
import threading
from sendEmail import sendExcelSheetToMods
from logger import startLogger
import os

to_email = os.environ.get("EMAILING_LIST")
cc_recipients = os.environ.get("EMAILING_LIST_CC")

logger = startLogger()

def excepthook(args):
    logger.error("An error occurred!! exc_value: ".format(args.exc_value), exc_info=True)
    logger.error("exc_traceback: ".format(args.exc_traceback), exc_info=True)
    logger.error("exc_type: ".format(args.exc_type), exc_info=True)
    logger.error("thread: ".format(args.thread), exc_info=True)

threading.excepthook = excepthook

def run_threadedSocialMedia(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    return (job_thread)

def run_threadedPosts(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    return (job_thread)

def run_threadedSendEmails(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    job_thread.join()

schedule.every().day.at("16:00", "Asia/Dubai").do(run_threadedSendEmails, lambda: sendExcelSheetToMods(to_email, cc_recipients))

tSocialMedia = run_threadedSocialMedia(runSocialMediaScheduler)
tPosts = run_threadedPosts(runPostScheduler)

while True:
    schedule.run_pending()
    time.sleep(600)
    if not (tSocialMedia.is_alive()):
        tSocialMedia = run_threadedSocialMedia(runSocialMediaScheduler)
    if not (tPosts.is_alive()):
        tPosts = run_threadedPosts(runPostScheduler)
