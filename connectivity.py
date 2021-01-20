import os
import cv2
import time
import requests
import re
cwd = os.getcwd()
list_ = os.listdir(cwd)
if not 'connection_lost.jpeg' in list_:
    print('please add an image with the name "connection_lost.jpeg" to this folder')
    exit()
else :
    path = cwd +'\\' + 'connection_lost.jpeg'
img = cv2.imread(path)
window = False

while(True):
    
    try:
        a = requests.get("https://www.google.com/search?q=hello&rlz=1C1CHBF_enIN877IN877&oq=hello&aqs=chrome.0.69i59j35i39i362l4j69i60...4.921j0j15&sourceid=chrome&ie=UTF-8")
        print(a)
    except:
        print('exception')
        if window == False :
            a = 'connection lost'
            print(a)
            print("printing window")
            cv2.imshow("connectivity",img)
            cv2.waitKey(1)
            time.sleep(1)
            window = True
            
    else:
        if window == True :
            print('destroying windows')
            time.sleep(1)
            cv2.destroyAllWindows()
            window = False

    time.sleep(2)
    
