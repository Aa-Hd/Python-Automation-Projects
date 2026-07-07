#Write a Python program that accepts six numbers as input and sorts them in descending order
#given input : 15 30 25 14 35 40

list_of_six=[]                                                           #task 16
for i in range(6):
    x=int(input())
    list_of_six=list_of_six+[x]
print(list_of_six)
list_of_six.sort(reverse=True)
print('Sorted list in descending order is:',list_of_six)