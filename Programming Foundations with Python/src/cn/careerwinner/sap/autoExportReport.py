'''
Created on 7 Jul 2017

@author: Andy Zhang
'''
import pyautogui
from subprocess import Popen
from time import sleep
import time
import os
import logging
import datetime

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

picPath = os.path.dirname(__file__)
        
class ExportReport():
    
    def __init__(self, year, month, pause_seconds, save_folder,ERPSystem):
        self.Year = year
        self.Month = month
        pyautogui.PAUSE = pause_seconds
        self.save_folder = save_folder
        self.ERPSystem = ERPSystem
        
    def confirm_this_step(self,stepSignatures):
        timer = 1
        n = len(stepSignatures)
        while(True):
            for i in range (0,n):
                stepSignature = stepSignatures[i]
                print('Waiting for Step ' + stepSignature + ' complete ...')
                logger.info('Waiting for Step ' + stepSignature + ' complete ...')
    
                if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\' + stepSignature + '.png') is not None):
                    print('Step ' + stepSignature + ' confirmed.')
                    logger.info('Step ' + stepSignature + ' confirmed.')
                    return True
    
            if(timer >= 60):
                print('Step ' + stepSignature + ' time out!')
                logger.error('Step ' + stepSignature + ' time out!')
#                 util.sendEmail()
                raise 'Step ' + stepSignature + ' time out!'
#                 return False
            print(timer)
            timer = timer + 1
        
    def export_report(self):
        pyautogui.FAILSAFE = True
        
        Year, Month = [self.Year, self.Month]
        
        inputDate =  str(Year) + Month
        
        savePath = self.save_folder + '\\' + inputDate + r'.dat'
        
        print('save file: '+savePath)
        

        logger.info('start exporting report of year month: ' + inputDate)
        logger.info('save Path: ' + savePath)
        
        SAPGUI = Popen(['start','SAPLogon'],shell=True)
        logger.info('start SAPGUI')
        
        sleep(3)
        
        if(self.ERPSystem == 'PED'):
            pyautogui.hotkey('ctrl', 'f')
            sleep(1)
            for i in range(1,4):
                pyautogui.hotkey('backspace')
            pyautogui.typewrite('PED')
            sleep(2)
            pyautogui.press('enter')
            logger.info('enter PED system')

        if(self.ERPSystem == 'DED'):
            pyautogui.hotkey('ctrl', 'f')
            sleep(1)
            for i in range(1,4):
                pyautogui.hotkey('backspace')
            pyautogui.typewrite('DED')
            sleep(2)
            pyautogui.press('enter')
        
        sleep(3)
        pyautogui.hotkey('win', 'up')  # Win + up
        sleep(2)
        
        #For PRD
        if(self.ERPSystem == 'PED'):
            pyautogui.typewrite('peaint01')
            pyautogui.hotkey('tab')
            pyautogui.typewrite('cbsint01')
            pyautogui.press('enter')
        
            logger.info('logon the PED ERP system') 

        if(self.ERPSystem == 'DED'):
            pyautogui.typewrite('PTNPUNNEEAM')
            pyautogui.hotkey('tab')
            pyautogui.typewrite('QWERTY')
            pyautogui.press('enter')
        
            logger.info('logon the DED ERP system') 
                       
        #TODO:
        #Multi user logon
        sleep(2)
        if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\multiUsers.png') is not None):
            pyautogui.hotkey('tab')
            pyautogui.hotkey('up')
            pyautogui.press('enter')
            logger.info('multi user loged on') 
            
        sleep(2)
        pyautogui.press('enter')
        
        #TODO:
        #confirm logon complete
        signatures = ['confirm_logon','confirm_logon_1','confirm_logon_2','confirm_logon_3','confirm_logon_4']
        self.confirm_this_step(signatures)
        
        #input t-code
        sleep(7)
        #in case tcode input box not visible
        pyautogui.press('enter')
        pyautogui.press('left')
        pyautogui.typewrite('zglr003\n')
        # pyautogui.press('enter')
        logger.info('run the zglr003 report') 
        
        sleep(3)
        logger.info('type in parameters for export reports') 
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite('สตง')
        
        #input year
        pyautogui.hotkey('tab')
        pyautogui.typewrite(Year)
        
        #input From Month
        pyautogui.hotkey('tab')
        pyautogui.typewrite(Month)
        
        #input To Month
        pyautogui.hotkey('tab')
        #if 
        if(Month == '12'):
            Month = '16'
        pyautogui.typewrite(Month)
        #Run the report
#         sleep(3)
        pyautogui.hotkey('alt','p')
        pyautogui.press('a')
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        pyautogui.press('enter')
        
        #Wait the report loaded
#         sleep(300)
        start_running_report_time = time.time()
        while(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady1.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady2.png') is None and pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/reportReady3.png') is None):
            
            logger.info('waiting for report loading ...')
            print('waiting for report loading ...')
            sleep(3)
        
        #TODO:
        #Confirm report loaded success and completed
        print('Cost ' + str(time.time()-start_running_report_time) + ' seconds to run the report.')
        logger.info('Cost ' + str(datetime.timedelta(seconds=(time.time()-start_running_report_time))) + 'to run the report.')
        pyautogui.hotkey('alt','r')
        pyautogui.press('r')
        
        #Click Save to file
        sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')
        
        sleep(2)
        pyautogui.typewrite(savePath)
        pyautogui.press('enter')
        
        #
        pyautogui.hotkey('alt','a')
        
        sleep(2)
        #Allow    
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')
        
        sleep(2)
        
        #Confirm
        pyautogui.hotkey('alt','a')
        pyautogui.moveTo(800,10)
#         pyautogui.press('enter')

        logger.info('save report of ' + inputDate) 

        #If already exist, replace it
        sleep(3)
        if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\alreadyexist.png') is not None):
            logger.info(inputDate + '.dat already exist.')
            pyautogui.press('enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')

        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\alreadyexist2.png') is not None):
            logger.info(inputDate + '.dat already exist2.')
            pyautogui.press('enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            
        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\alreadyexist3.png') is not None):
            logger.info(inputDate + '.dat already exist3.')
            pyautogui.press('enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            
        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\alreadyexist4.png') is not None):
            logger.info(inputDate + '.dat already exist4.')
            pyautogui.press('enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            
        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\alreadyexist5.png') is not None):
            print('entered the report exist')
            logger.info(inputDate + '.dat already exist5.')
            pyautogui.press('enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            
        else:
            logger.info(inputDate + '.dat is the first time to export.')
        
        #Confirm
        sleep(3)
        pyautogui.hotkey('alt','a')
        
        sleep(3)
        pyautogui.hotkey('alt','f4')
        sleep(2)
        pyautogui.press('tab')
        pyautogui.press('enter')
                
        #close SAP GUI
        sleep(2)
        pyautogui.hotkey('alt','f4')
        logger.info('close SAPGUI') 
        print('SAP GUI closed')


