import time

import pyautogui

# print(pyautogui.KEYBOARD_KEYS)

pyautogui.press('winleft')
time.sleep(2)
pyautogui.write('firefox')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.write('http://google.com')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

pyautogui.hotkey('winleft', 'e')
pyautogui.hotkey('ctrl', 'l')
time.sleep(2)
pyautogui.write('c:/universal/projects')
time.sleep(2)
pyautogui.press('enter')
