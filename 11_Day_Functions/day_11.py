def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

print_name('David') # David


def generate_groups (team,*args):
    print(team, end="\n\n")
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))


#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))

def add_all_nums(*args):
    total=0
    for i in args:
        total+=i
    return total
print(add_all_nums(2,3,5))

def to_faren(celsius):
    return (celsius * 9/5) + 32
print(to_faren(30))

def to_cel(farenheit):
    return (farenheit - 32) * 5/9
print(to_cel(30))

def print_list(lst):
    for i in lst:
        print(i)
print_list(['Asabeneh','David','Eyob'])


def reverse_list(lst):
    return lst[::-1]
print(reverse_list(['Asabeneh','David','Eyob']))


def capitalize_list_items(lst):
    return [i.upper() for i in lst]
print(capitalize_list_items(['asabeneh','david','eyob']))

def add_item(lst, *items):
    for i in items:
        lst.append(i)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat','Ginger'))

def remove_item(lst, *item):
    for i in item:
        if item in lst:
            lst.remove(i)
        print(f'{i} is not found in the list')
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango', 'Ginger'))

def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(5))

def sum_of_odds(n):
    odd_sum=sum([i for i in range(n+1) if i%2!=0])
    return odd_sum
sum_of_odds(5)


def evens_and_odds(n):
    num_of_evens = len([i for i in range(n+1) if i%2==0])
    num_of_odds = len([i for i in range(n+1) if i%2!=0])
    return num_of_evens, num_of_odds
print(evens_and_odds(100))

def factorial(n):
    n_factorial=1
    for i in range(1,n+1):
        n_factorial *=i
    return n_factorial
print(factorial(5))

def is_empty(lst):
    return len(lst)==0
print(is_empty([]))
print(is_empty([1,2,3]))


def stats(lst):
    mean = sum(lst)/len(lst)
    median= sorted(lst)[len(lst)//2]
    mode= max(set(lst), key=lst.count)
    range= max(lst) - min(lst)
    variance= sum([(i-mean)**2 for i in lst])/len(lst)
    std= variance **0.5
    return mean, median, mode, range, variance, std
print(stats([1,2,3,4,5,6,7,8,9,10]))


def find_unique_alt(lst):
    return len(lst)==len(set(lst))
print(find_unique_alt(['a','b','a','c','d','b','b']))
print(find_unique_alt([1,2,3,4,5,6,7,8,9,10]))

# Write a function which checks if all the items of the list are of the same data type.

def same_data_type(lst):
    item_types = [type(item) for item in lst]
    return len(set(item_types)) == 1
print(same_data_type([1,2,3,4,5,6,7,8,9,10]))
print(same_data_type(['a','b','a','c','d','b','b']))
print(same_data_type([1,2,3,4,5,6,7,8,9,10,'a']))

