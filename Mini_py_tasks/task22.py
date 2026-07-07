#Write a program sort_list_of_tuples(lst) that takes a list of tuples lst as input. Each tuple in the list contains two elements, the first being a string and the second being an integer. The program should sort the list based on the integer values in ascending order.
#input  : [("Alice", 25), ("Bob", 30), ("John", 18), ("Emma", 22)]

my_list=[]                                                         #task 22
tuples = ()
for i in range(4):
    name=input("enter name:")
    age=int(input('enter age:'))

    sublist = (name,age)
    
    #int(sublist[0])
    #tuple(sublist)
    tuples=(sublist)+(tuples)
    my_list.append(sublist)

print('List of tuples is : ',my_list,'\n')
my_list.sort(key=lambda x:x[1])
print('Sorted list of tuples :',my_list)