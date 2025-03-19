# #continue break
# count = 0
# while count < 5:
#     print(count)
#     count = count + 1

# print("tada!")

# count = 0
# while count < 5:
#     if count == 3:
#         continue #break
#     print(count)
#     count+=1


# language = 'Python'
# for letter in language:
#     print(letter)

# for i in range(len(language)):
#     print(language[i])
    
# for i in range(1,10,3):
#     print(i)


# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
# print('outside the loop')

# lst = list(range(10))
# print(lst)

# lst2 = [range(10)]
# print(lst2)    
# print(type(lst2[0]))


# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)
            
# for number in range(11):
#     print(number)   # prints 0 to 10, not including 11
# else:
#     print('The loop stops at', number)

##Exercises
# for i in range(10,-1,-1):
#     print (i)
# i=10
# while i>=0:
#     print(i)
#     i-=1

# for i in range(1,8):
#     print("#"*i)
    
# for row in range(8):
#     for col in range(8):
#         print("#", end=" ")
#     print("\n")

# for i in range(11):
#     print (f"{i} X {i} = {i*i}")


# languages = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for language in languages:
#     print(language)

# for language in  languages:
#     for letter in language:
#         print(letter,end=" ")
#     print()
    
# uni_letter = {letter  for language in languages for letter in language}
# print(uni_letter)
# uni_str = list(uni_letter)
# print(uni_str)
# print(sorted(uni_str))
# uni_tup=tuple(uni_letter)
# print(sorted(uni_tup))

# evens = [i for i in range(101) if i%2==0]
# odds =  [i for i in range(101) if i%2!=0]
# print(evens, odds, sep="\n\t")

# total=0
# for i in range (101):
#     total+=i
# print(f"The sum of all numbers in {total}.")

# total = sum(i for i in range(101))
# print(f"The sum of all numbers in {total}.")

# even_sum = sum(i for i in range (101) if i%2==0)
# odd_sum = sum(i for i in range (101) if i%2!=0)
# print(f"The sum of all even numbers is {even_sum}. And the sum of all odd numbers is {odd_sum}.")

# from data import countries
# print(countries.countries)
# country_land = [country for country in countries.countries if 'land' in country.lower()]
# print(country_land)


# fruit_loops =['banana', 'orange', 'mango', 'lemon']
# # print(fruit_loops.reverse())

# # fruit_loops.reverse()
# # print(fruit_loops)

# rev_list=[]
# for index in range (len(fruit_loops)-1,-1,-1):
#     print(index)
#     rev_list.append(fruit_loops[index])
# print(fruit_loops)
# print(rev_list)

# Import required modules
from data import countries_data
read = open('data/countries_data.py')
print(read.read())
print(type(countries_data))
print(countries_data[0])
print(countries_data[0]['name'])
print(countries_data[0]['capital'])
print(countries_data[0]['languages'])