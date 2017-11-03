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


def display_modify_todo(type_of_change=None):
    clear_screen()
    change_description = 'description'
    change_description_information = 'Now you can enter new description to this task, it must me be less than 150chars: '
    change_name = 'name'
    change_name_information = 'Now you can enter new name for this task, it must be less than 20 chars: '
    change_information = 'Enter "name" or "description" to change it: '

    if type_of_change == change_description:
        print(change_description_information)

    elif type_of_change == change_name:
        print(change_name_information)

    else:
        print(change_information)


def display_tasks_name(todo_list):
    pass


def display_all_tasks_details(todo_list):
    clear_screen()
    back_information = '\nEnter to back to main menu:'
    print(todo_list, back_information)


def display_get_index_of_task(todo_list, operation):
    clear_screen()
    task_to_mark = '\nEnter number for task you want ' + operation + ': '
    print(todo_list, task_to_mark)


def display_error():
    error_information = 'There is no task with index you entered!'
    print(error_information)
