import argparse
import curses

from models import connector

def main(stdscr) -> None:
    args:argparse.Namespace = get_argparse()
    hostname:str = args.hostname

    stdscr.clear()

    if not hostname:
        stdscr.addstr(0, 0, "-H/--hostname flag is currently required.")
        stdscr.addstr(1, 0, "Press ENTER to quit.")
        stdscr.refresh()
    else:
        stdscr.addstr(0, 0, f"TEST: {hostname}", curses.A_BOLD)
        stdscr.refresh()

    stdscr.getch()


def get_argparse() -> argparse.Namespace:
    """Grabs the command-line arguments specified when the program was invoked.

    :returns: The arguments given when starting the program.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--hostname",
                        help="The host or target name.",
                        default=None)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_argparse()
    curses.wrapper(main)
