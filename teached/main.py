# List features: allow duplicate, ordered, changeable
myList = ['ali', 'hassan', 'ahmad', 'reza','ali']
myList1 = [200, 300, 45, 38, 1200]
myList2 = [True, False, False, True]
myList3 = ['ali', 200, True]
print(myList)
# print(myList[-3:])
# if 'ali' in myList:
#     print('yes')
# myList[1:2] = ['mahmood','hossein']
# myList.insert(2, 'mahmood')
# myList.append('mahmood')
# myList.extend(myList1)
# myList.remove('ali')
# myList.pop()
# myList.clear()
# for x in myList:
#     print('your first name is:' , x)
# [print(x) for x in myList]
# myList.sort(key = str.upper)
# list1 = [x.capitalize() for x in myList]
# for x in myList:
#     print(x.capitalize(), end=" ")
# list1 = myList.copy()
# list1 = list(myList)
# myList1 +=  myList2
newList = [x.upper() for x in myList if 'd' in x]
print(newList)