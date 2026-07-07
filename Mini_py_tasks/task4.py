#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

list=[]                                                   #task4
tupple=()
for i in range(1,5):
    x=int(input('enter your number:'))
    list=list+[x]
    tupple=tupple+(x,)
print(list)
print(tupple)