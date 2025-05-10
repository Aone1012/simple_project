# video 3_1
"""
print(type('salam'))

a= 'salam'
print(a[0])
print(a[4])
print(a[3])
print(len(a))
for i in range(0,len(a)):
    print(i,a[i])

b = 'salam kojaaeee'
for i in range(0,len(b)):
    print(b[i])

for letter in 'my string':
    print(letter)

string = 'this is a sample string in count as'
for harf in string:
    print(harf)
string = 'this is a sample string in count as'

count = 0
for letter in string:
    if letter =='a':
        count +=1
print(count)
string = 'Man daram miram'
print(string[:3])

print(string[3:])
print(string[3:8])
print(string[:-3])
print(string[:-2])
string = 'R' + string[1:]
print(string)
                                        # Video 3_2
print('a' in 'amir')
print('bia berim' >' adad aval')
                                        #Method class
print('amir'.upper())
print(dir('amir'))
print('AMIO'.lower())
print('amir mohammad'.find('a'))
print('amir mohammad'.find('a',2))
print('       amir mohammad              ')

print('       amir mohammad              '.strip())
print('amir mohammad'.startswith('a'))
print('amir mohammad'.startswith('m'))
print('       amir mohammad              '.strip())
print('Amir mohammad'.lower().startswith('a'))
name= 'Amir'
print('hello',name,3)
print('hello %s chetori? '% name)
sen = 40
print('hello %s chetori? midino %s salet shode? %i' % (name,sen,256)) # %s = string %i =integer
                                             List                   #Video 3_3
l = [4,5,-1, 1.2,'amir']
print(l[0])
print(l[-2])
print(l[-1])
l2 = [l,5,[1,2]]
(l2)

print(len(l2))

print(l2[0])

for i in range (0,len(l2)):
   print(l2[i])

print(l)
l[0] = 9
print(l)
for i in range(0,len(l)):
   print(i,l[i])
l = [4,5,-1, 1.2,'amir']

l2 = [l,5,[1,2]]

for item in l:
    print(item)

l1 = [1, 2]
l2 = ['amir', 'ali']
print(l1 + l2)
print(l1 * 4)
print(l2 * 4)
l1 = [2,26]
l1.append('new')
print(l1)
l1.extend([51,26,17,5,4,2,7,89])
print(l1)
del l1[2]
print(l1)
l1.sort()           #sort()
l1.append(22)       #append
l1.sort()
print(l1)
print(l1.pop())     #pop
print(l1)
l1.remove(2)        #remove
print(l1)
l1.remove(2)
print(l1)

my_list = ['a', 'b', 'amir']
print(len(my_list))
print(max(my_list))
print(min(my_list))

my_list1 = [ 23, 33,45,3,4,5,66,7]
print(sum(my_list1))                    #sum
print(sum(my_list1)/len(my_list))       #Average

string = ' amir mohammad motamedy '
List_od_words =string.split()           #split
print(List_od_words)
print('-'.join(List_od_words))
"""
"""
                            #Danger Zohn
def change(a) :
    a[0] = 100

b=[7,8,9,6,8]
change(b)

print(b)

"""
# video_4
# Dictionary
"""
f2t = dict()
f2t ['yek'] = 'bir'
f2t ['do'] = 'ikki'

print(f2t)
gad = {'amir': 173, 'hamid': 175, 'vahid': 175}
print(gad['amir'])
print(gad['vahid'])
print(len(gad))
print(gad.keys())
print(list(gad.keys()))
print(gad.values())
print(list(gad.values()))

print(173 in gad)# not Values
print('amir' in gad) #just keys will be checked ___ in ___is very fast
"""
string = "Haloo ich bin Amir und ich zwanzig jahre alt. ich bin computer-Ingeniur aber arbeite als lehrer. "

counter = dict()

for letter in string:
    counter[letter] = counter.get(letter, 0) + 1
for this_one in list(counter.keys()):
    print('%s appearred %s times' % (this_one, counter[this_one]))

"""
dict()
d={ -:- , -:- , -:- , -:- }
    1 2
    1 = Keys
    2 = values
Ghad = dict()
Ghad.values() will return the values
Ghad.keys() will return the keys
Ghad.get(_,_) 
         1 2
         1 =  will check the Ghad keys if exist return that else return None 
         2 =  will return what you want except None

"""
