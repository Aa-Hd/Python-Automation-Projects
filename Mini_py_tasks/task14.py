#Write a Python program to find all common divisors between two numbers in a given pair


first_number = int(input("Enter first number: "))                        #task 14
second_number= int(input("Enter second number: "))
pair=[first_number,second_number]
if first_number< second_number: 
   limit = first_number 
else:
   second_number

print("Common divisors are:")

for i in range(1, limit + 1):
    if first_number % i == 0 and second_number % i == 0:
        print(i,',',end='')