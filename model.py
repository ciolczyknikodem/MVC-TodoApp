class ToDo:

    def __init__(self, _id, name, description):
        """
        Argument: str, str, str
        Return: none

        Create instance of ToDo class
        """

        self.id = _id
        self.name = name
        self.description = description
        self. is_done = False

    def set_to_done(self):
        """
        Argument: instance of ToDo class
        Return: none

        Method change is_done variable to True or False
        """
        self.is_done = True

    def __str__(self):
        """
        Argument: instance of ToDo class
        Return: str
        """

        if self.is_done:
            infromation_todo = '[X]' + self.id + ': ' + self.name + '\n' + self.description
            return infromation_todo

        else:
            infromation_todo = '[X]' + self.id + ': ' + self.name + '\n' + self.description
            return infromation_todo


class ToDoList:

    def __init__(self):
        """
        Argument: instance of ToDoList class
        Return: none
        """
        self.todo_list = []

    def add_task_to_list(self, task):
        """
        Argument: instance of ToDoList class, instance of ToDo class
        Return: none
        """
        self.todo_list.append(task)

    def remove_task_from_list(self, task_id):
        """
        Argument: instance of ToDoList, str
        Return: none
        """
        self.todo_list.remove(task_id)
