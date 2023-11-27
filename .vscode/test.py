class MyClass:
    name = 'ali'
    def __init__(self, family):
        # self.name = name
        # print(self.name)
        self.family = family

    def newfunc(self):
        print(self.family)

p = MyClass('ahmadi')
p.newfunc()
# print(p.name)
# p.newfunc('alavi')