#Write a Python program to accept a filename from the user and print the extension of java

file_name=input('enter your filename:')                   #task5
print(file_name)
print(type(file_name))
if '.json' in file_name:
    print('json')
elif '.txt' in file_name:
    print('txt')
elif '.java' in file_name:
    print ('java')
elif '.csv' in file_name:
    print('csv')
else:
    print('file type doesnt exist')