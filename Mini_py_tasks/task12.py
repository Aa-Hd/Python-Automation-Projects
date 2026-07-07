#Write a Python program to sort three integers without using conditional statements and loops.

intg1=20                                              #task 12(without using loops)
intg2=10
intg3=25
mylist=[intg1,intg2,intg3]
mylist.sort()
print(mylist)


intg1=20                                                     #task 12(using loops)
intg2=10
intg3=25
mylist=[intg1,intg2,intg3]
mysortedlist=[]
mysortedlist=mysortedlist+[min(mylist)]
for x in mylist:
    if x==min(mylist):
        pass
    elif x==max(mylist):
        pass
    else:
        mysortedlist=mysortedlist+[x]
    

mysortedlist=mysortedlist+[max(mylist)]
print(mysortedlist)