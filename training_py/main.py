import argparse
from enum import auto, StrEnum
import sys
from typing import Dict, List

import alura_conditional              # noqa: F401
import alura_loop                     # noqa: F401
import alura_regex                    # noqa: F401
import alura_lists_tuples             # noqa: F401
import alura_sets_dicts               # noqa: F401
import alura_fn                       # noqa: F401
import alura_async                    # noqa: F401
import alura_projects                 # noqa: F401


class TrainingTypes(StrEnum):
    CONDITIONAL = auto()
    LOOP = auto()
    REGEX = auto()
    LISTS_TUPLES = auto()
    SETS_DICTS = auto()
    FN = auto()
    ASYNC = auto()
    PROJECTS = auto()


class TrainingExerciseTypes(StrEnum):
    E01 = auto()
    E02 = auto()
    E03 = auto()
    E04 = auto()
    E05 = auto()
    E06 = auto()
    E07 = auto()
    E08 = auto()
    E09 = auto()
    E10 = auto()


if __name__ == "__main__":
    DEFAULT_EXERCISES: List[str] = [vl.name.lower() for vl in TrainingExerciseTypes]
    exercises: Dict[str, Dict[str, str]] = {
        f'{training_type.name.lower()}': {f'{key}': f'alura_{training_type.name.lower()}.exerc_{key.replace("e", "")}' for key in DEFAULT_EXERCISES} for training_type in TrainingTypes
    }
    parser = argparse.ArgumentParser(description="Training python...")
    parser.add_argument("-t", "--training", action="store_true", help="")
    subparser = parser.add_subparsers(dest='training', help="Choose training", required=True)
    for training_type in TrainingTypes:
        subparser.add_parser(training_type.name.lower()).add_argument('-e', '--exercise', choices=DEFAULT_EXERCISES, help=f'[{training_type.name}]Choose exercises: e1 - e10')

    args = parser.parse_args()
    eval(exercises[args.training][args.exercise])()

    sys.exit(0)
