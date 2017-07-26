'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport
import time
import datetime

now = datetime.datetime.now()
last_month = now.month-1 if now.month > 1 else 12
last_year = now.year - 1

print(now)

print('Last Month: ' + str(last_month))
print('Last Year: ' + str(last_year))

# year = '2015'
# year = now.year

#Wait for logoff server
#time.sleep(60)
start_time = time.time();

for y in range(2015, now.year):
    year = str(y)
    for x in range(1,last_month if year == now.year else 13):
        month = str(x)
     
        #month format: e.g: '01'
        if(len(month)==1):
            month = '0' + month
        pause_seconds = 2 
     
        save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
        #Server Folder
    #     save_folder = r'D:\FI\data\erp'
        print('save folder: ' + save_folder)
         
        reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder)
        reports.export_report()
        print('Running time for year :' + year + datetime.timedelta(seconds=(time.time()-start_time)))

print('Total running time:' + datetime.timedelta(seconds=(time.time()-start_time)))
