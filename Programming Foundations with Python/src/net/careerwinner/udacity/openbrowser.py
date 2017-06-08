import webbrowser
import time

var = 1

print("The program started on " + time.ctime())
while(var <= 3 ):
    time.sleep(60*60*50)
    webbrowser.open("http://music.163.com/#/outchain/2/409872465/")
    var = var +1

