#  Exercises - Day 4

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = 'Thirty', 'Days', 'Of', 'Python'
string_join = ' '.join(string)
print(string_join)
string1 = 'Thirty'
string2 = 'Days'
string3 =  'Of'
string4 = 'Python'
string_conc = '{} {} {} {}'.format(string1, string2, string3, string4)
print(string_conc)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
# Declare a variable named company and assign it to an initial value "Coding For All".
company = '{} {} {}'.format(str1, str2, str3)
# Print the variable company using print().
print('Using format: ', company)
# Print the length of the company string using len() method and print().
print('Len: ', len(company))
# Change all the characters to uppercase letters using upper() method.
company = company.upper()
print('Using upper: ', company)
# Change all the characters to lowercase letters using lower() method.
company = company.lower()
print('Using lower: ', company)
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = company.capitalize()
print('Using capitalize: ', company)
company = company.title()
print('Using title: ', company)
company = company.swapcase()
print('Using swapcase: ', company)
# Cut(slice) out the first word of Coding For All string.
company = company[6:15]
print('Cut first word of Coding for all:',company)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding_find = 'Coding For All'
find_coding = coding_find.find('Coding')
print('Find coding: ',find_coding)
if 'Coding' in coding_find:
    print('"Coding" is in "Coding For All"')
else:
    print('Is not')
# Replace the word coding in the string 'Coding For All' to Python.
company = 'Coding For All'
replace_company = company.replace('Coding','Python')
print(replace_company)
# Change Python for Everyone to Python for All using the replace method or other methods.
replace_company1 = replace_company.replace('Python','Python for Everyone')
print(replace_company1)
# Split the string 'Coding For All' using space as the separator (split()) .
split_company = replace_company1.split()
print(split_company)
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(techs.split())
# What is the character at index 0 in the string Coding For All.
company = 'Coding For All'
company_first = company[0]
print('first letter: ',company_first)
# What is the last index of the string Coding For All.
company_last = company[13]
print('last letter: ',company_last)
# What character is at index 10 in "Coding For All" string.
print('character at index 10: ',company[10], '(space)')
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym_str = 'Python For Everyone'
acronym = acronym_str[0]
acronym1 = acronym_str[7]
acronym2 = acronym_str[11]
print('Acronym of "Python For Everyone" is: ',acronym + acronym1 + acronym2)
# Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_str2 = 'Coding For All'
acronym_code = acronym_str2[0]
acronym_code1 = acronym_str2[7]
acronym_code2 = acronym_str2[11]
print('Acronym of "Coding For All" is: ',acronym_code + acronym_code1 + acronym_code2)
# Use index to determine the position of the first occurrence of C in Coding For All.
find_c = acronym_str2.find('C')
print(find_c)
# Use index to determine the position of the first occurrence of F in Coding For All.
index_f = acronym_str2.index('F')
print(index_f)
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
find_l = acronym_str2.rfind('l')
print(find_l)
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
bcause = 'You cannot end a sentence with because because because is a conjunction'
find_bcause = bcause.find('because')
print(find_bcause)
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
bcause2 = 'You cannot end a sentence with because because because is a conjunction'
find_bcause2 = bcause2.rfind('because')
print(find_bcause2)
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_out = 'You cannot end a sentence with because because because is a conjunction'
string_out = slice_out.replace('because','')
print('Slice out "because" from "You cannot end a sentence with because because because is a conjunction", Result= \n',string_out)
# Does ''Coding For All' start with a substring Coding?
substring_coding = 'Coding For All'
substring = 'Coding'
print('Prints 0 if starts with "Coding": ',substring_coding.index(substring))
# Does 'Coding For All' end with a substring coding?
substring_coding = 'Coding For All'
substring = 'Coding'
print('Prints 0 if doesnt found at end "Coding": ',substring_coding.rindex(substring))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
str_rep_tabs = '   Coding For All      '
right_tab = str_rep_tabs.replace('      ','')
right_tab = right_tab.replace('   ','')
print(right_tab)
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'
print(var1.isidentifier())
print(var2.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libaries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
hash_join = ' ,#'.join(python_libaries)
print(hash_join)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity\tAsabeneh\t250\tFinland\tHelsinki")
# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
result = "The are of circle with radius {} is {} meters square.".format(str(radius),str(area))
print(result)
# Make the following using string formatting methods:
# 8 + 6 = 14
res = "El resultado de 8 + 6 es: {}".format(int(8 + 6))
print(res)
# 8 - 6 = 2
res1 = "El resultado de 8 - 6 es: {}".format(int(8 - 6))
print(res1)
# 8 * 6 = 48
res2 = "El resultado de 8 * 6 es: {}".format(int(8 * 6))
print(res2)
# 8 / 6 = 1.33
res3 = "El resultado de 8 / 6 es: {}".format(int(8 / 6))
print(res3)
# 8 % 6 = 2
res4 = "El resultado de 8 % 6 es: {}".format(int(8 % 6))
print(res4)
# 8 // 6 = 1
res5 = "El resultado de 8 // 6 es: {}".format(int(8 // 6))
print(res5)
# 8 ** 6 = 262144
res6 = "El resultado de 8 ** 6 es: {}".format(int(8 ** 6))
print(res6)
# 🎉 CONGRATULATIONS ! 🎉
print("🎉 CONGRATULATIONS ! 🎉")