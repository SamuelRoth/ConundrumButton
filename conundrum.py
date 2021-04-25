# comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import serial
import pyautogui
import time

arduino = serial.Serial('/dev/cu.usbserial-1432410')
check_in = arduino.readline()
print(check_in)


while True:
    button_check = arduino.readline()
    button_string = str(button_check)
    contains_button = "button"
    print (button_string)
    if contains_button in button_string:
        print("starting screenshare automation")
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
        
        print ("loading conundrum")
        driver = webdriver.Firefox()
        driver.set_window_rect(20, -1040, 1880, 1900)
        driver.get("https://incoherency.co.uk/countdown/practice/")
        enable_music = driver.find_element_by_id("enable-music")
        enable_music.click()
        sixty_seconds = driver.find_element_by_id("60clock")
        sixty_seconds.click()
        conundrum_start = driver.find_element_by_id("conundrum-button")
        conundrum_start.click()
    