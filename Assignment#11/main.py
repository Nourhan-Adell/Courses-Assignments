"""Given a non-empty list of integers, every element appears twice except for one. Find that single one."""


def duplicate(list):
    dups = []
    a_set = set()
    for item in list:
        lenght_one = len(a_set)
        a_set.add(item)
        lenght_two = len(a_set)
        if lenght_one == lenght_two:
            dups.append(item)

    new_list = [item for item in a_set if item not in dups]

    return new_list


list = [1, 1, 2, 2, 5, 6, 6, 3, 3, 9, 9, 7, 7, 5, 0]
print(duplicate(list))
