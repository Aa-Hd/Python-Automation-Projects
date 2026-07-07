#Write a Python program to check if lowercase letters exist in a string.

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
