import random


def generate_id_for_task():
    symbols = ['@', '#', '%', '!', '*', '&', '^']
    _id = ''

    for unique_element in range(4):
        numbers = random.randint(0, 9)
        _id += random.choice(symbols)
        _id += str(numbers)

    _id = ''.join(random.sample(_id, len(_id)))
    return _id


# asd = generate_id_for_task()
# print(asd)


def check_if_id_already_exist(new_id, todo_list):
    print(todo_list)
    if todo_list:
        for _id in todo_list:
            if _id.id == new_id:
                return True

            else:
                return False
