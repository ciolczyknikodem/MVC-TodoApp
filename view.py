import os
import time


def clear_screen():
    os.system('clear')


def display_menu_options():
    """
        Argument: none
        Return: none

        Function display main menu options
    """
    clear_screen()
    welcome_infromation = 'Welcome in ToDo aplication!\n'
    exit_program = '0. Exit'
    control_information = '\n\nMy program using key getch in menu, you dont need to confirm your chose by enter. Enjoy!'

    options = ['Add task to list todo', 'Modify name or description of task', 'Remove task from todo list',
               'Mark task to done/undone', 'Display tasks', 'Display specific todo task\'s details']

    print(welcome_infromation)
    index = 0
    for element in options:
        index += 1
        index = str(index)

        print(index + '. ' + element)
        index = int(index)

    print(exit_program, control_information)


def display_add_task_name():
    clear_screen()
    print('Adding task to your Todo List:\n\nEnter name of your task: ')


def display_add_task_description():
        print('\nName of task has been added!\nEnter description of task: ')


def display_tasks_name():
    pass


def display_all_tasks_details(todo_list):
    clear_screen()
    print(todo_list)
    print('\nEnter to back to main menu:')
