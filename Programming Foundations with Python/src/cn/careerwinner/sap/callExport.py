'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport

year = '2017'

for x in range(1,2):
    month = str(x)
    
    pause_seconds = 2  

    save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
         
    # savePath = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports' + '\\' + inputDate + r'.DAT'
         
    reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder)
    reports.export_report()