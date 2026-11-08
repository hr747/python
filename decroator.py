import math
def timer(func):
    def inner(*args,**kwargs):
        print('time stat')
        # print(fun)
        func(*args,**kwargs)

        print ('time end')

        return inner
@timer
def get_faction(n):
    print('factrial starting')
    result=math.factorial(n)
    print(f'f of {n}is:{result}')

get_faction(n=5)
# vajal decroted

# timer (get_faction)()