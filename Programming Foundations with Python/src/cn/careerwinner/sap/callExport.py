'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport
import time
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

#Wait for logoff server
#time.sleep(60)

#System will be used
ERPSystem = 'PED'
#ERPSystem = 'DED'

#save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
#Server Folder
save_folder = r'D:\FI\data\erp'

def run():  
    start_time = time.time();

    for i in range(1,9):
        eight_months_before = date.today() + relativedelta(months = -i)
        year = str(eight_months_before.year)
        
        month = str(eight_months_before.month)
        #month format: e.g: '01'
        if(len(month)==1):
            month = '0' + month
        pause_seconds = 5 
        print('Exporting report of Year Month : '+str(year)+str(month))
         
        print('save folder: ' + save_folder)
        
        this_start_time = time.time()
        reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder,ERPSystem)
        reports.export_report()
        print('Running time for year month ' + str(year)+str(month) + '   ' + str(datetime.timedelta(seconds=(time.time()-this_start_time))))
    
    print('Total running time:' + str(datetime.timedelta(seconds=(time.time()-start_time))))
    
def fullRun():  
    start_time = time.time();
    
    for i in range(2015,date.today().year):
        year = str(i)
        for m in range(1,12):
       
            month = str(m)
            #month format: e.g: '01'
            if(len(month)==1):
                month = '0' + month
            pause_seconds = 2 
            print('Exporting report of Year Month : '+str(year)+str(month))
             
            print('save folder: ' + save_folder)
            
            this_start_time = time.time()
            reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder,ERPSystem)
            reports.export_report() 
            print('Running time for year month ' + year + month + ' : ' + str(datetime.timedelta(seconds=(time.time()-this_start_time))))
        
        print('Total running time:' + str(datetime.timedelta(seconds=(time.time()-start_time))))

if __name__ == '__main__':
    # execute only if run as a script
    run()
