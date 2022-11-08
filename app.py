import webbrowser
import time
import pyperclip
import pyautogui as pg


webbrowser.open("https://www.google.com/", new=2, autoraise=True)
time.sleep(1)
pyperclip.copy("平泉町 観光")


pg.keyDown("command")
pg.press("v")

pg.keyUp("command")
time.sleep(1)
pg.press("enter")
