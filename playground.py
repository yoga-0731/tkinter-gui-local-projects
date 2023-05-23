# Default arguments
def add(a=1, b=2, c=3):
    return a + b + c


print(add(2))


# Unlimited positional arguments - functions with many arguments
def add(*args):
    print(f"{type(args)} {args}")
    return sum(args)


print(add(1, 2, 3, 4, 5))


# Unlimited keyword arguments
# Example - 1:
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


calculate(a=5, b=10)


# Example - 2:
def calculate(n , **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=5, multiply=10)


# Class with kwargs (like tkinter)
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs.get('model')  # Advantage of get() is if the key is not in kwargs, it returns None
        # and not an error


car = Car(make='Nissan')
print(car.make, car.model)


# Mix of all
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
