
import pyautogui
import time
import winsound

time.sleep(5)
image=pyautogui.screenshot()
winsound.Beep(800,2000)


path=pyautogui.screenshot("path.png")