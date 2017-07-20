'''
Created on 7 Jul 2017

@author: andy
'''
import pyautogui
from subprocess import Popen
from time import sleep
import time

import sys

print(sys.path)

# pyautogui.PAUSE = 2.5

class ExportReport():
    
#     valid_ratings = ["G","PG","PG-13","R"]
    
    def __init__(self, year, month, pause_seconds, save_folder):
        self.Year = year
        self.Month = month
        pyautogui.PAUSE = pause_seconds
        self.save_folder = save_folder
        
    def export_report(self):
#         webbrowser.open(self.trailer_youtube_url)
#         webbrowser.open("http://music.163.com/#/outchain/2/409872465/")
        
        print(pyautogui.size())
        
#         PAUSE = 2.5
        
#         pyautogui.PAUSE = 7
#         self.PAUSE
        pyautogui.FAILSAFE = True
        
        # inputDate = time.strftime("%m.%Y", time.localtime())
        
        # inputDate = '05.2017'
        
        # Month,Year = inputDate.split('.')
        
        Year, Month = [self.Year, self.Month]
        
        inputDate =  Year + Month
        
        # savePath = r'C:\Users\I310003\Documents\SAP\Projects\PEA\Automatical\reports' + '\\' + inputDate + r'.DAT'
        savePath = self.save_folder + '\\' + inputDate + r'.DAT'
        
        print(savePath)
        
        SAPGUI = Popen(['start','SAPLogon'],shell=True)
        sleep(7)
        
        #STEP 1: Open SAP GUI
        pyautogui.hotkey('win', 'up')  # Win + up
        
        #STEP 2: Double click ERP icon
        if(pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP_Server.png') is not None):
            x, y = pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP_Server.png')
            pyautogui.doubleClick(x, y)
        elif(pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP.png') is not None):
            x, y = pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP.png')
            pyautogui.doubleClick(x, y)
        elif(pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP_select.png') is not None):
            x, y = pyautogui.locateCenterOnScreen('autoExportReport/DoubleClickERP_select.png')
            pyautogui.doubleClick(x, y)
        else:
            pyautogui.alert(text='There is no DED system found', title='System no found', button='OK')
            
        
        #Logon system, input username and password
        #Client: 210/220
        #U: PTNPUNNEEAM
        #P: QWERTY
        
        #Find input box
        x, y = pyautogui.locateCenterOnScreen('autoExportReport/user.png')
        pyautogui.click(x, y+50)
        
        pyautogui.typewrite('PTNPUNNEEAM\n')
        pyautogui.hotkey('tab')
        pyautogui.typewrite('QWERTY')
        pyautogui.press('enter')
        
        #TODO:
        #Multi user logon
        if(pyautogui.locateCenterOnScreen('autoExportReport/multiUsers.png') is not None):
#             x, y = pyautogui.locateCenterOnScreen('autoExportReport/multiUsers.png')
#             pyautogui.click(x-50, y-25)
#             pyautogui.press('enter')  
            pyautogui.hotkey('tab')
            pyautogui.hotkey('up')
            pyautogui.press('enter')
        
        
        #input t-code
        pyautogui.typewrite('zglr003\n')
        # pyautogui.press('enter')
        
        #input FIS
        pyautogui.moveTo(800, 10)
        sleep(3)
        x, y = pyautogui.locateCenterOnScreen('autoExportReport/FIS.png')
        pyautogui.click(x, y)
        pyautogui.typewrite('สตง')
        
        #input year
        pyautogui.hotkey('tab')
        pyautogui.typewrite(Year)
        
        #input From Month
        pyautogui.hotkey('tab')
        pyautogui.typewrite(Month)
        
        #input To Month
        pyautogui.hotkey('tab')
        pyautogui.typewrite(Month)
        # pyautogui.press('enter')
        
        #Run the report
        sleep(3)
        pyautogui.hotkey('alt','p')
        pyautogui.press('a')
        # x, y = pyautogui.locateOnScreen('autoExportReporth/run.png', region=(0,0, 300, 400))
        # x, y = pyautogui.locateCenterOnScreen('autoExportReporth/run.png')
        # pyautogui.click(x, y)
        
        # x, y = pyautogui.locateCenterOnScreen('autoExportReporth/newSession.png')
        # pyautogui.click(x, y)
        pyautogui.hotkey('up')
        pyautogui.hotkey('up')
        pyautogui.press('enter')
        
        #Click export report
        sleep(1)
        # x, y = pyautogui.locateCenterOnScreen('autoExportReporth/exportButton.png')
        # pyautogui.click(x, y)
        pyautogui.hotkey('alt','r')
        pyautogui.press('r')
        
        print('after export report')
        
        #Click Save to file
        sleep(1)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.press('enter')
        # x, y = pyautogui.locateCenterOnScreen('autoExportReporth/saveToFile.png')
        # pyautogui.click(x, y)
        
        print('after save report')
        
        sleep(3)
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
#         pyautogui.press('enter')

        #If already exist, replace it
        if(pyautogui.locateCenterOnScreen('autoExportReport/alreadyexist.png') is not None):
            print('entered the report exist')
            pyautogui.press('enter')
            print('这里刚刚敲入enter')
            #Allow    
            sleep(3)
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
        
        #Confirm
        print('这里出来了判断')
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
        pyautogui.press('tab')
        pyautogui.press('enter')
        print('report界面关闭了！')
#         x, y = pyautogui.locateCenterOnScreen('autoExportReport/close.png')
#         pyautogui.click(x,y)
        
#         pyautogui.hotkey('tab')
#         pyautogui.press('enter')
#         x, y = pyautogui.locateCenterOnScreen('autoExportReport/closeYes.png')
#         pyautogui.click(x,y)
                
        #close SAP GUI
        pyautogui.hotkey('alt','f4')
        print('SAP GUI关闭了')
#         pyautogui.hotkey('tab')
#         pyautogui.press('enter')
#         x, y = pyautogui.locateCenterOnScreen('autoExportReport/close.png')
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