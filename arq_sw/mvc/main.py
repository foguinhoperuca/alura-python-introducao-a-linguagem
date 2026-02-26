import argparse
import sys
from typing import Optional

import controller
from view import View, ViewCli, ViewTk


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MVC python...")
    parser.add_argument('--view', choices=["cli", "tk"], help='View availiable: [cli | tk]')
    args = parser.parse_args()

    view: Optional[View] = None
    if args.view == 'cli':
        view = ViewCli()
    elif args.view == 'tk':
        view = ViewTk()
    else:
        sys.exit(f'Invalid view: {args.view}!')

    controller.set_view(view)
    view.update()
    view.mainloop()

    sys.exit(0)
