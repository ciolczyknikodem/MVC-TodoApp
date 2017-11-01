import view
import model
import controller
import os
import key_getch
import sys


def main():

    while True:
        view.display_menu_options()

        type_of_operation = key_getch.getch()

        if type_of_operation == '1':
            controller.add_task_to_list()

        elif type_of_operation == '0':
            sys.exit()


if __name__ == '__main__':
    main()
