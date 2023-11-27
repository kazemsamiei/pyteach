# filter

ages = [10, 12, 42, 44, 11, 35, 66, 46, 89]

def myfunc(x):
    if x > 20:
        return True
    else:
        return False

adultAge = filter(myfunc, ages)

for x in adultAge: print(x, end=" ")