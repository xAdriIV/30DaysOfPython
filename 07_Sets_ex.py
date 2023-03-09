# 💻 Exercises: Day 7

# # Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla','Space X'])
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('Amazon')
print(it_companies)
# What is the difference between remove and discard
it_companies.discard('Oracle')
print(it_companies)
# Exercises: Level 2

# Join A and B
print(A.union(B)) # Skip repeats
# Find A intersection B
intersec_AB = A.intersection(B)
print(intersec_AB)
# Is A subset of B
print("Is A subset of B: ",A.issubset(B))
# Are A and B disjoint sets
print("Are A and B disjoint sets: ",A.isdisjoint(B))
# Join A with B and B with A
print("Join A with B and B with A: ",A.union(B.union(A)))
# What is the symmetric difference between A and B
print("Symmetric difference between A and B: ",A.difference(B))
# Delete the sets completely
del A,B
it_companies.clear()
# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print("Compare the length of the list and the set: ","age: ",len(age),"//","age_st: ",len(age_st))
# Explain the difference between the following data types: string, list, tuple and set
print("characters only -",type("string"))
print("Group elements modificable -",type(list()))
print("Group elements unmutable -",type(tuple()))
print("Collection of items -",type(set()))
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
stc = {"I", "am", "a", "teacher", "and", "I", "love", "to", "inspire", "and", "teach", "people."}
print(len(stc))
# 🎉 CONGRATULATIONS ! 🎉