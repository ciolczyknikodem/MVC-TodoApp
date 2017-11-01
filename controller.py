import view
from model import ToDo
from generate_id import generate_id_for_task, check_if_id_already_exist


def add_task_to_list(todo_list):
    name_of_new_task = ''
    description_of_task = ''
    unique_id = True

    # while unique_id is True:
    new_id = generate_id_for_task()
        # unique_id = check_if_id_already_exist(new_id, todo_list)
    # print(new_id)

    while not len(name_of_new_task) > 0 and len(name_of_new_task) < 20:
        view.display_add_task_name()
        name_of_new_task = input()

    while not len(description_of_task) > 0 and len(name_of_new_task) < 150:
        view.display_add_task_description()
        description_of_task = input()

    new_task = ToDo(new_id, name_of_new_task, description_of_task)
    todo_list.add_task_to_list(new_task)


def ask_for_display_tasks(todo_list):
    view.display_all_tasks(todo_list)
