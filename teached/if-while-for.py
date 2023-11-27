# if 
from math import pi
from operator import ne
import py_compile
from traceback import print_tb


a = 200
b = 300
c = 400

# if a<b:
#     print('a is smaller than b.')
# elif a>b:
#     print('a is greater than b.')
# else:
#     print('a is equal to b')

# if a<b : print('a<b')

# print('a<b') if a<b else print('a is not smaller than b ')

# if a < b or b < c:
    # print('both condition is true')
# if a!= b: print('a not equal to b')

# if not a>b:
#     print('a<b')

# if a<b:
#     if b<c:
#         print('a<b<c')

# while
# i = 0
# while i<6:
#     print(i)
#     # i+=1

# i = 0
# while i< 15:
#     i += 1
#     if i==10:
#         continue
#     print(i)    

# for
mylist = ['ali', 'hassan', 'mohammad', 'hossein']
# for x in mylist:
#     print(mylist.index(x))

# y = 'mohammad'
# for x in y:
#     print (x)

# for x in mylist:
#     if x == 'hassan':
#         continue
#     print (x)

# y =[]
# for x  in range(2, 100, 5):
#      y.append(x)

# print(y)

# y = list(range(2,100, 5))
# print(y)

# y = list(['blue','yello','red'])
# print(y)

mydict = {
    'student1':{
        'name': 'ali',
        'family':'alavi',
        'score': 20
    },
    'student2':{
        'name': 'ali2',
        'family':'alavi2',
        'score': 18
    },'student3':{
        'name': 'ali3',
        'family':'alavi3',
        'score': 19
    },
}
# print(mydict.items())
# i = 0
# for x, y in mydict.items():
#     newdict = mydict[x]
#     newlist = list(newdict)
#     # print(list(newdict.items())[i][0] ,' = ' , list(newdict.items())[i][1])
#     # print(newdict.items())
#     print( list(newdict.keys())[1], list(newdict.values())[1])
#     i+=1
    # print(newlist.index(x))

# print(len(mydict))

for x in mydict.items():
    print('*********************')
    print(*list(x[1:])[0].items(), sep='\n')