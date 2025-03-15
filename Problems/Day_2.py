# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

radius = 30
pi=3.14
area=pi*(radius**2)
print(area)
circumference=2*pi*radius
print(circumference)
first_name, last_name, country, age = input("Enter your first name :"), input("Enter your last name: "), input("Enter your country: "), input("Enter your age: ")
print(first_name, last_name, country, age)
