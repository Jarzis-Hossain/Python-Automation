from base64 import b64encode, b64decode
from pyautogui import moveTo, move, click, hotkey, sleep, typewrite
from webbrowser import open

nope = """
FAILSAFE = False
open('https://gmail.com')
sleep(11)
hotkey('win', 'up')
sleep(11)
while True:
    moveTo(115, 271, 0.5)
    click()
    sleep(6)
    moveTo(1422, 414, 0.5)
    click()
    sleep(1)
    typewrite("reciver's email")
    sleep(0.6)
    move(0, 400)
    click()
    sleep(0.5)
    typewrite("Email message")
    sleep(0.5)
    hotkey('ctrl', 'enter')
"""
eco = b64encode(nope.encode('UTF-8'))
sleep(4)
uco = b64decode(eco.decode('UTF-8'))
exec(uco)
eco = b64encode(nope.encode('UTF-8'))
