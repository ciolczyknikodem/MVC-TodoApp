import view
from model import ToDo
from generate_id import generate_id_for_task


def add_task_to_list(todo_list):
    name_of_new_task = ''
    description_of_task = ''
    unique_id = True
    min_len_of_task = 0
    max_len_of_name = 20
    max_len_of_description = 150

    while unique_id is True:
        new_id = generate_id_for_task()
        unique_id = todo_list.check_if_id_already_exist(new_id)

    while not len(name_of_new_task) > min_len_of_task and len(name_of_new_task) < max_len_of_name:
        view.display_add_task_name()
        name_of_new_task = input()

    while not len(description_of_task) > min_len_of_task and len(name_of_new_task) < max_len_of_description:
        view.display_add_task_description()
        description_of_task = input()

    new_task = ToDo(new_id, name_of_new_task, description_of_task)
    todo_list.add_task_to_list(new_task)


def modify_task(todo_list):
    pass


def ask_for_display_tasks(todo_list):
    view.display_all_tasks_details(todo_list)
    exit_to_menu = input()
