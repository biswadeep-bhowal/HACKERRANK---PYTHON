students = []
min1, min2 = 101.00, 101.00

for _ in range(int(input())):
    
    name = input()
    score = float(input())
    
    if score<min1:
        min2=min1
        min1=score
    elif min2>score>min1:
        min2=score
        
    students.append([name, score])


# Iterating through a list containing only min2 scores, sorted by name.

for student in sorted(filter(lambda s: s[1]==min2, students), key=lambda s: s[0]):
    print(student[0])