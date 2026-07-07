#Write a python programe which takes two integers 'length' and 'width' and prints rectangle using *

length=int(input('please input legnth of rectangle:'))         #task7
print('the legth of rectangle is:',length)
width=int(input('please input width of rectangle:'))
print('the width of rectangle is:',width)
for i in range(length):
    print('*'*width)