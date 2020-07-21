""" I want to find if the two lists are intersected at a point or not and printing the intersection between them
if they are intersected--------> that's by making a function
OR to use a build-in function 'intersection' but it works on the set"""


def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3


list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 6, 7]
print(intersection(list1, list2))
print("\n ******************** \n")
# The build-in function
set1 = set(list1)
set2 = set(list2)
print(set1.intersection(set2))
