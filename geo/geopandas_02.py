import shutil
import sys
import os
from typing import List
import zipfile

import folium
from folium.plugins import MarkerCluster
import geopandas as gpd  # type: ignore
import pandas as pd      # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from shapely.geometry import Polygon, Point, LineString, MultiPolygon  # type: ignore

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
    print(len(filenames))

    # for item in filenames:
    #     zip_ref = zipfile.ZipFile(f'{Util.GEO_02_THIRD_PARTY}/01.Dados/Mapas/RJ-SETOR/DADOS/{item}')
    #     zip_ref.extractall(dir_tmp)
    #     zip_ref.close()

    sectors = pd.concat([gpd.read_file(f'{dir_tmp}/{item[:-4]}_setor.shp') for item in filenames], ignore_index=True)
    print(sectors.crs)
    sectors.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    print(sectors.crs)

    sectors.plot(color='white', edgecolor='black')  # , figzise=(15, 8) doesn't work...
    plt.savefig(f'{Util.GEO_02_OUTPUT}/full_RJ-SETOR')
    sectors.to_file(f'{Util.GEO_02_INPUT}/RJ-SETOR.shp')

    botafogo = sectors[sectors['NM_BAIRRO'] == 'Botafogo']
    botafogo.plot(color='white', edgecolor='black')  # , figzise=(15, 8) not working...
    plt.savefig(f'{Util.GEO_02_OUTPUT}/botafogo')


def lecture_02() -> None:
    print('geopandas 02 lecture 02')

    census = pd.read_excel(f'{Util.GEO_02_THIRD_PARTY}/Censo2010/01.Dados/Censo 2010/RJ/EXCEL/Basico_RJ.xls')
    sector = gpd.read_file(f'{Util.GEO_02_INPUT}/RJ-SETOR.shp')
    print(census.head())
    print('-------------------------------')
    print('CENSUS: ', type(census), len(census), len(census.columns), census.dtypes['Cod_setor'])
    print('SECTOR: ', type(sector), len(sector), len(sector.columns), sector.dtypes['CD_GEOCODI'])
    census['Cod_setor'] = census['Cod_setor'].astype(str)
    print('CENSUS: ', type(census), len(census), len(census.columns), census.dtypes['Cod_setor'])
    sector = pd.merge(sector, census, left_on='CD_GEOCODI', right_on='Cod_setor', how='left')
    print('SECTOR: ', type(sector), len(sector), len(sector.columns), sector.dtypes['CD_GEOCODI'])
    sector.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    sector.to_file(f'{Util.GEO_02_INPUT}/RJ-SETOR.shp')

    dataset = gpd.read_file(f'{Util.GEO_02_INPUT}/DATASET.shp')
    print('DATASET: ', type(dataset), len(dataset), len(dataset.columns), dataset.crs)
    dataset.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501

    basemap = sector.plot(color='white', edgecolor='grey')
    dataset.plot(ax=basemap, color='blue', markersize=1)  # , figzise=(15, 8) doesn't work...
    plt.savefig(f'{Util.GEO_02_OUTPUT}/dataset')

    dataset2 = gpd.sjoin(dataset, sector, how='left', op='within')  # op: [intersects | within | contains]
    print(dataset2.index.duplicated(keep='first'))
    duplicated = dataset2[dataset2.index.duplicated(keep='first')]
    print(duplicated)
    not_duplicated = dataset2[~dataset2.index.duplicated(keep='first')]
    print(not_duplicated)
    not_duplicated.to_file(f'{Util.GEO_02_INPUT}/DATASET_not_duplicated.shp')


def exercise_02() -> None:
    print('geopandas 02 lecture 02 exercise 02')
    p = {'Ident': 'Polygon A', 'geometry': Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])}
    polygon = gpd.GeoDataFrame([p])

    pt = {
        'Ident': ['A', 'B', 'C', 'E', 'F', 'G'],
        'geometry': [
            Point(0.5, 0.0),
            Point(0.3, 0.7),
            Point(0.8, 0.4),
            Point(1.0, 1.0),
            Point(1.1, 1.1),
            Point(-0.1, -0.1)]
    }
    points = gpd.GeoDataFrame(pt)

    base = polygon.plot(color='white', edgecolor='blue', figsize=(15, 8))
    points.plot(ax=base, color='orange', markersize=100)
    plt.savefig(f'{Util.GEO_02_OUTPUT}/geo02_lecture_02_exercise_02')

    sjoin_a = gpd.sjoin(polygon, points, how='inner', op='contains')
    print(sjoin_a)
    print('----------------- A -----------------')
    sjoin_b = gpd.sjoin(points, polygon, how='inner', op='within')
    print(sjoin_b)
    print('----------------- B -----------------')
    sjoin_c = gpd.sjoin(polygon, points, how='left', op='intersects')
    print(sjoin_c)
    print('----------------- C -----------------')
    sjoin_d = gpd.sjoin(polygon, points, how='right', op='intersects')
    print(sjoin_d)
    print('----------------- D -----------------')


def lecture_03() -> None:
    print('geopandas 02 lecture 03')

    sector = gpd.read_file(f'{Util.GEO_02_INPUT}/RJ-SETOR.shp')
    print('SECTOR: ', type(sector), len(sector), len(sector.columns), sector.dtypes['CD_GEOCODI'])
    # sector.plot(color='white', edgecolor='black', figsize=(15, 8))
    # plt.savefig(f'{Util.GEO_02_OUTPUT}/geo02_lecture_03_before')
    print(sector.head())
    sector = sector.to_crs({'init': 'epsg:4326'})
    sector_m = sector[['NM_BAIRRO', 'geometry']]
    neighborhood = sector_m.dissolve(by='NM_BAIRRO')
    neighborhood.plot(color='white', edgecolor='black', figsize=(15, 8))
    plt.savefig(f'{Util.GEO_02_OUTPUT}/neighborhood')

    sector_m_02 = sector[['NM_BAIRRO', 'geometry', 'V002']]
    neighborhood_02 = sector_m_02.dissolve(by='NM_BAIRRO', aggfunc='sum')
    neighborhood_02.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    neighborhood_02.reset_index(inplace=True)
    dir_neighborhood = f'{Util.GEO_02_INPUT}/neighborhood'
    if not os.path.exists(dir_neighborhood):
        os.makedirs(dir_neighborhood)

    neighborhood_02.to_file(f'{dir_neighborhood}/RJ-BAIRRO.shp')
    breakpoint()


def lecture_04() -> None:
    print('geopandas 02 lecture 04')
    crs = {'init': 'epsg:4326'}
    rj = gpd.read_file(f'{Util.GEO_02_INPUT}/RJ-MUNIC.shp')
    rj.to_crs(crs, inplace=True)

    rj2 = gpd.read_file(f'{Util.GEO_02_INPUT}/33MUE250GC_SIR.shp')
    rj2.to_crs(crs, inplace=True)
    rj2.plot(color='white', edgecolor='black', figsize=(15, 8))
    plt.savefig(f'{Util.GEO_02_OUTPUT}/rj2')
    rj2_city = rj2[rj2['NM_MUNICIP'] == 'RIO DE JANEIRO']
    rj2_city.plot(color='white', edgecolor='black', figsize=(15, 8))
    plt.savefig(f'{Util.GEO_02_OUTPUT}/rj2_city')

    # geo_dados = gpd.read_file(f'{Util.GEO_02_INPUT}/DATASET_not_duplicated.shp')
    # sector = gpd.read_file(f'{Util.GEO_02_INPUT}/RJ-SETOR.shp')
    # sector = sector.fillna(0)
    neighborhood = gpd.read_file(f'{Util.GEO_02_INPUT}/neighborhood/RJ-BAIRRO.shp')
    neighborhood.to_crs(crs, inplace=True)

    y = rj2_city.centroid.y.iloc[0]
    x = rj2_city.centroid.x.iloc[0]
    basemap = folium.Map([y, x], zoom_start=11, tiles='OpenStreetMap')
    # basemap.choropleth(rj_city)  # FIXME not work!!

    base = folium.Map([y, x], zoom_start=11, tiles='OpenStreetMap')
    geojson_rj = folium.GeoJson(rj2_city)
    geojson_rj.add_child(folium.Popup(rj2_city.NM_MUNICIP.iloc[0]))
    geojson_rj.add_to(base)
    base.save(f'{Util.GEO_02_OUTPUT}/folium_lecture_04-01.html')

    base_neighborhood = folium.Map([y, x], zoom_Start=11, tiles='OpenStreetMap')
    style_function = lambda feature: {
        'fillColor': 'green' if feature['properties']['V002'] > 50000 else 'yellow',
        'color': 'black',
        'weight': 1
    }
    for i in range(len(neighborhood)):
        geo = folium.GeoJson(neighborhood[i:i + 1], name=neighborhood['NM_BAIRRO'][i], style_function=style_function)
        label = '{} - {} habitantes'.format(neighborhood['NM_BAIRRO'][i], neighborhood['V002'][i])
        folium.Popup(label).add_to(geo)
        # base_neighborhood.add_child(folium.Marker(location=[neighborhood['geometry'][i].centroid.y, neighborhood['geometry'][i].centroid.x], popup="<h4>" + str(neighborhood['NM_BAIRRO'][0]) + "</h4><h5>" + str(neighborhood['V002'][0]) + "</h5><p>TODO put something here</p>", icon=folium.Icon(color='red', prefix='fa', icon='fas fa-home')))
        geo.add_to(base_neighborhood)

    folium.LayerControl().add_to(base_neighborhood)
    base_neighborhood.save(f'{Util.GEO_02_OUTPUT}/folium_lecture_04-02_neighborhood.html')

    # Example to put a marker
    base_neighborhood.add_child(folium.Marker(location=[neighborhood['geometry'][0].centroid.y, neighborhood['geometry'][0].centroid.x], popup="<h4>" + str(neighborhood['NM_BAIRRO'][0]) + "</h4><h5>" + str(neighborhood['V002'][0]) + "</h5><p>TODO put something here</p>", icon=folium.Icon(color='red', prefix='fa', icon='fas fa-home')))
    # base.choropleth(rj, name='Rio de Janeiro', line_color='Black', line_weight=3, fill_opacity=0)
    base_neighborhood.save(f'{Util.GEO_02_OUTPUT}/folium_lecture_04-03_marker.html')

    # TODO finish marker cluster and final class
    # base.choropleth(rj,
    #             name='Rio de Janeiro', 
    #             line_color='Black', 
    #             line_weight=3, 
    #             fill_opacity=0)
    cluster = MarkerCluster()

    breakpoint()


def challenge_01() -> None:
    print('Challenge GeoPandas 02')
