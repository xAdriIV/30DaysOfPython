# Ejercicios: Día 5
# ------------------
# Ejercicios: Nivel 1

# Declare an empty list
empty_list = list()
# Declare a list with more than 5 items
soccers = ['Cristiano', 'Modric', 'Vinicius', 'Kross', 'Valverde']
# Find the length of your list
print('Number of players: ', len(soccers))
# Get the first item, the middle item and the last item of the list
first_soccer = soccers[0]
print(first_soccer)
third_soccer = soccers[2]
print(third_soccer)
last_soccer = soccers[-1]
print(last_soccer)
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["name","age","height","marital status","address"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
# Print the list using print()
print(mixed_data_types,"\n",it_companies)
# Print the number of companies in the list
print("Number of companies in the list: ",len(it_companies))
# Print the first, middle and last company
first_company = it_companies[0]
print(first_company)
middle_company = it_companies[3]
print(middle_company)
last_company = it_companies[-1]
print(last_company)
# Print the list after modifying one of the companies
it_companies[0] = 'Youtube'
print(it_companies[0:])
# Add an IT company to it_companies
it_companies.append('IT')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(4,'IT')
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
upper_comp = it_companies[0].upper()
print(upper_comp + str(it_companies))
# Join the it_companies with a string '#;  '
hash_comp = '#; '.join(it_companies)
print(hash_comp)
# Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
del it_companies[0:3]
print('Slice first 3: ', it_companies)
# Slice out the last 3 companies from the list
del it_companies[-3:] # (de -3 en adelante)
print('Slice last 3: ', it_companies)
# Slice out the middle IT company or companies from the list
del it_companies[0:1]
print('Slice middle it: ', it_companies)
# Remove the first IT company from the list
del it_companies[0]
print('Remove first it : ',it_companies)
# Remove all IT companies from the list
del it_companies[0:]
print('Lista vacia...',it_companies)
# Destroy the IT companies list
del it_companies
print("Lista borrada.")
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end + back_end
print(fullstack)
# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
fullstack.insert(5,'Python')
fullstack.insert(6,'SQL')
print(fullstack)

# Exercises: Level 2
#--------------------
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort(reverse=False)
print('min to max ages: ',ages)
# Add the min age and the max age again to the list
ages_double = ages + ages
ages_double.sort(reverse=False)
print('min to max ages doubles: ',ages_double)
# Find the range of the ages (max minus min)
age_range = max(ages_double) - min(ages_double)
print('Range age: ',age_range)
# Find the median age (one middle item or two middle items divided by two)
age_media = ages_double[10] / 2
print('Media age: ', age_media)
# Find the average age (sum of all items divided by their number )
ages_double = sum(ages_double) / len(ages_double)
print('Average age: ', int(ages_double))
# Compare the value of (min - average) and (max - average), use abs() method
print('Magnitude of ages double: ',abs(ages_double))
# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries_middle = countries[3:5]
print('Print middle countries in the list: ',countries_middle)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries1 = countries[0:3]
countries2 = countries[3:]
print(countries1, countries2)
print()

# def split(arr, size):
#      arrs = []
#      while len(arr) > size:
#          pice = arr[:size]
#          arrs.append(pice)
#          arr   = arr[size:]
#      arrs.append(arr)
#      return arrs
# print(split(countries,3))
# Reverse split list
def split(arr, size):
      arrs = []
      while len(arr) > size:
          pice = arr[size:]
          arrs.append(pice)
          arr   = arr[:size]
      arrs.append(arr)
      return arrs

list_reverse = split(countries,3)
list_reverse.reverse()
print("First 3 and the scandic countries: ",list_reverse)
# 🎉 CONGRATULATIONS ! 🎉
print("🎉 CONGRATULATIONS ! 🎉")