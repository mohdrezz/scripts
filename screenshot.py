import pyautogui
import time
from PIL import Image
import glob

x = 1
while x < 10 :
    pyautogui.screenshot('C:/Users/Zulman/Desktop/PythonScripts/screenshot/image_'+str(x)+'.png')
    x += 1
    time.sleep(5)