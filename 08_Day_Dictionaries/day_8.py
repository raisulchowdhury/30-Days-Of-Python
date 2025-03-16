# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
print(person['address']['zipcode'])
print(person.get('city'))   # None'))
person['company']="Google"
print(person)
person['company']="Netflix"
print(person)
person["company"]=[person['company']]
print(person)
print("age" in person)



person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
all_keys = person.keys()
print(all_keys)

person.pop("age")
print(person)

person.popitem()
print(person)

del person['is_marred']
print(person)

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

dct_list = dct.items()
print(dct_list)

dct_list_alt = list(dct.items())
print(dct_list_alt)

dct_list_alt.clear()
print(dct_list_alt)

print(dct)
# dct.clear()
# print(dct)

keys_list = dct.keys()
print(keys_list)

values_list = dct.values()
print(values_list)

dog = {}  # Existing empty dictionary
dog.update({'name':'diggi', 
            'color':'brown',
            'breed':'German Shepherd',
            'legs':[4,5]})
print(dog)
print(len(dog.items()))
print(len(dog['legs']))
dog['legs'].append(6)
print(len(dog['legs']))
print(len(dog.items()))
dog_tuple = dog.items()
print(dog_tuple)
dog.pop('legs')
print(dog)
dog.clear()
print(dog)
del dog
print(dog)