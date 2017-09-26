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
import os
import util

import smtplib
from time import sleep

util.checkReportFiles()

# sleep(1)
# for i in range(1,4):
#     pyautogui.hotkey('backspace')
#1
# picPath = os.path.dirname(__file__)
# 
# def confirm_this_step(stepSignatures):
#     timer = 1
#     n = len(stepSignatures)
#     while(True):
#         for i in range (0,n):
#             stepSignature = stepSignatures[i]
#             print('Waiting for Step ' + stepSignature + ' complete ...')
# 
#             if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/' + stepSignature + '.png') is not None):
#                 print('Step ' + stepSignature + ' confirmed.')
# #                 logger.info('Step ' + stepSignature + ' confirmed.')
#                 return True
# #       logger.info('Waiting for Step ' + stepSignature + ' complete ...')
# 
#         if(timer >= 20):
#             print('Step ' + stepSignature + ' time out!')
# #            logger.info('Step ' + stepSignature + ' time out!')
# #                     util.sendEmail()
#             return False
#         print(timer)
#         timer = timer + 1   
#     
# stepSignatures = ['confirm_logon','confirm_logon_1','confirm_logon_2','confirm_logon_3','confirm_logon_4']
# print(confirm_this_step(stepSignatures))
# callList = ['a','b','c']

# def testCallList(it):
#     i = len(it)
#     return i
# 
# callList = ['a','b','c']
# it = 'string'
# print(testCallList(callList))

# sender = 'SAP_DataServices@portalnet.co.th'
# receivers = ['andy.zhang05@sap.com']
# 
# message = """From: From Data Services Python Export Report Tool
# To: To Person <andy.zhang05@sap.com>
# Subject: Python auto export tool didn't works well
# 
# Dear Colleagues,
# 
# Please check the reports files for Data Services jobs, it seems that the file has not ready.
#     Notes: 1. If you want the export tool run automatically, please use logoff.bat file to logoff remote desktop.
#            2. If you want to run the export tool manually, please don't minimize the remote desktop.
#            
# FROM REPORT EXPORT TOOL 
# """
# 
# # try:
# smtpObj = smtplib.SMTP('172.30.46.146')
# smtpObj.sendmail(sender, receivers, message)         
# print("Successfully sent email")
# except SMTPException:
#    print("Error: unable to send email")

# picPath = os.path.dirname(__file__)
# print(picPath)
# while(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/confirm_logon.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady1.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady2.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady3.png') is None):
#     print('waiting for report loading ...')
#      
# if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/confirm_logon.png') is not None):
#     print('logon')
# 
# if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady1.png') is not None):
#     print('reportReady1')# 
# if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady2.png') is not None):
#     print('reportReady2')
# 
# if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady3.png') is not None):
#     print('reportReady3')
    
# 
# def job():
#     print("I'm working...")
#     print(time.clock())
#     callExport()
# 
# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("15:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# 
# while True:
#     schedule.run_pending()
#     time.sleep(1)

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
