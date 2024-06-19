import argparse
import logging
# Monkey patch!!
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util import Util

import geopandas_01
import geopandas_02
import geopandas_01_new
import geopandas_02_new


if __name__ == "__main__":
    print("")
    print("***************************************")
    print("|| Python Geo Processing: GeoPandas  ||")
    print("***************************************")
    print("")
    logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)

    # generate_figure_from_shape(in_file='geo/data/map_rj/33MUE250GC_SIR.shp', out='geo/data/output/rj_original', plot_original=True)  # noqa: E501
    # generate_figure_from_shape(in_file='geo/data/map_rj/33MUE250GC_SIR.shp', out='geo/data/output/rj_black-white', plot_original=False)  # noqa: E501

    # lecture_01()
    # exercise_01()

    # lecture_02_a()
    # lecture_02_b()

    # lecture_03()

    # lecture_04()

    # lecture_05()
    # exercise_05()

    # lecture_06_01()
    # exercise_06_01()
    # exercise_06_02()
    # lecture_06_02()
    # exercise_06_03()

    parser = argparse.ArgumentParser(description="Geoprocessing Alura!!", epilog="Study")  # noqa: E501
    parser.add_argument("-c", "--course", choices=["geo01", "geo01_new", "geo02", "geo02_new"], help="Set course")  # noqa: E501
    parser.add_argument("-a", "--activity", choices=["lecture", "exercise", "challenge"], help="Set activity")  # noqa: E501
    parser.add_argument("-id", "--identification", type=str, help="Define which activity will run")  # noqa: E501
    args = parser.parse_args()
    print(args)

    if args.course == 'geo01':
        module = geopandas_01
    elif args.course == 'geo02':
        module = geopandas_02
    elif args.course == 'geo01_new':
        module = geopandas_01_new
    elif args.course == 'geo02_new':
        module = geopandas_02_new

    method: str = f'{args.activity}_{args.identification}'
    print(f'Choosen method: {method}')
    exec_activity = getattr(module, method)
    exec_activity()

    sys.exit(0)
