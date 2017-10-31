import view
import model
import os
import key_getch
import sys


def main():
    os.system('clear')

    while True:
        view.display_menu_options()

        type_of_operation = key_getch.getch()

        if type_of_operation == '1':
            print('Working')

        elif type_of_operation == '0':
            sys.exit()


if __name__ == '__main__':
    main()
