#it's for ubuntu linux
#install the packages before running the script
#sudo apt-get install scrot
#sudo pip install opencv-python

#pyautogui docs - https://pyautogui.readthedocs.io/en/latest/

#if you get this error(Xlib.error.DisplayConnectionError: Can't connect to display ":0": b'No protocol specified\n'), use the  command "xhost +"

#pyautogui - used to automate graphical user interface
import pyautogui

#shows the screen width and height
screenWidth, screenHeight = pyautogui.size()
print("Screen Width : " + str(screenWidth))
print("Screen Height : " + str(screenHeight))

#feed the screen shot of the element you have to click.  In this example I have used youtube bell button screen shot.
#note error will throw if the element is not in the screen
x,y = pyautogui.locateCenterOnScreen("bell.png",confidence = 0.5)
#print the width and height of the element
print("Element Width : " + str(x) + " Element Height : " + str(y))
#moves the curser to the element location
pyautogui.moveTo(x,y)
#clicks the element
pyautogui.click()
