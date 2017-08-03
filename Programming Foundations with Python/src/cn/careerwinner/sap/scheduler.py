'''
Created on Aug 3, 2017

@author: I310003
'''

import schedule
import time
import callExport

def job():
    print("I'm working...")
    print(time.clock())
    callExport()

schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)