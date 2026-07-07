#Write a Python program to compute the greatest common divisor (GCD) of two positive integers

integer1=int(input())                                           #task9
integer2=int(input())
print(integer1,'and',integer2)
if integer1<integer2:
    smallest=integer1
smallest
for i in range(1,smallest+1):
    if integer1%i==0 and integer2%i==0:
        gcd=i
print(gcd)