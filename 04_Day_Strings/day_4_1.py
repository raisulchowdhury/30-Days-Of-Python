company="Coding For All"
company.lower()
print(company)
first=(company.split())[0]
print(first)
print(company.replace ('Coding', 'Python'))
print(company)
print(company[10:])
new_company="Python For Everyone"
nc_lst=new_company.split()
split_lst=[i[0] for i in nc_lst]
print(split_lst)
print(''.join(split_lst))
print(company.lower().rfind('i'))
bec_sentence="You cannot end a sentence with because because because is a conjunction"
bec_only=bec_sentence[bec_sentence.find('because'): (bec_sentence.rfind('because')+1)]
print  (bec_only)
for index,i in enumerate(bec_sentence):
    print(index,i)
new_sentence=bec_sentence.replace('because because because','')
print(new_sentence)
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_lib=" ".join(libraries)
print(new_lib)