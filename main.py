import view
import model
import controller
import key_getch
import sys


def main():
    todo_list = model.ToDoList()
    add_new_task = '1'
    modify_task = '2'
    remove_task_from_list = '3'
    mark_task = '4'
    display_tasks_name = '5'
    display_all_tasks_details = '6'
    exit_program = '0'

    while True:
        view.display_menu_options()
        type_of_operation = key_getch.getch()

        if type_of_operation == add_new_task:
            controller.add_task_to_list(todo_list)

        elif type_of_operation == modify_task:
            controller.modify_task(todo_list)

        elif type_of_operation == remove_task_from_list:
            controller.remove_task_from_list(todo_list)

        elif type_of_operation == mark_task:
            controller.mark_task(todo_list)

        elif type_of_operation == display_tasks_name or type_of_operation == display_all_tasks_details:
            controller.ask_for_display_tasks(type_of_operation, todo_list)

        elif type_of_operation == exit_program:
            sys.exit()


if __name__ == '__main__':
    main()
