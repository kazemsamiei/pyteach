# Dictionary features: ordered, changeable, Not allowed duplicate

myDict = {
    'student1':{
        'name':'ali',
        'family':'hashemi',
        'age': 18,
        'gender': 'male',
        'tel':['123456', '654321']
    },
    'student2':{
        'name':'hamid',
        'family':'hashemi',
        'age': 18,
        'gender': 'male',
        'tel':['123456', '654321']
    },
    'student3':{
        'name':'ali',
        'family':'hashemi',
        'age': 18,
        'gender': 'male',
        'tel':['123456', '654321']
    }
}
# print(myDict.keys())
# print(myDict.values())
# myDict['address'] = 'qom'
# myDict['age'] = 25
# print(myDict.items())
# myDict.pop('age')
# del myDict
# myDict.clear()
# for x, y in myDict.items():
#     print(x, "=", y)
# dict1 = myDict.copy()
# print(dict1)
print(myDict['student2']['name'])