import argparse
import sys

import conditional
import loop
import regex
import lists_tuples


if __name__ == "__main__":  # noqa: C901
    parser = argparse.ArgumentParser(description="Training python...")
    parser.add_argument("-t", "--training", action="store_true", help="")
    subparser = parser.add_subparsers(dest='training', help="Choose training", required=True)
    subparser.add_parser('conditional').add_argument('-e', '--exercise', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    subparser.add_parser('loop').add_argument('-e', '--exercise', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    subparser.add_parser('regex').add_argument('-e', '--exercise', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    subparser.add_parser('lists_tuples').add_argument('-e', '--exercise', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    args = parser.parse_args()

    if args.training == 'conditional':
        if args.exercise == 'e01':
            conditional.exerc_01()
        elif args.exercise == 'e02':
            conditional.exerc_02()
        elif args.exercise == 'e03':
            conditional.exerc_03()
        elif args.exercise == 'e04':
            conditional.exerc_04()
        elif args.exercise == 'e05':
            conditional.exerc_05()
        elif args.exercise == 'e06':
            conditional.exerc_06()
        elif args.exercise == 'e07':
            conditional.exerc_07()
        elif args.exercise == 'e08':
            conditional.exerc_08()
        elif args.exercise == 'e09':
            conditional.exerc_09()
        elif args.exercise == 'e10':
            conditional.exerc_10()
        else:
            sys.exit(f"[CONDITIONAL] Failed execution. exercise don't recognized! {args.exercise=}")
    elif args.training == 'loop':
        if args.exercise == 'e01':
            loop.exerc_01()
        elif args.exercise == 'e02':
            loop.exerc_02()
        elif args.exercise == 'e03':
            loop.exerc_03()
        elif args.exercise == 'e04':
            loop.exerc_04()
        elif args.exercise == 'e05':
            loop.exerc_05()
        elif args.exercise == 'e06':
            loop.exerc_06()
        elif args.exercise == 'e07':
            loop.exerc_07()
        elif args.exercise == 'e08':
            loop.exerc_08()
        elif args.exercise == 'e09':
            loop.exerc_09()
        elif args.exercise == 'e10':
            loop.exerc_10()
        else:
            sys.exit(f"[LOOP] Failed execution. exercise don't recognized! {args.exercise=}")
    elif args.training == 'regex':
        if args.exercise == 'e01':
            regex.exerc_01()
        elif args.exercise == 'e02':
            regex.exerc_02()
        elif args.exercise == 'e03':
            regex.exerc_03()
        elif args.exercise == 'e04':
            regex.exerc_04()
        elif args.exercise == 'e05':
            regex.exerc_05()
        elif args.exercise == 'e06':
            regex.exerc_06()
        elif args.exercise == 'e07':
            regex.exerc_07()
        elif args.exercise == 'e08':
            regex.exerc_08()
        elif args.exercise == 'e09':
            regex.exerc_09()
        elif args.exercise == 'e10':
            regex.exerc_10()
        else:
            sys.exit(f"[REGEX] Failed execution. exercise don't recognized! {args.exercise=}")
    elif args.training == 'lists_tuples':
        if args.exercise == 'e01':
            lists_tuples.exerc_01()
        elif args.exercise == 'e02':
            lists_tuples.exerc_02()
        elif args.exercise == 'e03':
            lists_tuples.exerc_03()
        elif args.exercise == 'e04':
            lists_tuples.exerc_04()
        elif args.exercise == 'e05':
            lists_tuples.exerc_05()
        elif args.exercise == 'e06':
            lists_tuples.exerc_06()
        elif args.exercise == 'e07':
            lists_tuples.exerc_07()
        elif args.exercise == 'e08':
            lists_tuples.exerc_08()
        elif args.exercise == 'e09':
            lists_tuples.exerc_09()
        elif args.exercise == 'e10':
            lists_tuples.exerc_10()
        else:
            sys.exit(f"[LISTS TUPLES] Failed execution. exercise don't recognized! {args.exercise=}")

    sys.exit(0)
