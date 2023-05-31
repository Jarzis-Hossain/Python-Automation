from pyautogui import moveTo, press, FAILSAFE, size
import pyautogui
from keyboard import is_pressed
from subprocess import check_output
from base64 import b64encode, b64decode
from time import sleep
pyautogui.FAILSAFE = False
my_code = """
screenWidth, screenHeight = size()
middleX = int(screenWidth / 2)
middleY = int(screenHeight / 2)
while True:
    moveTo(middleX, middleY)
    press("esc")
    moveTo(middleX, middleY)
    if is_pressed('q+s+e'):
        break"""
encoded_string = b64encode(my_code.encode("utf-8"))
sleep(2)
decoded_string = b64decode(encoded_string)
exec(decoded_string)
