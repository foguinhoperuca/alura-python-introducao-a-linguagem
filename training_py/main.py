import argparse
import sys

from conditional import exerc_01, exerc_02, exerc_03, exerc_04, exerc_05, exerc_06, exerc_07, exerc_08, exerc_09, exerc_10
import loop
import regex


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training python...")
    parser.add_argument("-t", "--training", action="store_true", help="")
    subparser = parser.add_subparsers(dest='training', help="Choose training", required=True)
    subparser.add_parser('conditional').add_argument('--routine', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    subparser.add_parser('loop').add_argument('--routine', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    subparser.add_parser('regex').add_argument('--routine', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
    args = parser.parse_args()

    if args.training == 'conditional':
        if args.routine == 'e01':
            exerc_01()
        elif args.routine == 'e02':
            exerc_02()
        elif args.routine == 'e03':
            exerc_03()
        elif args.routine == 'e04':
            exerc_04()
        elif args.routine == 'e05':
            exerc_05()
        elif args.routine == 'e06':
            exerc_06()
        elif args.routine == 'e07':
            exerc_07()
        elif args.routine == 'e08':
            exerc_08()
        elif args.routine == 'e09':
            exerc_09()
        elif args.routine == 'e10':
            exerc_10()
        else:
            sys.exit(f"[CONDITIONAL] Failed execution. Routine don't recognized! {args.routine=}")
    elif args.training == 'loop':
        if args.routine == 'e01':
            loop.exerc_01()
        elif args.routine == 'e02':
            loop.exerc_02()
        elif args.routine == 'e03':
            loop.exerc_03()
        elif args.routine == 'e04':
            loop.exerc_04()
        elif args.routine == 'e05':
            loop.exerc_05()
        elif args.routine == 'e06':
            loop.exerc_06()
        elif args.routine == 'e07':
            loop.exerc_07()
        elif args.routine == 'e08':
            loop.exerc_08()
        elif args.routine == 'e09':
            loop.exerc_09()
        elif args.routine == 'e10':
            loop.exerc_10()
        else:
            sys.exit(f"[LOOP] Failed execution. Routine don't recognized! {args.routine=}")
    elif args.training == 'regex':
        if args.routine == 'e01':
            regex.exerc_01()
        elif args.routine == 'e02':
            regex.exerc_02()
        elif args.routine == 'e03':
            regex.exerc_03()
        elif args.routine == 'e04':
            regex.exerc_04()
        elif args.routine == 'e05':
            regex.exerc_05()
        elif args.routine == 'e06':
            regex.exerc_06()
        elif args.routine == 'e07':
            regex.exerc_07()
        elif args.routine == 'e08':
            regex.exerc_08()
        elif args.routine == 'e09':
            regex.exerc_09()
        elif args.routine == 'e10':
            regex.exerc_10()
        else:
            sys.exit(f"[REGEX] Failed execution. Routine don't recognized! {args.routine=}")

    sys.exit(0)
