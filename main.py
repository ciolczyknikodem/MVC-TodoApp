import view
import model
import controller
import key_getch
import sys


def main():
    todo_list = model.ToDoList()

    while True:
        view.display_menu_options()
        type_of_operation = key_getch.getch()

        if type_of_operation == '1':
            controller.add_task_to_list(todo_list)

        elif type_of_operation == '2':
            pass

        elif type_of_operation == '3':
            pass

        elif type_of_operation == '4':
            pass

        elif type_of_operation == '5':
            controller.ask_for_display_tasks(todo_list)

        elif type_of_operation == '0':
            sys.exit()


if __name__ == '__main__':
    main()
