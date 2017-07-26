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

import datetime

print(datetime.timedelta(seconds=60))

now = datetime.datetime.now()
last_month = now.month-1 if now.month > 1 else 12
last_year = now.year - 1

print(now)

print('' + str(last_month))
print(last_year)

print(time.time())

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
# 
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
