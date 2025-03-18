for a in range(-2, 3):
    print ('positive') if a>0 else print('negative') if a<0 else print ('zero')

age = int(input("what's your age? "))

if age>=18:
    print('You are old enough to drive')
else:
    print(f"you need {18-int(age)} more years to learn to drive.")

my_age: int = 250
your_age = int(input("Enter your age: "))
gap = my_age-your_age
mid_text = "year" if abs(gap)==1 else "years" if abs(gap)>1 else ""

if gap ==0:
    print ("We are of the same age")
else:
    print(f"I am {abs(gap)} {mid_text} older than you") if gap>0 else print(f"I am {abs(gap)} {mid_text} younger than you")
    
score = int(input("Enter your score: "))
grade = "A" if score>=80 else "B" if 70<=score<80 else "C" if 60<=score<70 else "D" if 50<=score<60 else "F"
print(f"Your grade is {grade}")


summer = "June, July, August"
autumn = "September, October, November"
winter = "December, January, February"
spring = "March, April, May"
month = input("Enter month: ")
season = "Summer" if month.lower() in summer.lower() else "Autumn" if month.lower() in autumn.lower() else "Winter" if month.lower() in winter.lower() else "Spring" if month.lower() in spring.lower() else "Please enter the full month name"
print(f"The season is {season}")


fruits = ['banana', 'orange', 'mango', 'lemon']

fav_fruit = input("what's your favourite fruit? ")
if fav_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fav_fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])

coding_skills = person.get('skills')
coding_skills = set(coding_skills)
front_end_skills = {'JavaScript', 'React'}
back_end_skills = {'Node', 'Python', 'MongoDB'}
full_stack_skills = {'React', 'Node', 'MongoDB'}

if coding_skills == front_end_skills:
    print("He is a front end developer")
elif coding_skills.issuperset(back_end_skills):
    print("He is a back end developer")
elif coding_skills.issuperset(full_stack_skills):
    print("He is a full stack developer")
else:
    print("unknown title")

if person['is_marred'] and person['country']=='Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is marred.")