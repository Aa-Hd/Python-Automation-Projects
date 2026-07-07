#Write a Python program to check if a string contains all letters of the alphabet

string_alphabet = input("Enter a sentence: ")                 #task 18
print("The given string is:",string_alphabet,'\n')

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0

for i in alphabet:
    if i in string_alphabet or i.upper() in string_alphabet:
        count += 1
        

if count == 26:
    print("The given string contains all letters of alphabets")
else:
    print("The given string doesnt contains all letters of alphabets")