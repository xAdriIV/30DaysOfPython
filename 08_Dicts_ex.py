# Exercises: Day 8

# Create an empty dictionary called dog
dog = {
    'name':'kios',
    'color':'white',
    'breed':'None',
    'legs':'four',
    'age': 5
    }
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys
# for the dictionary
student = {
    'first_name':'Adrian',
    'last_name':'Ignacio',
    'gender':'Men',
    'age': 27,
    'marital status':'Single',
    'skills':['Python','C', 'JavaScript','HTML'],
    'country':'Spain',
    'city':'Madrid',
    'address':{
        'street':'San Mateo',
        'zipcode':'2800'
    }
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('CSS')
print(student['skills'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.popitem() # Remove the last item
# Delete one of the dictionaries
student.pop('city')
print(student)
# 🎉 CONGRATULATIONS ! 🎉
print("🎉 CONGRATULATIONS ! 🎉")