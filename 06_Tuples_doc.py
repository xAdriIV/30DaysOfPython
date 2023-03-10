# Day 6: Tuples

# A tuple is a collection of different data types which is ordered and unchangeable (immutable).
# Tuples are written with round brackets, ().
# We cannot use add, insert, remove methods in a tuple because it is not modifiable
# Unlike list, tuple has few methods. Methods related to tuples:

# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

# Creating a Tuple
# Empty tuple: Creating an empty tuple

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values
# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuple length
# We use the len() method to get the length of a tuple.
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)

# Accessing Tuple Items
# Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items. Accessing tuple items

# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
# Negative indexing Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item. Tuple Negative indexing

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]