#count the value exist in the dictionary
#input:  The original dictionary : {1: ['gfg', 'best', 'geeks'], 2: ['gfg', 'CS'], 3: ['best', 'for', 'CS'],
#                                   4: ['test', 'ide', 'success'], 5: ['gfg', 'is', 'best']}
#output:  Values Frequency : {'gfg': 3, 'best': 3, 'geeks': 1, 'CS': 2, 'for': 1, 'test': 1, 'ide': 1, 'success': 1, 'is': 1}



dictionary = {                                                                    #task23
    1: ['gfg', 'best', 'geeks'],
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




specific_value=input()                                     #another method
print(specific_value)                                      #counts for a specific value from d 
list=dictionary.values()                                   

count=0
for values in list:
    if specific_value  in values:
        count+=1
    else :
        pass
else:
    print("The given value doesnt exist")
print(f"The frequency of {specific_value} is : ",count)