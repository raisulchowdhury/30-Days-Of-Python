# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
print(all_fruits)
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
print(all_fruits)


# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first, *rest = fruits
print(first)
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']


fruits = ["apple", "banana", "cherry"]
fruits[1:1] = ["orange", "mango", "pineapple"]  # Insert at index 1
print(fruits)
letter_count = sum([len(fruit) for fruit in fruits])
print(letter_count)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.sort())
# print(sorted(fruits))  
print(len(fruits))

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
# it_companies.sort()
# print(it_companies)
print(sorted(it_companies))
print(it_companies)
# it_companies.clear()
# print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.extend(["Python", "SQL"])
print(full_stack)
double_stacked =full_stack.copy()
print(double_stacked)

ages = [19, 22, 19, 24, 20, 25, 26, 25, 25, 25, 25]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
print(sum(ages)/len(ages))
print(max(ages)-min(ages))
print(len(ages))
# if odd then floored else middle 2 avg

median=ages[len(ages)//2] if len(ages)%2!=0 else (ages[len(ages)//2]+ages[len(ages)//2-1])/2
print(median)