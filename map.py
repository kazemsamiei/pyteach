# map
from cgi import print_arguments
from unicodedata import name


mylist = ['hamdi', 'ahmad', 'mahmood']

def myfunc(a):
    return len(a)

nameLenght = map(myfunc, mylist)

[print(x) for x in nameLenght]