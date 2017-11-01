import os


def display_menu_options():
    """
        Argument: none
        Return: none

        Function display main menu options
    """

    welcome_infromation = 'Welcome in ToDo aplication!\n'
    exit_program = '0. Exit'
    control_information = '\n\nMy program using key getch in menu, you dont need to confirm your chose by enter. Enjoy!'

    options = ['Add task to list todo', 'Modify name or description of task', 'Remove task from todo list',
               'Mark task to done/undone', 'Display tasks', 'Display tasks with details']

    print(welcome_infromation)
    index = 0
    for element in options:
        index += 1
        index = str(index)

        print(index + '. ' + element)
        index = int(index)

    print(exit_program, control_information)


def display_add_task(name, description):
    os.system('clear')
    print('Adding task to your Todo List:')
    
