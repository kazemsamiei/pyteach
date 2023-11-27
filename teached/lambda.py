# returned value = lambda arguments : expression
# x = lambda a : a**2
# x = lambda a, b : a*b
# x = lambda a, b, c : a + b + c

def myfunc(n):
    return lambda a : a * n 
x = myfunc(2)
print(x(4))

