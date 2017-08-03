'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport
import time
import pyautogui
from subprocess import Popen
import os
import sys

from dateutil.relativedelta import relativedelta
import pyautogui
from datetime import date
import time


import logging

# SAPGUI = Popen(['start','SAPLogon'],shell=True)
# 
# time.sleep(60)
# 
# print(str(SAPGUI.pid()))

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

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# 
# # create a file handler
# handler = logging.FileHandler('exportReport.log')
# handler.setLevel(logging.INFO)
# 
# # create a logging format
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# 
# # add the handlers to the logger
# logger.addHandler(handler)
# 
# logger.info('Hello baby')

# for i in range(1,9):
#     eight_months_before = date.today() + relativedelta(months = -i)
#     year = str(eight_months_before.year)
#     month = str(eight_months_before.month)
#     #month format: e.g: '01'
#     if(len(month)==1):
#         month = '0' + month
#     pause_seconds = 2 
#     print('Year Month : '+str(year)+str(month))
    


# print(datetime.timedelta(seconds=60))
# 
# now = datetime.datetime.now()
# last_month = now.month-1 if now.month > 1 else 12
# last_year = now.year - 1
# 
# print(now)
# 
# print('' + str(last_month))
# print(last_year)
# 
# print(time.time())



# print(pyautogui.prompt(text='text', title='title' , default='username'))

# print(pyautogui.password(text='text', title='title', default='password', mask='*'))

# today = datetime.date.today()
# previous_month = datetime(today.year, today.month + 1, today.day)
# 
# three_mon_rel = relativedelta(months=3)
# print(today + three_mon_rel)
# 
# print(today)
# print(previous_month)
# 
# year = '2015'
# print('enter very beginning')
# 
# SAPGUI = Popen(['start','SAPLogon'],shell=True)
# 
# time.sleep(7)
# 
# win = pyautogui.getWindow('SAP Logon')
# 
# print(win.get_position())
# 
# 
# print(os.path.abspath(os.curdir))
# print(sys.argv[0])
# print(os.path.dirname(__file__))



# for x in range(1,16):
#     
#     month = str(x)
#     
#     #month format: e.g: '01'
#     if(len(month)==1):
#         month = '0' + month
#     pause_seconds = 12  
# 
#     save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
#     #Server Folder
#     #save_folder = r'D:\FI\data\erp'
#     print('save folder: ' + save_folder)
# 
#     
#     reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder)
#     reports.export_report()
#     
