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
            infromation_todo = '[X]. ' + 'ID: ' + self.id + ' : ' + 'Task name: ' + self.name + '\n' + 'Description: ' + self.description
            return infromation_todo

        else:
            infromation_todo = '[ ]. ' + 'ID: ' + self.id + ' : ' + 'Task name: ' + self.name + '\n' + 'Description: ' + self.description
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

    def check_if_id_already_exist(self, new_id):
        """
        Arguments: instance of ToDoList, str
        Return: Bool

        Method check if new_id already exist in list
        """
        for _id in self.todo_list:
            if _id.id == new_id:
                return True

            return False

    def mark_task(self, index):
        if self.todo_list[index].is_done is False:
            self.todo_list[index].is_done = True

    def __str__(self):
        list_string = ''
        index = 1

        for element in self.todo_list:
            index = str(index)
            list_string += index + '. ' + element.__str__() + '\n'
            index = int(index)

        return list_string
