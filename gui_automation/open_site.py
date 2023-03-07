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

easter_egg_button_location = (3240, 867)
pyautogui.click(easter_egg_button_location, button='right')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('left')
pyautogui.press('right')
pyautogui.press('left')
pyautogui.press('right')
pyautogui.press('b')
pyautogui.press('a')
breakpoint()


# pyautogui.position()
