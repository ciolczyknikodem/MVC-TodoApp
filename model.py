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
