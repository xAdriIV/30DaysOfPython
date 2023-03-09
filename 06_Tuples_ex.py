# 💻 Exercises: Day 6

# Exercises: Level 1
# Create an empty tuple
empty_tuple = tuple()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis = ('rebeca', 'mabel')
bro = ('victor','xavi','Edu')
# Join brothers and sisters tuples and assign it to siblings
siblings = sis + bro
# How many siblings do you have?
print('I have:',len(siblings),'Siblins')
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
parents = ["minerva", "vicente"]
family_members.extend(parents)
print("Extend parents, using list: ",family_members)
#siblings_list = list(siblings_tuple)
#print(siblings_list)
family_members = tuple(family_members)
print("Return to tuple: ",family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = list(family_members[0:4])
parents = list(family_members[-2:])
print("sibs: ",siblings)
print("parents:", parents)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animals = ('cat','dog','cow','snake','fish')
food_stuff_tp = fruits + vegetables + animals
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_lt))
print(food_stuff_lt)
slice_middle = food_stuff_lt[6:8:1]
print("Slice out the middle items: ",slice_middle)
# Slice out the first three items and the last three items from food_staff_lt list
print("Slice out the first three items and the last three",food_stuff_lt)
first3 = food_stuff_lt[0:3]
lasts3 = food_stuff_lt[-3:]
print("First 3 : ",first3)
print("Last 3: ", lasts3)
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
print(food_stuff_tp[0])
print('orange' in food_stuff_tp) # Asking for food_stuff_tp and return "False" because the tuple is del
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

