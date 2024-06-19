import os
from typing import List

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Polygon, Point, LineString, MultiPolygon


def generate_figure_from_shape(in_file: str, out: str, plot_original: bool = True) -> None:  # # noqa: E501
    shp: gpd.geodataframe.GeoDataFrame = gpd.read_file(in_file)
    if plot_original:
        shp.plot()
    else:
        shp.plot(color='white', edgecolor='black', figsize=(15, 8))

    plt.savefig(out)
    print(f'Columns is: {shp.columns}')
    print(shp)
    # logging.debug(Util.warning(shp))


def lecture_01() -> None:
    p1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    g = gpd.GeoSeries(p1)
    print(g)
    g.plot()
    plt.savefig('geo/data/output/N01_polygon-01')

    p2 = Polygon([(0, 0), (1, 0), (1, 1)])
    g2 = gpd.GeoSeries(p2)
    print(g2)
    g2.plot()
    plt.savefig('geo/data/output/N01_polygon-02')

    g = gpd.GeoSeries([p1, p2])
    g.plot(cmap="tab20")
    plt.savefig('geo/data/output/N01_polygon-03')

    p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
    g = gpd.GeoSeries([p1, p2, p3])
    g.plot(cmap="tab20")
    plt.savefig('geo/data/output/N01_polygon-04')

    p4 = LineString([(0, 1), (3, 0), (1, 1)])
    g = gpd.GeoSeries([p1, p2, p3, p4])
    g.plot(cmap="tab10")
    plt.savefig('geo/data/output/N01_polygon-05')

    p5 = Point(0.5, 0.5)
    g = gpd.GeoSeries([p1, p2, p3, p4, p5])
    g.plot(cmap="tab10")
    plt.savefig('geo/data/output/N01_polygon-06')

    print(g)

    p6 = Polygon([(1, 0), (1.5, 0.4), (2, 0)])
    p7 = Polygon([(1, 1), (1.5, 0.6), (2, 1)])

    p8 = MultiPolygon([p6, p7])

    g = gpd.GeoSeries([p1, p2, p3, p4, p5, p8])
    g.plot(cmap="tab10")
    plt.savefig('geo/data/output/N01_polygon-07')
    print(g)


def exercise_01() -> None:
    p1 = Polygon([(0, 0), (2, 1), (2, 0), (0, 1)])
    g = gpd.GeoSeries([p1])
    g.plot(cmap='tab10', figsize=(15, 8))
    plt.savefig('geo/data/output/E01_answer-a')

    figuras = []
    for i in [0.5, 0.2, 0]:
        figuras.append(Polygon([(0 - i, 0 + i), (1 - i, 0 - i), (1 + i, 1 - i), (0 + i, 1 + i)]))  # noqa: E501

    g = gpd.GeoSeries(figuras)
    g.plot(cmap='Spectral', figsize=(15, 8))
    plt.savefig('geo/data/output/E01_answer-b')

    p1 = Polygon([(0, 0), (1, 0.5), (0, 1)])
    p2 = Polygon([(2, 0), (1, 0.5), (2, 1)])
    g = gpd.GeoSeries([p1, p2])
    g.plot(cmap='tab10', figsize=(15, 8))
    plt.savefig('geo/data/output/E01_answer-c')

    p1 = Point(0.5, 0.5).buffer(0.5)
    p2 = MultiPolygon([Point(0.25, 0.6).buffer(0.1), Point(0.75, 0.6).buffer(0.1)])  # noqa: E501
    p3 = MultiPolygon([Point(0.25, 0.6).buffer(0.02), Point(0.75, 0.6).buffer(0.02)])  # noqa: E501
    p4 = LineString([(0.2, 0.25), (0.8, 0.25)])
    g = gpd.GeoSeries([p1, p2, p3, p4])
    g.plot(cmap='Wistia', figsize=(15, 8))
    plt.savefig('geo/data/output/E01_answer-d')


def lecture_02_a() -> None:
    rj = gpd.read_file('geo/data/map_rj/33MUE250GC_SIR.shp')

    rj_city = rj[rj['NM_MUNICIP'] == 'RIO DE JANEIRO']
    print(rj_city)
    rj_city.plot(color='orange', edgecolor='black', figsize=(15, 8))
    plt.savefig('geo/data/output/rj_city')

    out_dir: str = 'geo/data/rj_city'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    rj_city.to_file(os.path.join(out_dir, 'rj_city.shp'))


def lecture_02_b() -> None:
    data = pd.read_table('geo/data/data.txt')
    list_points: List = list(zip(data.Longitude, data.Latitude))
    print(data)
    print(list_points[:5])

    points: List[Point] = [Point(pos) for pos in zip(data.Longitude, data.Latitude)]  # noqa: E501
    crs = {
        'proj': 'latlong',
        'ellps': 'WGS84',
        'datum': 'WGS84',
        'no_defs': True
    }
    geo_data: gpd.geodataframe.GeoDataFrame = gpd.GeoDataFrame(data, crs=crs, geometry=points)  # noqaa: E501
    print(geo_data)
    out_dir: str = 'geo/data/rj_city'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    geo_data.to_file(os.path.join(out_dir, 'rj_dataset.shp'))
    geo_data.plot(figsize=(15, 8), alpha=0.2)
    plt.savefig('geo/data/output/N-02_lecture-02')


def lecture_03() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    rj.plot()
    plt.savefig('geo/data/output/rj_city')
    geo_data = gpd.read_file('geo/data/rj_city/rj_dataset.shp')
    geo_data.plot()
    plt.savefig('geo/data/output/rj_dataset')
    print(rj.crs)
    print('-----------')
    print(geo_data.crs)
    print('===========')

    rj.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    geo_data.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    print(rj.crs)
    print('-----------')
    print(geo_data.crs)
    print('===========')
    # rj.to_file('geo/data/rj_city/rj_city.shp')
    # geo_data.to_file('geo/data/rj_city/rj_dataset.shp')


def lecture_04() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    geo_data = gpd.read_file('geo/data/rj_city/rj_dataset.shp')
    base_map = rj.plot(color='grey', edgecolor='black', figsize=(15, 8))
    print(base_map)

    geo_data.plot(ax=base_map, figsize=(15, 8), alpha=0.2)
    plt.savefig('geo/data/output/basemap')
    res: bool = geo_data.iloc[0].geometry.within(rj.iloc[0].geometry)
    print(res)
    res2: bool = rj.iloc[0].geometry.contains(geo_data.iloc[0].geometry)
    print(res2)
    serie = geo_data['geometry'].within(rj.iloc[0].geometry)
    print(len(geo_data['geometry']))
    print(len(serie))

    sample = geo_data.iloc[:12]
    sample.plot(ax=base_map, figsize=(15, 8), alpha=1)
    plt.savefig('geo/data/output/sample')

    before = geo_data.shape[0]
    print(before)
    filtered = geo_data[geo_data['geometry'].within(rj.iloc[0].geometry)]
    after = filtered.shape[0]
    print(after)
    result = before - after
    print(result)
    filtered.plot(ax=base_map, figsize=(15, 8), alpha=0.1)
    plt.savefig('geo/data/output/filtered')
    filtered.to_file('geo/data/rj_city/filtered.shp')


def lecture_05() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    geo_data = gpd.read_file('geo/data/rj_city/filtered.shp')
    metro = gpd.read_file('geo/data/estacoes_metro.geojson')
    metro = metro.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs')  # noqa: E501
    # print(metro)
    base_map = rj.plot(color='grey', edgecolor='black', figsize=(15, 8))
    geo_data.plot(ax=base_map, color='orange', alpha=0.2)
    metro.plot(ax=base_map, color='black', markersize=50)
    plt.savefig('geo/data/output/metro_rj')

    distances = metro.distance(geo_data.iloc[0].geometry)
    print(distances.min())
    print(distances.max())

    geo_data['Dist_Metro'] = geo_data['geometry'].apply(lambda x: metro.distance(x).min())  # noqa: E501
    print(geo_data['Dist_Metro'])
    coef = geo_data['Valor'].corr(geo_data['Dist_Metro'])
    print(coef)


def exercise_05() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    # rj.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    base_map = rj.plot(color='grey', edgecolor='black', figsize=(15, 8))

    data = [
        ('A', '-22.9531', '-43.1884'),
        ('B', '-23.0278', '-43.4665'),
        ('C', '-22.8463', '-43.3007'),
        ('D', '-22.8969', '-43.3165')
    ]
    geo = gpd.GeoDataFrame(data, crs={'init': 'epsg:4326'}, geometry=[Point((el[2], el[1])) for el in data])  # noqa: E501
    geo.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501

    metro = gpd.read_file('geo/data/estacoes_metro.geojson')
    metro.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501

    geo['Metro_MIN'] = geo['geometry'].apply(lambda x: metro.iloc[metro.distance(x).idxmin()].Nome)  # noqa: E501
    geo['Dist_Metro_MIN'] = geo['geometry'].apply(lambda x: round(metro.distance(x).min(), 2))  # noqa: E501
    geo['Metro_MAX'] = geo['geometry'].apply(lambda x: metro.iloc[metro.distance(x).idxmax()].Nome)  # noqa: E501
    geo['Dist_Metro_MAX'] = geo['geometry'].apply(lambda x: round(metro.distance(x).max(), 2))  # noqa: E501

    print(geo)
    geo.plot(ax=base_map, color='red', alpha=0.2)
    metro.plot(ax=base_map, color='black', markersize=50)
    plt.savefig('geo/data/output/exercise_05')


def lecture_06_01() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    geo_data = gpd.read_file('geo/data/rj_city/filtered.shp')
    metro = gpd.read_file('geo/data/estacoes_metro.geojson')
    metro.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    trem = gpd.read_file('geo/data/estacoes_trem.geojson')
    trem.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    trem = trem[trem.within(rj.iloc[0].geometry)]
    brt = gpd.read_file('geo/data/estacoes_brt.geojson')
    brt.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501

    base_map = rj.plot(color='grey', edgecolor='black', figsize=(15, 8))
    geo_data.plot(ax=base_map, color='orange', alpha=0.2)
    metro.plot(ax=base_map, color='black', markersize=50)
    trem.plot(ax=base_map, color='red', markersize=50)
    brt.plot(ax=base_map, color='blue', markersize=50)
    plt.savefig('geo/data/output/lecture_06_01')

    transport = pd.concat([metro.geometry, trem.geometry, brt.geometry], ignore_index=True)  # noqa: E501
    geo_data['Dist_Transp'] = geo_data['geometry'].apply(lambda x: transport.distance(x).min())  # noqa: E501
    print(geo_data.head())

    geo_data.to_file('geo/data/rj_city/transport.shp')


def lecture_06_02() -> None:
    rj = gpd.read_file('geo/data/rj_city/rj_city.shp')
    base_map = rj.plot(color='lightgrey', edgecolor='black', figsize=(15, 8))
    geo_data = gpd.read_file('geo/data/rj_city/filtered.shp')
    beachs = gpd.read_file('geo/data/cobertura_vegetal_e_uso_da_terra_2016.geojson')  # noqa: E501
    beachs.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    beachs = beachs[beachs['legenda'] == 'Praia']
    geo_data['Dist_Beach_KM'] = geo_data['geometry'].apply(lambda x: beachs.distance(x).min())  # noqa: E501
    print(geo_data)

    # geo_data.plot(ax=base_map, color='orange', alpha=0.2)

    beachs.plot(ax=base_map, color='white', edgecolor='black', figsize=(15, 8))
    plt.savefig('geo/data/output/lecture_06_02')
    print(beachs['legenda'].value_counts())

    # print(geo_data.head())


def exercise_06_01() -> None:
    Square = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    Point_A = Point(1.1, 1.1)
    Point_B = Point(0.5, 0.5)
    points = gpd.GeoDataFrame(geometry=[Point_A, Point_B], index=['A', 'B'])
    polygon = gpd.GeoDataFrame(geometry=[Square], index=['P'])

    base = polygon.plot(color='white', edgecolor='red', figsize=(15, 8))
    points.plot(ax=base, markersize=150)
    plt.savefig('geo/data/output/exercise_06_01')

    print(points.loc['B'].geometry.within(polygon.iloc[0].geometry))
    print(polygon.iloc[0].geometry.contains(points.loc['A'].geometry))
    print(points.distance(points.loc['A'].geometry).iloc[0])
    print(points.distance(points.loc['B'].geometry).loc['B'])
    print(polygon['geometry'].apply(lambda x: points.distance(x))['B'].iloc[0])


def exercise_06_02() -> None:
    A = pd.DataFrame([1, 2], columns=['A'])
    B = pd.DataFrame([3, 4], columns=['A'])
    C = pd.DataFrame([5, 6], columns=['A'])

    print(A, B, C)
    print('---')
    print(A)
    print('---')
    print(B)
    print('---')
    print(C)
    print("***************************")
    # # FIXME not same as A.append. It was changed in pandas +2.0
    # A0 = A._append([B, C], ignore_index=True)
    # print('A0')
    # print(A0)
    # print('+++++++++++++++++++++++++++++++++++++++++')
    A1 = A.merge(B, how='outer').merge(C, how='outer')
    print('A1')
    print(A1)
    print('+++++++++++++++++++++++++++++++++++++++++')
    A2 = pd.concat([A, B, C], ignore_index=True)
    print('A2')
    print(A2)
    print('+++++++++++++++++++++++++++++++++++++++++')
    A3 = pd.concat([A, B, C], sort=True)
    print('A3')
    print(A3)
    print('+++++++++++++++++++++++++++++++++++++++++')


def exercise_06_03() -> None:
    rj = gpd.read_file('geo/data/map_rj/33MUE250GC_SIR.shp')
    rj.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    capital = rj[rj['NM_MUNICIP'] == 'RIO DE JANEIRO']
    capital.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    rj['DIST_CAPITAL'] = rj['geometry'].apply(lambda x: round(capital.distance(x), 2))  # noqa: E501
    # print(rj)
    # print(rj['DIST_CAPITAL'].max())
    # print(rj['DIST_CAPITAL'].idxmax())
    # print('---------------')
    max_dist = rj[rj['NM_MUNICIP'] == rj.iloc[rj['DIST_CAPITAL'].idxmax()]['NM_MUNICIP']]  # noqa: E501
    max_dist.to_crs('+proj=utm +zone=23 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=km +no_defs', inplace=True)  # noqa: E501
    # print(max_dist['NM_MUNICIP'])
    # print('======================')
    print(max_dist)

    base_map = rj.plot(color='lightgrey', edgecolor='black', figsize=(15, 8))
    capital.plot(ax=base_map, color='red')
    max_dist.plot(ax=base_map, color='yellow')

    plt.savefig('geo/data/output/exercise_06_03')
