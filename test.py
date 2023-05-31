import pyautogui
from time import sleep

sleep(3)
print(pyautogui.size())

while True:
    pyautogui.moveTo(135, 274, 0.5)
    pyautogui.click()
    pyautogui.moveTo(1264, 404, 0.5)
    pyautogui.click()
    pyautogui.typewrite("Replace this string with the reciver's email")
    sleep(0.5)
    pyautogui.move(0, 400)
    pyautogui.click()
    sleep(1)
    pyautogui.typewrite("Replace this string with the message that you want to send")
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'enter')
