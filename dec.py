import string
from random import randint

s = []
for i in range(20):
    s.append(randint(-10, 10))
l = [c for c in s]
def f2(l):
    i=0
    while i < len(l):
        print(l[i])
        i+=1
def decorator(leng):
    def new_leng(*args,**keywargs):
        print('Running function: ', leng.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', keywargs)
        result = leng(*args, **keywargs)
        print('Result: ', result)
        return result
    return new_leng
f2_decorator = decorator(f2)
f2_decorator(l)
