# import geopandas as gpd
import matplotlib.pyplot as plt  # type: ignore

# Monkey patch!!
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import Util


def lecture_01() -> None:
    print('geopandas 01 NEW lecture 01')
    print(f'{Util.GEO_02_NEW_DATA}')


def exercise_01() -> None:
    print('geopandas 01 NEW lecture 01')


def challenge_01() -> None:
    print('Challenge GeoPandas 01 NEW')
