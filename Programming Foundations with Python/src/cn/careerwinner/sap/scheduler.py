'''
Created on Aug 3, 2017

@author: Andy Zhang
'''

import schedule
import time
import callExport
import util
from datetime import date

def exportReport():
    #Open it only when require a full load
#     callExport.fullRun()

    #comment this if you require a full load
    callExport.run()
        
def checkFiles():
    util.checkReportFiles()

print('PLEASE DO NOT CLOSE THIS CONSOLE!\n \nThis console is export erp reports scheduler.\n')
print('Please close remote desktop with - leave remote desktop - bat file')

#############################################################################
#    Here the todayDate should be the date you want the export tool run.    #
#                                                                           #
#                                                                           #
#############################################################################

todayDate = str(0)

while True:
    schedule.run_pending()
    print('Today: ' + todayDate)
    newDay = str(date.today().day)
    print('New Day: ' + newDay)

    #Daily job, only skip 23
    if(todayDate != newDay and newDay != '23'):
        print('begin to exporting report and check files')
#         schedule.every().day.at("01:12").do(exportReport)
        print('ENTERED THE EVERYDAY EXCEPT SPECIFIC DAY ...');
        # schedule for check Report files
#         schedule.every().day.at("03:12").do(checkFiles)
#         print('finished the export and check files.')
        todayDate = newDay
    
    #Monthly Job
    if(todayDate != newDay and newDay == '23'):
        print('begin to exporting report and check files')
        # schedule for export report
#         schedule.every().day.at("01:12").do(exportReport)
        print('ENTERED THE SPECIFIC DAY ...');
        # schedule for check Report files
#         schedule.every().day.at("03:12").do(checkFiles)
        print('finished the export and check files.')
        todayDate = newDay
    
    #sleep 5 MIN, you can change the time here to change the check rate
    time.sleep(60*5)