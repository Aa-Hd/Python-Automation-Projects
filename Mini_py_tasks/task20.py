#Write a program rotate_list(lst, k) that takes a list lst and an integer k as inputs.
#  The program should rotate the list to the right by k positions.
#  For example, if k = 2, the last two elements should move to the beginning of the list.
#input :   "my_list = [1, 2, 3, 4, 5]
#input :   rotation_count = 2"

rotation_count=int(input("Enter number of rotations as an integer"))     #task 20
my_list=[]

for i in range(5):
     x=int(input("Enter elements of list as integers"))
     my_list=my_list+[x]

print("my list before rotation is : ",my_list,'\n')

for j in range(rotation_count):                              #process for each rotation
     temp=my_list[j]                     
     my_list.insert(j+1,temp)                                #inserts at index 1,elemnt to be inserted is is 1
     
     my_list[j]=my_list[-1]                                  #updating 0 index
     
     my_list.pop()                                           #removing last duplicate element
                                                              

print(f"my list after {rotation_count}  rotations is : ",my_list)