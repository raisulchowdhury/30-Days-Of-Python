def absolute(x):
    return x if x>=0 else -x

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')



# Suppose you have a list of numbers, and you want to:

# Square each number (map).
# Keep only the even squares (filter).
# Calculate their product (reduce).
#  Here’s how you can do it:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, numbers))
print(squared_nums)
even_squares = list(filter(lambda x: x%2==0, squared_nums))
print(list(even_squares))

prod = reduce(lambda x,y: x*y,even_squares)
print(prod)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list(map(lambda x: print(x), countries))
list(map(lambda x: x.upper(),countries))
list(map(lambda x: [x,x**2],numbers))
list(filter(lambda x: 'land' in x, countries))
list(filter(lambda x: len(x)==6, countries))
list(filter(lambda x: x.startswith('E'), countries))

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

from functools import reduce
result = reduce(lambda x,y: x+", "+y if y!=countries[-1] else x+" and "+y, countries)
print(result + " are north European countries.")

#12