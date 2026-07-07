#Write a Python program to get the least common multiple (LCM) of two positive integers.

integer1=int(input())                                           #task 10
integer2=int(input())
print('the given integers are:',integer1,'and',integer2)
if integer1<integer2:
    smallest=integer1
smallest
for i in range(1,smallest+1):
    if integer1%i==0 and integer2%i==0:
        gcd=i
print('GCD:', gcd)

lcm = (integer1 * integer2) // gcd

print('LCM:', lcm)