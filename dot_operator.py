class StrangeType:
    x = 1
    y = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square_x(self):
        self.x = self.x ** 2        
    
    
    def cube_y(self):
        self.y = self.y ** 3

    
    def sum_data(given_thing):
        assert type(given_thing) == StrangeType   # if the type of "thing" is not "StrangeType" i'm gonna blow up.
        return given_thing.x + given_thing.y


def multiply(x, by_y):
    return x * by_y

murtazas_data = StrangeType(4, 5)
bartoszs_data = StrangeType(3, 2)

print(murtazas_data.x)
print(murtazas_data.y)

print(bartoszs_data.x, bartoszs_data.y)

bartoszs_data.square_x()

print(bartoszs_data.x)

murtazas_data.cube_y()

# -----
a = StrangeType.sum_data(murtazas_data)
b = StrangeType.sum_data(bartoszs_data)

# StrangeType.sum_data(murtazas_data, bartoszs_data)

print(str.strip("           Bartosz Slapa                  "))
# Bartosz Slapa

print("          Bartosz Slapa    ".strip())
# Bartosz Slapa

name = "    Bartosz Slapa "
print(name.strip())
# Bartosz Slapa

name2 = "MurtazaMMMMMMMMMMMMMMMMMMMMMMMMM"
print(name2.strip('Mua'))   # it removes all trailing  M, u, a
# rtaz

help(str.strip) # this helps


# . = "is a part of"
print(a, b)

# Traceback (most recent call last):
#   File "d:\dev\repos\GitHub\Strive\learnin_to_git\bartosz_murtaza\dot_operator.py", line 41, 
# in <module>
#     b = murtazas_data.sum_data(bartoszs_data)
# TypeError: sum_data() takes 1 positional argument but 2 were given





# print(1, 2, 3, 4, "sexy", "comsos", [1,2,3], {"one":1, "two":6})
# name = "Martin"
# print(name, bartoszs_data.x, "is", "very", murtazas_data.y, "handsome", "Indian", "Man!")

