"""
f = open('D:/Python/Exec/Fisrt_project/scores.txt')
counter = sum = 0
for line in f:
    counter += 1
    this_number = float(line.strip())
    print('line number %i is: %s' % (counter, this_number))
    sum += this_number

print('The Sum is: %s \nThe Average is: %s ' % (sum, sum / counter))
"""
"""
f = open('D:/Python/Exec/Fisrt_project/scores.txt')
lines = f.readlines()
for line in lines:
    print(line.strip())
"""
"""
f = open('D:/Python/Exec/Fisrt_project/average.txt', 'w')
average = sum / counter
f.write(str(average))
f.close()
"""
# """
import csv
from statistics import mean

with open('grade.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        name = row[0]
        these_grades = list()
        for grade in row[1:]: #because the first on is tne name
            these_grades.append(int(grade))
           # print(name, grade, these_grades)
        print('average of %6s is %5.2f' % (name,mean(these_grades)))
# """
