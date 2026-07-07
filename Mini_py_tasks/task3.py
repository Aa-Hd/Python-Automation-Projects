#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input("please enter your first name:")       
last_name = input("please enter your last name:")

list=[first_name,'',last_name]
print(list[::-1])