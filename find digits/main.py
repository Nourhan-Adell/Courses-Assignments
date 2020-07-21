""""" This program is used to find the digits in a string or the number of digits in the string
or finding the last digit in the string"""
input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string]  # this to write eah character separately in the list
print(new_list)
print()

new_list2 = [c for c in input_string if c.isdigit()]  # printing only the digits in the word
print(new_list2)
print()

new_list3 = [c for c in input_string if c.isdigit()][-1]  # To print only the last digit in the word
print(new_list3)
print()

new_list4 = [price * 3 for price in input_string]  # It will print each character 3 times, and word(price)it's like "i"
print(new_list4)

new_list5 = [word[0] for word in input_string]  # It's like the first output
print(new_list5)

"""List comprehension syntax:
variable =[expression(i) for i 'Iterates'
 in input-string || input-list 'processes'   
if filter(i) 'any condition']"""
