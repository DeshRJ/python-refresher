#fun args
from unicodedata import name


def multi(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

multi(1,3,5)

def add(x, y):
    return x + y

nums = [22, 45]
add(*nums)           #* used to unpack list

nums1 = {'x' :22, 'y': 45}  #** used to unpack dict.
add(**nums1)

#keyword args

def named(**kwargs):
    print(kwargs)

named(name = 'a', age= '25')

detail = {'name':'a', 'age': '25'}
named(**detail)

