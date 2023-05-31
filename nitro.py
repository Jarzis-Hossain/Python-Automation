import random
import string
import pyautogui as p
import keyboard

p.sleep(8)
def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    random_string1 = generate_random_string(4)
    random_string2 = generate_random_string(4)
    random_string3 = generate_random_string(4)
    random_string4 = generate_random_string(4)
    code = random_string1 + '-' + random_string2 + '-' + random_string3 + '-' + random_string4
    p.write(code)
    p.moveTo(1496, 249)
    p.click(1496, 249)
    p.click(991, 256)
    p.keyDown('ctrl')
    p.press('a')
    p.keyUp('ctrl')
    p.keyUp('ctrl')
    p.press('backspace')
    if keyboard.is_pressed('s'):
        break
