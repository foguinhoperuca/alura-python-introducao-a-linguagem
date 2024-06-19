import argparse
import logging
# Monkey patch!!
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# import types.ModuleType
import types
from typing import Dict, List

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

    parser = argparse.ArgumentParser(description="Geoprocessing Alura!!", epilog="Study")  # noqa: E501
    parser.add_argument("-c", "--course", choices=["geo01", "geo01_new", "geo02", "geo02_new"], help="Set course")  # noqa: E501
    parser.add_argument("-a", "--activity", choices=["lecture", "exercise", "challenge"], help="Set activity")  # noqa: E501
    parser.add_argument("-id", "--identification", type=str, help="Define which activity will run")  # noqa: E501
    args = parser.parse_args()
    print(args)

    if args.course == 'geo01':
        module: types.ModuleType = geopandas_01
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
