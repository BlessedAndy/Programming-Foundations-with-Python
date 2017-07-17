'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport

import sys

print(sys.path)

print('job is running')

# if __name__ == '__main__':
#     pass

#(self, year, month, pause_seconds, save_folder)

# inputDate = time.strftime("%m.%Y", time.localtime())
        
# inputDate = '05.2017'
        
# Month,Year = inputDate.split('.')

year = '2016'
month = '02'
    
pause_seconds = 2
 
save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
         
# savePath = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports' + '\\' + inputDate + r'.DAT'
         
reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder)
reports.export_report()

