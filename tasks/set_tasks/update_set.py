"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая обновит множество значениями из другого множества
"""


def update_set(set_1: set, set_2: set) -> set:
    # TODO вставить код сюда
    return set_1


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    update_set(some_set, {3, 4, 5})
    assert some_set == {1, 2, 3, 4, 5}
    print('Решено!')