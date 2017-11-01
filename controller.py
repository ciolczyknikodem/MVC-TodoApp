import view
import model


def add_task_to_list():
    name_of_new_task = ''
    description_of_task = ''

    while not len(name_of_new_task) > 0 and len(name_of_new_task) < 20:
        view.display_add_task_name()
        name_of_new_task = input()

    while not len(description_of_task) > 0 and len(name_of_new_task) < 150:
        view.display_add_task_description()
        description_of_task = input()

    task = ToDo(_id, name_of_new_task, description_of_task)
