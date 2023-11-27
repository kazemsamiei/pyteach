# class MyClass:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myObj = MyClass()
# myIter = myObj.__iter__() # iter(myObj)

# print(myIter.__next__()) # next(myIter)
# print(myIter.__next__())
# print(myIter.__next__())


class MyClass:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
            

myObj = MyClass()
myIter = myObj.__iter__() # iter(myObj)

# print(myIter.__next__()) # next(myIter)
# for x in myIter:
#     print(x)
print(hasattr(myIter,'__path__'))