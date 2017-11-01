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

    def change_name_of_task(self, new_task_name):
        """
        Argument: instance of ToDo class, str --> user input
        Return: none

        Method change name of instance task
        """
        self.name = new_task_name

    def change_description_of_task(self, new_task_description):
        """
        Argument: instance of ToDo class, str --> user input
        Return: none

        Method change description of instance task
        """
        self.description = new_task_description

    def __str__(self):
        """
        Argument: instance of ToDo class
        Return: str
        """

        if self.is_done:
            infromation_todo = '[X]. ' + self.id + ' : ' + self.name + '\n' + 'Description: ' + self.description
            return infromation_todo

        else:
            infromation_todo = '[ ]. ' + self.id + ' : ' + self.name + '\n' + 'Description: ' + self.description
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

    def __str__(self):
        list_string = ''

        for element in self.todo_list:
            list_string += element.__str__() + '\n'

        return list_string
