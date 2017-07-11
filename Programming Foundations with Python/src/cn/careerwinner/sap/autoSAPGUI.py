'''
Created on 7 Jul 2017

@author: andy
'''
import pyautogui
print(pyautogui.size())

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True


>>> pyautogui.press('enter')  # press the Enter key
>>> pyautogui.press('f1')     # press the F1 key
>>> pyautogui.press('left')   # press the left arrow key


pyautogui.moveTo(x, y, duration=num_seconds)

pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter

pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)

pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
>>> pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

 pyautogui.alert('This displays some text with an OK button.')
>>> pyautogui.confirm('This displays text and has an OK and Cancel button.')
'OK'
>>> pyautogui.prompt('This lets the user type in a string and press OK.')
'This is what I typed in.'



pyautogui.locateOnScreen('looksLikeThis.png')

pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds


pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end


alert(text='', title='', button='OK')

confirm(text='', title='', buttons=['OK', 'Cancel'])

prompt(text='', title='' , default='')


>>> import pyautogui
>>> button7location = pyautogui.locateOnScreen('calc7key.png')
>>> button7location
(1416, 562, 50, 41)
>>> button7x, button7y = pyautogui.center(button7location)
>>> button7x, button7y
(1441, 582)
>>> pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found


>>> import pyautogui
>>> x, y = pyautogui.locateCenterOnScreen('calc7key.png')
>>> pyautogui.click(x, y)


pyautogui.getWindows() # returns a dict of window titles mapped to window IDs
pyautogui.getWindow(str_title_or_int_id) # returns a “Win” object
win.move(x, y)
win.resize(width, height)
win.maximize()
win.minimize()
win.restore()
win.close()
win.position() # returns (x, y) of top-left corner
win.moveRel(x=0, y=0) # moves relative to the x, y of top-left corner of the window
win.clickRel(x=0, y=0, clicks=1, interval=0.0, button=’left’) # click relative to the x, y of top-left corner of the window
Additions to screenshot functionality so that it can capture specific windows instead of full screen.