import pyperclip
from typing import List


content: str = pyperclip.paste()
res: List[str] = content.split('\n')

for index, r in enumerate(res):
    print(f'Found res[{index}]: {r}')
