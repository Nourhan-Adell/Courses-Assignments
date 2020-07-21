# combine two lists as a tuple
names = ["Nourhan", "Moahmed", "Mirna", "Esraa", "Alaa", "Ahmed", "Moataz"]
number = [1, 5, 6, 8, 2, 3, 10]
number2 = [5, 2, 6, 9]
new_list = []
new_list2 = []
for i in zip(names, number):
    new_list.append(i)

for j in zip(names, number2):
    new_list2.append(j)

print(new_list)
print(new_list2)
# The combination will be = the number of the smallest list
