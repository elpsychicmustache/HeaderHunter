import curses

def main(stdscr) -> None:
    stdscr.clear()
    stdscr.addstr(0, 0, "Test 123", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
