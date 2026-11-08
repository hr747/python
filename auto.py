import pyautogui
from time import sleep

sleep(5)
for i in range(0, 9):
    pyautogui.write("I love you ", interval=0.25)
    pyautogui.press('enter')