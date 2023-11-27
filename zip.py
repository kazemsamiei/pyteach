# zip

mylist1 = ['hamid', 'ali', 'ahmad']
mylist2 = ['reza', 'akbar']

ziplist = zip(mylist1, mylist2)
print(type(ziplist))

for x in ziplist:
    print(type(x))
    