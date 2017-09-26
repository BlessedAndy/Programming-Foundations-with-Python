'''
Created on Aug 10, 2017

@author: I310003
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dateutil.relativedelta import relativedelta
from datetime import date
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('log_exportReport.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

#Server Folder
save_folder = r'D:\FI\data\erp\\'

lastMonth = date.today() + relativedelta(months = -1)
year,month = str(lastMonth.year), str(lastMonth.month)

if(len(month)==1):
    month = '0' + month

filePath = save_folder + year + month + '.DAT'

def sendEmail():
    sender = 'SAP_DataServices@portalnet.co.th'

    receivers = 'apirak.k@portalnet.co.th; amarin.n@portalnet.co.th'
    receiver2 ='amarin.n@portalnet.co.th'
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Report files are not ready! Please Check"
    msg['From'] = sender
    msg['To'] = receivers
    
    html = """\
    <html>
     <head>
      <meta charset="UTF-8">
      <title>Report files are not ready! Please Check</title>
     </head>
      <body>

                Dear Colleagues,<br><br>
    
                Please check the reports files for Data Services jobs, it seems that the file """ + filePath  +""" not ready yet.<br><br>
                Notes: <br>
                    1. If you want the export tool run automatically, please use logoff.bat file to logoff remote desktop.<br>
                    2. If you want to run the export tool manually, please don't minimize the remote desktop.<br><br>
               
                FROM REPORT EXPORT TOOL <br>
           Check Data Services jobs here: <a href="http://pspbobi20:8080/DataServices">Mangement Console</a> .
        </p>
      </body>
    </html>
    """
    
    part = MIMEText(html, 'html')
    
    msg.attach(part)
    
    s = smtplib.SMTP('172.30.46.146')
    try:
        s.sendmail(sender, receivers, msg.as_string())
        s.sendmail(sender, receiver2, msg.as_string())
        s.quit() 
    except OSError:
        print('Cannot send email!')
        logger.error('Cannot send email!')
    else:
        print('Successfully sent email')
        logger.info('Successfully sent email')
    
def checkReportFiles():

    if(os.path.isfile(filePath)):
        print('LastMonth report file ' + filePath + ' exist')
        logger.info('LastMonth report file ' + filePath + ' exist')
    else:
        print('LastMonth report file ' + filePath + ' not exist')
        logger.error('LastMonth report file ' + filePath + ' not exist')
        sendEmail()
        
