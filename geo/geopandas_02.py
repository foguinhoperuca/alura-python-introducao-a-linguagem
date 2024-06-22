import shutil
import sys
import os
from typing import List
import zipfile

import geopandas as gpd
import matplotlib.pyplot as plt  # type: ignore

# Monkey patch!!
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import Util

def lecture_01() -> None:
    print('geopandas 02 lecture 01')
    dir_tmp: str = f'{Util.GEO_02_THIRD_PARTY}/01.Dados/Mapas/RJ-SETOR/TEMP'
    if not os.path.exists(dir_tmp):
        os.makedirs(dir_tmp)

    filenames: List[str] = []
    for _, _, files in os.walk(f'{Util.GEO_02_THIRD_PARTY}/01.Dados/Mapas/RJ-SETOR/DADOS'):
        filenames = files

    print(f'{Util.GEO_02_THIRD_PARTY}/01.Dados/Mapas/RJ-SETOR/DADOS')
    print(filenames[:10])
    print(len(filenames))

    for item in filenames:
        zip_ref = zipfile.ZipFile(f'{Util.GEO_02_THIRD_PARTY}/01.Dados/Mapas/RJ-SETOR/DADOS/{item}')
        zip_ref.extractall(dir_tmp)
        zip_ref.close()


def exercise_01() -> None:
    print('geopandas 02 lecture 01')


def challenge_01() -> None:
    print('Challenge GeoPandas 02')
