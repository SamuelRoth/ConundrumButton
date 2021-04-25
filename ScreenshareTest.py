import pyautogui
import time

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print(screenWidth)
print(screenHeight)
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

print("starting")

pyautogui.keyDown('command')
pyautogui.keyDown('shift')
pyautogui.keyDown('s')
pyautogui.keyUp('s')
pyautogui.keyUp('shift')
pyautogui.keyUp('command')
print("screen sharing enabled")

iconLocation = pyautogui.locateOnScreen('d2label.png')
print("found desktop2")
print(iconLocation)
if iconLocation != None:
    pyautogui.click((iconLocation.left/2), (iconLocation.top/2))

time.sleep(.5)

shareLocation = pyautogui.locateOnScreen('clickshare.png')
print("found share button")
print(shareLocation)
if shareLocation != None:
    pyautogui.click((shareLocation.left/2), (shareLocation.top/2))
