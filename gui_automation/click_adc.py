import pyautogui
import time


img: str = "link_gestao_app_mobile2.png"
print(f'Alerta DEFESA CIVIL {img}')

coord = pyautogui.locateOnScreen(img)
# coord = pyautogui.locateCenterOnScreen(img)
# print(f'coord: {coord}')
breakpoint()

time.sleep(3)
pyautogui.click(pyautogui.locateCenterOnScreen(img))
