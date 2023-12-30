from datetime import datetime, timedelta

def getYesterdaysDate():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    return (yesterday.strftime("%Y-%m-%d"))

def getTodaysDate():
    today = datetime.now()
    return today.strftime("%Y-%m-%d")

