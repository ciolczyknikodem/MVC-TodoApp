class ToDo:

    def __init__(self, _id, name, description):

        self.id = _id
        self.name = name
        self.description = description
        self. is_done = False

    def set_to_done(self):
        self.is_done = True

    def __str__(self):
        if self.is_done:
            infromation_todo = '[X]' + self.id + ': ' + self.name + '\n' + self.description
            return infromation_todo

        else:
            infromation_todo = '[X]' + self.id + ': ' + self.name + '\n' + self.description
            return infromation_todo
