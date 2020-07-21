# This program is to use set() function that didn't allow to input a duplicate variables
# this program also is used to find the number of duplicate variables in the list

# add to a set and print the final list
a_set = set()
a_set.add("Nourhan Adel")
a_set.add("Esraa saad")
a_set.add("Mirna Maher")
a_set.add("Nourhan Adel")
print(a_set)

print("\n ********************************* \n")


# Duplicate function
def retutn_duplicate(list):
    duplicates = []
    b_set = set()
    for item in list:
        length_one = len(b_set)
        b_set.add(item)
        length_two = len(b_set)
        if length_one == length_two:
            duplicates.append(item)
    return duplicates


list = ["Mirna Maher", "Nourhan Adel", "Esraa saad", "Mohamed Adel", "Nourhan Adel", "Mirna Maher"]
dups = retutn_duplicate(list)
print("The duplicate list is {} whose lenght {} ".format(dups, len(dups)))
