"""
n = 10
while n>0:
    print(n)
    n -=1

from reportlab.pdfbase.pdfutils import preProcessImages

friends = ['hamid',"rezam",'reza']
count = 0
for thisone in  friends:
    print(thisone)
    count = count + 1
print(count)
"""


def input_num(prompt):
    Nummer = []

    while True:
        try:
            Value = float(input(prompt))
            if Value == -1:
                break
            else:
                Nummer.append(Value)
        except ValueError:
            print("Wrong Value")
    return Nummer

import statistics
import numpy
List = input_num("Input dein nummer: ")

print(List)

value =0
for a in List:
    value += a
avg = value / len(List)


avg1 = numpy.average(List)

avg2 = statistics.mean(List)


print(f"The mid of list is: {avg}")
print(f"The mid1 of list is: {avg1}")
print(f"The mid2 of list is: {avg2}")


