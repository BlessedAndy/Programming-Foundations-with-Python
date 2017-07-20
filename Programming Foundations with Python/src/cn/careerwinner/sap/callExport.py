'''
Created on Jul 14, 2017

@author: I310003
'''
import autoExportReport

year = '2017'

for x in range(1,16):
    
    month = str(x)
    
    #month format: e.g: '01'
    if(len(month)==1):
        month = '0' + month
    
    pause_seconds = 6  

    save_folder = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports'
         
    reports = autoExportReport.ExportReport(year, month, pause_seconds, save_folder)
    reports.export_report()