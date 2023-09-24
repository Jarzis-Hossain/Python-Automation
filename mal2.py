import tkinter as tk
import signal
import pyautogui as pg
def disable_mouse():
    screenWidth, screenHeight = pg.size()
    cornnerX = screenWidth
    middleY = int(screenHeight / 2)
    pg.moveTo(cornnerX, middleY)
    root.after(300, disable_mouse)

def disable_event():
    pass

def ignore_kill_signals():
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.overrideredirect(True)
root.attributes('-topmost', True)

ignore_kill_signals()
disable_mouse()
root.mainloop()
