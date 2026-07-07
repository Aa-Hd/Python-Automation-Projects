#Write a Python program to count the number of carry operations for each of a set of addition problems.

integer_1 = int(input("Enter first number: "))                              #task 15
integer_2= int(input("Enter second number: "))

sum=integer_1+integer_2
carry = 0
count = 0

while integer_1 > 0 or integer_2 > 0:
    digit1 = integer_1 % 10
    digit2 = integer_2% 10

    if digit1 + digit2 + carry >= 10:
        carry = 1
        count += 1
    else:
        carry = 0

    integer_1= integer_1// 10
    integer_2 = integer_2// 10
print('sum of given numbers is:',sum)
print("Number of carry operations:", count)