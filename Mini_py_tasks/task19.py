#Write a Python program to sort all words of a given string
#input : this is a test string

string = input("Enter a sentence with all small alphabets: ")       #task 19
print("The given string is : ",string,"\n")
words = []
word = ""

                                                 
for element in string:                                           # extract words manually
    if element!= " ":
        word = word + element
    else:
        words = words + [word]
        word = ""

                                              
words = words + [word]                                         # add last word

n = 0                                                         #count number of words manually
for w in words:
    n += 1

for i in range(n):                                            # manual sorting
    for j in range(i+1, n):
        if words[i] > words[j]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
                                                              
new_string=''

for w in words:
    new_string=new_string+' '+w
print('Sorted string is : ',new_string,"\n")                    ##print("Sorted words are : ",words,"\n")