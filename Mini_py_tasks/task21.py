#Write a pytho program to  concatenate_lists(lists) that takes a list of lists lists as 
#  and print a new list obtained by concatenating all the sublists.

lists = []                                                   #task 21

for i in range(3):
    sublist = input("Enter all elements of sublist separated by spaces: ").split()
    
    for j in range(len(sublist)):                                 # convert each element to integer
        sublist[j] = int(sublist[j])
    
    lists=lists+[sublist]
print('All lists are :',lists,'\n')

concatenated_list = []                                             # concatenate all sublists
for sublist in lists:
    for item in sublist:
        concatenated_list=concatenated_list+[item]

print("Concatenated list is : ", concatenated_list)