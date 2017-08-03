'''
Created on 7 Jul 2017

@author: andy
'''
import pyautogui
from subprocess import Popen
from time import sleep
import os
import logging

class ExportReport():
    
    def __init__(self, year, month, pause_seconds, save_folder):
        self.Year = year
        self.Month = month
        pyautogui.PAUSE = pause_seconds
        self.save_folder = save_folder
        
    def export_report(self):
        pyautogui.FAILSAFE = True
        
        picPath = os.path.dirname(__file__)
        
        # inputDate = time.strftime("%m.%Y", time.localtime())
        # inputDate = '05.2017'
        # Month,Year = inputDate.split('.')
        
        Year, Month = [self.Year, self.Month]
        
        inputDate =  str(Year) + Month
        
        # savePath = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports' + '\\' + inputDate + r'.DAT'
        savePath = self.save_folder + '\\' + inputDate + r'.dat'
        
        print('save file: '+savePath)
        
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # create a file handler
        handler = logging.FileHandler('exportReport.log')
        handler.setLevel(logging.INFO)
        
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # add the handlers to the logger
        logger.addHandler(handler)
        logger.info('start exporting report of year month: ' + inputDate)
        logger.info('save Path: ' + savePath)
        
        SAPGUI = Popen(['start','SAPLogon'],shell=True)
        logger.info('start SAPGUI')
        sleep(7)
        
        #STEP 1: Open SAP GUI
        pyautogui.hotkey('win', 'up')  # Win + up
        
        #STEP 2: Double click ERP icon
        sleep(3)
        if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP_Server.png') is not None):
            x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP_Server.png')
            pyautogui.doubleClick(x, y)
            logger.info('DoubleClickERP_Server')
        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP.png') is not None):
            x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP.png')
            pyautogui.doubleClick(x, y)
            logger.info('DoubleClickERP')
        elif(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP_select.png') is not None):
            x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\DoubleClickERP_select.png')
            pyautogui.doubleClick(x, y)
            logger.info('DoubleClickERP_select')
        else:
            pyautogui.alert(text='There is no DED system found', title='System no found', button='OK')
            logger.error('There is no system found')
            raise RuntimeError('There is no system found')
            
        #Logon system, input username and password
        #Client: 210/220
        #U: PTNPUNNEEAM
        #P: QWERTY

        #Find input box
        sleep(3)
        pyautogui.hotkey('win', 'up')  # Win + up
        sleep(2)
        x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\user.png')
        pyautogui.click(x, y+50)
        
#         pyautogui.typewrite('PTNPUNNEEAM\n')
        #Server version
        pyautogui.typewrite('PTNPUNNEEAM')
        pyautogui.hotkey('tab')
        pyautogui.typewrite('QWERTY')
        pyautogui.press('enter')
        
        logger.info('logon the ERP system') 
                       
        #TODO:
        #Multi user logon
        sleep(2)
        if(pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\multiUsers.png') is not None):
#             x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/multiUsers.png')
#             pyautogui.click(x-50, y-25)
#             pyautogui.press('enter')  
            pyautogui.hotkey('tab')
            pyautogui.hotkey('up')
            pyautogui.press('enter')
            logger.info('multi user loged on') 
        
        
        #input t-code
        sleep(3)
        #in case tcode input box not visible
        pyautogui.press('enter')
        pyautogui.press('left')
        pyautogui.typewrite('zglr003\n')
        # pyautogui.press('enter')
        logger.info('run the zglr003 report') 
        
        #input FIS
        pyautogui.moveTo(800, 10)
        sleep(3)
        x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport\\FIS.png')
        pyautogui.click(x, y)
        logger.info('type in parameters for export reports') 
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
        # pyautogui.press('enter')
        
        #Run the report
#         sleep(3)
        pyautogui.hotkey('alt','p')
        pyautogui.press('a')
        # x, y = pyautogui.locateOnScreen(picPath + '\\autoExportReporth/run.png', region=(0,0, 300, 400))
        # x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReporth/run.png')
        # pyautogui.click(x, y)
        
        # x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReporth/newSession.png')
        # pyautogui.click(x, y)
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        pyautogui.press('enter')
        
        #Click export report
        sleep(12)
        # x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReporth/exportButton.png')
        # pyautogui.click(x, y)
        pyautogui.hotkey('alt','r')
        pyautogui.press('r')
        
        #Click Save to file
        sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')
        # x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReporth/saveToFile.png')
        # pyautogui.click(x, y)
        
        sleep(2)
        pyautogui.typewrite(savePath)
        pyautogui.press('enter')
        
        #
        pyautogui.hotkey('alt','a')
        
        #Allow    
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')
        
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
        
#         pyautogui.prompt(text='export report complete', title='info' , default='Good Job!')
        
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.press('enter')
        
#         sleep(3)
        
#         pyautogui.hotkey('alt','a')
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.hotkey('tab')
        # pyautogui.press('enter')
        
#         sleep(3)
        
        # pyautogui.hotkey('alt','a')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
#         pyautogui.hotkey('tab')
#         pyautogui.press('enter')
#         
#         sleep(3)
#         
#         pyautogui.hotkey('alt','a')
        
        #close report

        sleep(3)
        pyautogui.hotkey('alt','f4')
        sleep(1)
        pyautogui.press('tab')
        pyautogui.press('enter')
#         x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/close.png')
#         pyautogui.click(x,y)
        
#         pyautogui.hotkey('tab')
#         pyautogui.press('enter')
#         x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/closeYes.png')
#         pyautogui.click(x,y)
                
        #close SAP GUI
        sleep(1)
        pyautogui.hotkey('alt','f4')
        logger.info('close SAPGUI') 
        print('SAP GUI closed')
#         pyautogui.hotkey('tab')
#         pyautogui.press('enter')
#         x, y = pyautogui.locateCenterOnScreen(picPath + '\\autoExportReport/close.png')
#         pyautogui.click(x,y)

# pyautogui.press('enter')  # press the Enter key
# pyautogui.press('f1')     # press the F1 key
# pyautogui.press('left')   # press the left arrow key

#pyautogui.moveTo(x, y, duration=num_seconds)

#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter

#pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

#pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
#pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

#pyautogui.alert('This displays some text with an OK button.')
#pyautogui.confirm('This displays text and has an OK and Cancel button.')

#pyautogui.prompt('This lets the user type in a string and press OK.')

#pyautogui.locateOnScreen('looksLikeThis.png')

#pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds


#pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
#pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
#pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end


#alert(text='', title='', button='OK')

#confirm(text='', title='', buttons=['OK', 'Cancel'])

#prompt(text='', title='' , default='')

#button7location = pyautogui.locateOnScreen('calc7key.png')
#button7x, button7y = pyautogui.center(button7location)
#pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found


#x, y = pyautogui.locateCenterOnScreen('calc7key.png')
#pyautogui.click(x, y)


#pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
#pyautogui.getWindow(str_title_or_int_id) # returns a â€œWinâ€� object
#win.move(x, y)
#win.resize(width, height)
#win.maximize()
#win.minimize()
#win.restore()
#win.close()
#win.position() # returns (x, y) of top-left corner
#win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
#win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=â€™leftâ€™) # click relative to the x, y of top-left corner of the window
#Additions to screenshot functionality so that it can capture specific windows instead of full screen.
