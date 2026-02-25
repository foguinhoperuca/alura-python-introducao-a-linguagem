import argparse
import sys

from conditional import exerc_01, exerc_02, exerc_03, exerc_04, exerc_05, exerc_06, exerc_07, exerc_08, exerc_09, exerc_10


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training python...")
    parser.add_argument("-t", "--training", action="store_true", help="")
    subparser = parser.add_subparsers(dest='training', help="Choose training", required=True)
    subparser.add_parser('conditional').add_argument('--routine', choices=["e01", "e02", "e03", "e04", "e05", "e06", "e07", "e08", "e09", "e10"], help='Choose exercises: e1 - e10')
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
            sys.exit(f"Failed execution. Routine don't recognized! {args.routine=}")

    sys.exit(0)
