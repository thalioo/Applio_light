import curses

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.addstr("Press 'q' to quit.\n")

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(main)