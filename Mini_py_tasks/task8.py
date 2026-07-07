#Write a Python program which accepts a sequence of comma-separated numbers from user 
# and generate Bar Graph using '*' with those numbers

sequence_of_numbers=()                                          #task8         
for i in range(1,5):
    x=int(input('enter your number:'))
    sequence_of_numbers=sequence_of_numbers+(x,)
print(sequence_of_numbers)

for i in sequence_of_numbers:
    n = int(i)
    for j in range(n):
        print("*", end="")
    print()