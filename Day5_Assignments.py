1.Make a generator to perform the same functionality of the iterator

def GeneratorDemo(num):
    for x in num:
        yield(x*2)
SqrValue= GeneratorDemo([1,2,3,4,5])
print(SqrValue)
print(next(SqrValue))
print(next(SqrValue))
print(next(SqrValue))
print(next(SqrValue))
print(next(SqrValue))
	 
2.Try overwriting some default dunder methods and manipulate their default behavior

class Person:
    def __init__(self, name,age,city):
        self.name = name
        self.city = city
        self.age = age
    def __str__(self):
        return "Aao kabhi haveli pe !! Dear: {} , Age: {} from {}".format(self.name, self.age,self.city)
person = Person('Ragnor', 30,"Scandinavia" )
print(person)

3.Write a decorator that times a function call using timeit
start a timer before func call
end the timer after func call
print the time diff

from functools import wraps
import time


def DecoratorDemo(func):
    @wraps(func)
    def timeitwrapper(*args, **kwargs):
        starttime = time.perf_counter()
        print(f"Start time {starttime}")
        func(*args, **kwargs)
        endtime = time.perf_counter()
        print(f"end time {endtime}")
        print(f"time spend is {endtime-starttime}")
    return timeitwrapper


@DecoratorDemo
def breakast():
    print('Breakfast time ')

@DecoratorDemo
def dinner(name,dinnermenu):
    print(f"{name} is having {dinnermenu} for dinner ")
breakast()
dinner("joe","Pizza")