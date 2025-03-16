test_ls=[1,2,3,4,4,5]
test_st=set(test_ls)
print(test_st)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3=st1.union(st2)
print(st3)
print(st1)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3=st1.intersection(st2) # {'item3', 'item2'}
print(st3)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Samsung', 'Huawei', 'Cisco'])
print(it_companies)
it_companies.remove('Huawei')
print(it_companies)
# it_companies.remove('Huawei') # error
it_companies.discard('Huawei') # no error
print(it_companies)

C=A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print   (words)
print(len(words))
unique_words = set(words)
print(len(unique_words ))