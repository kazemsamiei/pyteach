# Class

# class MyInfo:
#     name = 'ali'
#     family = 'alavi'
#     age = 20
#     def __init__(self, getName, getFamily, getAge):
#         # print('new object is created')
#         self.name = getName
#         self.family = getFamily
#         self.age = getAge

#     def running(self):
#         print(self.name, ' is running')

# user1 = MyInfo('majid', 'majidi', 37)
# print(user1.age)
# user1.running()
# user1 = MyInfo()
# print(user1.name, user1.family, user1.age)
# user2 = MyInfo('hossein', 'hassani', 20)
# print(user2.name, user2.family, user2.age)

# user1.running()
# user2.running()

class person:
    def __init__(self, getName, getFamily, getAge):
        self.name = getName
        self.family = getFamily
        self.age = getAge

    def printinfo(self):
        print(self.name, self.family, self.age)

class student(person):
    def __init__(self, getName, getFamily, getAge, 
                 getstuCode, getstuField, getstuTerm):
        super().__init__(getName, getFamily, getAge)
        self.stuCode = getstuCode
        self.stuField = getstuField
        self.stuTerm = getstuTerm
    
    def printinfo(self):
        print(f"your name is {self.name} {self.family} and you are {self.age} years old."
               f"\nyour Student Code is {self.stuCode} and your field is {self.stuField}."
                 f"\nyou are in {self.stuTerm}th term")

stu1 = student(getName='ali', getFamily='alavi', getAge=20, 
               getstuCode='123456', getstuField='Software Engineering', getstuTerm=3)
# stu1.printinfo()
random_byte_array = bytearray('ABC', 'utf-8')
# mem = memoryview(stu1)
# print(random_byte_array)
for x in random_byte_array:
    print(x)



