# decoraters

# function which enhance the other fucntion

# high order functions

# the functions that pass function as an argument
# also return funtion


def saymyname(fun):
    def wrapper(*args, **kwargs):
        print("say my name")
        fun(*args, **kwargs)
        print("right!!!")
    return wrapper


@saymyname
def greet(name):
    print(f"hiii {name}")


@saymyname
def add(a, b):
    print(a + b)


add(7, 8)
greet("Ijx")
