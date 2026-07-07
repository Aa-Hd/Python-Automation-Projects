#Write a Python program to find smallest and largest word in a given string

string = input("Enter your sentence: ")                                #task 17
print("The given string is:",string, '\n' )

words = set(string.split())                                 # convert words to set


max_len = 0
min_len = 0
max_word = ""
min_word = ""

for word in words:
    
    count = 0                                                # count characters manually
    for letter in word:
        count += 1

    print(word,":" "length =", count,'\n')

    if count > max_len:                                      # find maximum length word
        max_len = count
        max_word = word

    if min_len==0 or count < min_len:                         # find minimum length word
        min_len = count
        min_word = word

print("Maximum length word is : ", max_word," and its Length is ",  max_len,'\n')
print("Minimum length word is : ", min_word, "and its Length is ", min_len,'\n')