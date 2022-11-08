import webbrowser
import time
import pyperclip
import pyautogui


webbrowser.open("https://www.google.com/", new=2, autoraise=True)
time.sleep(1)
pyperclip.copy("平泉町 観光")


pyautogui.keyDown("command")
pyautogui.press("v")

pyautogui.keyUp("command")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

# pg.screenshot()
s = pyautogui.screenshot("screenshot.png")
s.show()
