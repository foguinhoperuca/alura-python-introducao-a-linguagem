import random
import time

import pyautogui as pag

curr_coords = pag.position()
afk_counter = 0

while True:
    if pag.position == curr_coords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_coords = pag.position

    if afk_counter > 2:
        x = random.randint(2560, 5120)
        y = random.randint(1, 1440)
        pag.moveTo(x, y, 0.5)
        curr_coords = pag.position()

    print(f'AFK Counter: {afk_counter}')
    time.sleep(1)
