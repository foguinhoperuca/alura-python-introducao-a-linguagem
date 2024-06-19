import geopandas as gpd
import matplotlib.pyplot as plt  # type: ignore

# Monkey patch!!
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import Util


def lecture_01() -> None:
    print('geopandas 02 lecture 01')
    rj = gpd.read_file('alura_curso_geopandas_02/dados/RJ_Municipios_2022.shp')  # type: ignore[attr-defined]
    print(rj.head())
    print(type(rj))
    rj.plot()
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_lecture_01_original')
    rj.plot(color='white', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_lecture_01_black-white')

    print(rj.columns)
    rj = rj[rj['NM_MUN'] == 'Rio de Janeiro']
    print(rj)
    rj.plot(color='orange', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_lecture_01_only_rj')
    rj.to_file(f'{Util.GEO_02_NEW_INPUT}/rj_municip.shp')
    rj_municip = gpd.read_file(f'{Util.GEO_02_NEW_INPUT}/rj_municip.shp')  # type: ignore[attr-defined]
    rj_municip.plot(color='green', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_lecture_01_rj_municip_green')  # noqa: E501


def exercise_01() -> None:
    print('geopandas 02 lecture 01')


def challenge_01() -> None:
    print('Challenge GeoPandas 02 NEW')
    sp_state = gpd.read_file(f'{Util.GEO_02_NEW_DATA}/Estado_SP.shp')  # type: ignore[attr-defined]
    print(sp_state.head())
    print('-------------')
    print(sp_state.columns)
    print('-------------')
    print(sp_state)
    sp_state.plot(color='lightgrey', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_challenge_state')

    sp_municip = sp_state[sp_state['NM_MUN'] == 'São Paulo']
    sp_municip.plot(color='blue', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_challenge_sp_municip')
    sp_municip.to_file(f'{Util.GEO_02_NEW_INPUT}/sp_municip.shp')

    sp = gpd.read_file(f'{Util.GEO_02_NEW_INPUT}/sp_municip.shp')  # type: ignore[attr-defined]
    sp.plot(color='red', edgecolor='black')
    plt.savefig(f'{Util.GEO_02_NEW_OUTPUT}/geopandas02_challenge_sp')
