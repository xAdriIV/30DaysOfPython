# # Exercises: Day 9

# # Exercises: Level 1

# # Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# # You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# # Enter your age: 30
# # You are old enough to learn to drive.
# # Output:
# # Enter your age: 15
get_age = input("Enter your age: ")
if int(get_age) >= 18:
    print("You are old enough to learn to drive")
elif int(get_age) < 18:
    diff = 18 - int(get_age)
    print(f"You need",diff, "more years to learn to drive")
# # You need 3 more years to learn to drive.
# # Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# # You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# # Enter your age: 30
# # You are 5 years older than me.
my_age = 27
your_age = input("Enter your age: ")
if int(my_age) > int(your_age):
    print("Im older than you")
else:
    diff = int(your_age) - int(my_age)
    print(f"You are", diff,"years older than me")

# # Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# # Enter number one: 4
# # Enter number two: 3
# # 4 is greater than 3
a = input("Enter number one: ")
b = input("Enter number two: ")
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is esqual to b")

# # ### Exercises: Level 2
# # Write a code which gives grade to students according to theirs scores:

# # 80-100, A
# # 70-89, B
# # 60-69, C
# # 50-59, D
# # 0-49, F
note = int(input("Enter your note: "))
if note <= 49 or note == 0:
    print("Your grade is: F")
elif note >= 50 and note <= 59:
    print("Your grade is: D")
elif note >= 60 and note <= 69:
    print("Your grade is: C")
elif note >= 70 and note <= 89:
    print("Your grade is: B")
elif note >= 90 and note <= 100:
    print("Your grade is: A")
else:
    print("Error, range is 0 - 100")
    
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month: ")
month = month.capitalize()
if month == 'September' or month == 'October' or month == 'November':
    print("The season is Autum")
elif month == 'December' or month == 'January' or month == 'February':
    print("The season is Winter")
elif month == 'March' or month == 'April' or month == 'May':
    print("The season is Spring")
elif month == 'June' or month ==  'July' or month == 'August':
    print("The season is Summer")
elif month != 'September' or 'October' or 'November' or 'December' or 'January' or 'February' or 'March' or 'April' or 'May' or 'June' or 'July' or 'August':
    print("Please enther one month of the year")
else:
    ("Error, shutdown...")
# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
add_fruit = input("Enter a fruit: ")
print("Fruit to add: ",add_fruit)
print("Fruits: ",fruits)

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
if add_fruit not in fruits:
    print("Fruit not in list.\nAdding fruit to list...")
    add_fruit = [add_fruit]
    fruits.extend(add_fruit)
    print(fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

    person={
     'first_name': 'Asabeneh',
     'last_name': 'Yetayeh',
     'age': 250,
     'country': 'Finland',
     'is_married': True,
     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address': {
         'street': 'Space street',
         'zipcode': '02210'
     }
     }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print("Person has skills keys: ", type(person.keys()))
print("Middle skill: ", person['skills'][2])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print("Python is in person skills: ", 'Python' in person['skills'])
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 

if ('JavaScript' and 'React') in person['skills']:
    print("He is a front end developer")
#   if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
elif ('Node' and 'Python' and 'MongoDBperson') in person['skills']:
    print("He is a backend developer")
#   if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
elif ('React' and 'Node' and 'MongoDB') in person['skills']:
    print('He is a fullstack developer')
#   else print('unknown title') - for more accurate results more conditions can be nested!
else:
    print("unknown title")
#  * If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] == True and 'Finland' in person['country']:
    print(person['first_name'], person['last_name'],"lives in",person['country']+".","He is married")
#     Asabeneh Yetayeh lives in Finland. He is married.
print("# 🎉 CONGRATULATIONS ! 🎉")
# 🎉 CONGRATULATIONS ! 🎉
