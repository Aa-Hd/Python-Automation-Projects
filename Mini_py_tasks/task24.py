#Create nested list , Create score list , Sort score list make sure it has each element only one ( with using list(set())) ,
# Sort score list and find second lowest grade , Find this score in nested list and sort for the names again
#input : Nested list = [  ["Ali",50],["Sara",40],["John",50],["Emma",30],["Tom",40]  ]

students_and_grades=[["Alice", 85],["Bob", 90],["John", 78],["Emma", 88],["Sam", 75]]       #task 24

print("Nested List:",students_and_grades,'\n')

scores = []

for i in students_and_grades:
    scores.append(i[1])

print("Score List :",scores,'\n')
scores.sort()
unique_scores=[set(scores)]
print("Sorted Score List with Unique Elements:",unique_scores,'\n')
second_lowest = scores[1]

names = []

for i in students_and_grades:
    if i[1] == second_lowest:
        names.append(i[0])

names.sort()

print("second lowest grade:",second_lowest,'\n')
print("Second lowest student", names)