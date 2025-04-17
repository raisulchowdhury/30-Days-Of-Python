# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

add_three_nums = lambda a,b,c: (a+b+c)
print(add_three_nums(2,3,4))    # 9

def power(x):
    return lambda n : x ** n

print(power(2)(3))

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
[n for n in numbers if n<=0]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
[num for row in list_of_lists for sec_row in row for num in sec_row]

[(i, i**0, i**1, i**2, i**3,i**4,i**5) for i in range (11)]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

[[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)] in countries]

[{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

[' '.join((first, last)) for [(first, last)]  in names]
[(first + " " + last) for [(first, last)]  in names]
[(f"{first} {last}") for [(first, last)]  in names]