import view
from model import ToDo
from generate_id import generate_id_for_task


def back_to_menu():
    input()


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


def get_task_index():
    change_input_index_by_1 = 1
    correct_input = True
    while correct_input is True:
        index_of_task = input()
        if index_of_task.isdigit():
            index_of_task = int(index_of_task)
            index_of_task -= change_input_index_by_1
            correct_input = False

    return index_of_task


def mark_task(todo_list):
    view.display_all_tasks_details(todo_list)
    index_of_task = get_task_index()
    is_error = todo_list.mark_task(index_of_task)
    if is_error:
        view.display_error()
        back_to_menu()


def remove_task_from_list(todo_list):
    view.display_all_tasks_details(todo_list)
    index_of_task = get_task_index()
    is_error = todo_list.remove_task_from_list(index_of_task)
    if is_error:
        view.display_error()
        back_to_menu()


def change_description_of_task(todo_list):
    pass


def ask_for_display_tasks(type_of_operation, todo_list):
    display_tasks_name = '5'
    display_all_tasks_details = '6'

    if type_of_operation == display_tasks_name:
        view.display_tasks_name(todo_list)
        back_to_menu()

    elif type_of_operation == display_all_tasks_details:
        view.display_all_tasks_details(todo_list)
        back_to_menu()
