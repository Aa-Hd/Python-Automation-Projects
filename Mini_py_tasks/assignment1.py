# Write a Python program which accepts the radius of a circle from the user and compute the area.

radius=int(input('Please input radis of a cricle:'))   #task 2

area_of_circle=3.14*(radius**2)

print('Area of circle is :',area_of_circle)


first_name = input("please enter your first name:")       #task3
last_name = input("please enter your last name:")

list=[first_name,'',last_name]
print(list[::-1])


list=[]                                                   #task4
tupple=()
for i in range(1,5):
    x=int(input('enter your number:'))
    list=list+[x]
    tupple=tupple+(x,)
print(list)
print(tupple)

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


number = int(input("Enter a number (1-10000): "))        #task 6

ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

if number == 10000:
    print("ten thousand")

else:
    if number >= 1000:
        print(ones[number//1000], "thousand", end=" ")
        number = number % 1000

    if number >= 100:
        print(ones[number//100], "hundred", end=" ")
        number = number % 100

    if number >= 20:
        print(tens[number//10], end=" ")
        number = number % 10

    elif number >= 10:
        print(teens[number-10], end=" ")
        number = 0

    if number > 0:
        print(ones[number], end="")


length=int(input('please input legnth of rectangle:'))         #task7
print('the legth of rectangle is:',length)
width=int(input('please input width of rectangle:'))
print('the width of rectangle is:',width)
for i in range(length):
    print('*'*width)


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


string_1=input()                                      #task 11
string_2=input()
print(string_1,end='')
print(string_2)


intg1=20                                              #task 12(without using loops)
intg2=10
intg3=25
mylist=[intg1,intg2,intg3]
mylist.sort()
print(mylist)


intg1=20                                                     #task 12(using loops)
intg2=10
intg3=25
mylist=[intg1,intg2,intg3]
mysortedlist=[]
mysortedlist=mysortedlist+[min(mylist)]
for x in mylist:
    if x==min(mylist):
        pass
    elif x==max(mylist):
        pass
    else:
        mysortedlist=mysortedlist+[x]
    

mysortedlist=mysortedlist+[max(mylist)]
print(mysortedlist)


lowercaseletters=set("abcdefghijklmnopqrstuvwxyz")                   #task 13
sentence=input()
print(sentence)

allsmallletters=[]
allotherthings=[]

for x in sentence:
    if x in lowercaseletters:                                          #small=x in lowercaseletters
       allsmallletters=allsmallletters+[x]
    else:                                                               #for x not in sentence:   
       allotherthings=allotherthings+[x]

print('Existing small letters in sentence:',allsmallletters)
print('Non small letters:',allotherthings)

if allsmallletters!=[]:  print("Small letters exist")
if allsmallletters==[]:  print("Small letters doesnt exist")



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


list_of_six=[]                                                           #task 16
for i in range(6):
    x=int(input())
    list_of_six=list_of_six+[x]
print(list_of_six)
list_of_six.sort(reverse=True)
print('Sorted list in descending order is:',list_of_six)


string = input("Enter your sentence: ")                                #task 17
print("The given string is:",string, '\n' )

words = set(string.split())                                 # convert words to set
print("All words in the string are : ",words,'\n')

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

    if min_len==0 or count < min_len:                   # find minimum length word
        min_len = count
        min_word = word

print("Maximum length word is : ", max_word," and its Length is ",  max_len,'\n')
print("Minimum length word is : ", min_word, "and its Length is ", min_len,'\n')


string_alphabet = input("Enter a sentence: ")                 #task 18
print("The given string is:",string_alphabet,'\n')

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0

for i in alphabet:
    if i in string_alphabet or i.upper() in string_alphabet:
        count += 1
        

if count == 26:
    print("The given string contains all alphabets")
else:
    print("The given string doesnt contains all alphabets")


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

print("Sorted words are : ",words,"\n")
new_string=''

for w in words:
    new_string=new_string+' '+w
print('Sorted string is : ',new_string,"\n")



rotation_count=int(input("Enter number of rotations as an integer"))     #task 20
my_list=[]
for i in range(5):
     x=int(input("Enter elements of list as integers"))
     my_list=my_list+[x]

print("my list before rotation is : ",my_list,'\n')

for j in range(rotation_count):                              #process for each rotation
     temp=my_list[j]                     
     my_list.insert(j+1,temp)                                #inserts at index 1,elemnt to be inserted is is 1
     
     my_list[j]=my_list[-1]                                  #updating 0 index
     
     my_list.pop()                                           #removing last duplicate element
     print(f"my list after {j+1}  rotation is : ", my_list  ,'\n' )

print(f"my final list after total  rotations is : ",my_list)


lists = []                                                   #task 21

for i in range(3):
    sublist = input("Enter all elements of sublist separated by spaces: ").split()
    
    for j in range(len(sublist)):                                 # convert each element to integer
        sublist[j] = int(sublist[j])
    
    lists=lists+[sublist]
print('All lists are :',lists,'\n')

concatenated_list = []                                             # concatenate all sublists
for sublist in lists:
    for item in sublist:
        concatenated_list=concatenated_list+[item]

print("Concatenated list is : ", concatenated_list)


my_list=[]                                                         #task 22
tuples = ()
for i in range(4):
    name=input("enter name:")
    age=int(input('enter age:'))

    sublist = (name,age)
    
    #int(sublist[0])
    #tuple(sublist)
    tuples=(sublist)+(tuples)
    my_list.append(sublist)

print('List of tuples is : ',my_list,'\n')
my_list.sort(key=lambda x:x[1])
print('Sorted list of tuples :',my_list)



dictionary = {                                                                    #task23
    1: ['gfg', 'best', 'geeks'],                                                  #counts for all values
    2: ['gfg', 'CS'],
    3: ['best', 'for', 'CS'],
    4: ['test', 'ide', 'success'],
    5: ['gfg', 'is', 'best']
    }

frequency = {}

for values in dictionary.values():
    for word in values:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print("Values Frequency :", frequency)

specific_value=input()                                 #task 23 another method
print(specific_value)                                  #counts for a specific value
list=d.values()
print(list)
count=0
for x in list:
    if specific_value  in x:
        count+=1

print(count)


students_and_grades=[["Alice", 85],["Bob", 90],["John", 78],["Emma", 88],["Sam", 75]]       #task 24

print("Nested List:",students_and_grades)
#students_and_grades = [  ["Ali",50],["Sara",40],["John",50],["Emma",30],["Tom",40]  ]

scores = []

for i in students_and_grades:
    scores.append(i[1])

print("Score List :",scores)
scores.sort()
unique_scores=set(scores)
print("Sorted Score List with Unique Elements:",list(unique_scores))
second_lowest = scores[1]

names = []

for i in students_and_grades:
    if i[1] == second_lowest:
        names.append(i[0])

names.sort()

print("second lowest grade:",second_lowest)
print("Second lowest students:", names)