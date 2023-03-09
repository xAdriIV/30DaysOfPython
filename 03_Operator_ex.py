# Exercises - Day 3

# Declare your age as integer variable
age = int()
# Declare your height as a float variable
height = float()
# Declare a variable that store a complex number
number_complex = complex()

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input('Escriba la base: ')
height = input('Ahora la altura: ')
area_of_triangle = 0.5 * int(base) * int(height)
print(area_of_triangle)
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
# # Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Ingrese el side a: ')
side_b = input('Ingrese el side b: ')
side_c = input('Ingrese el side c: ')
perimeter_of_triangle = int(side_a) + int(side_b) + int(side_c)
print(perimeter_of_triangle)
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = 8
width = 5
area = length * width
print(f"De {length} y {width} el area es: ", area)
perimeter = 2 *(length + width)
print(f"De {length} y {width} el perimetro es: ", perimeter)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Escriba el radio: ")
area_of_circle = 3.14 * int(radius) ** 2
print(f'el area es: ', area_of_circle)
radio2 = input("Escriba el radio: ")
circunference = 2 * 3.14 * int(radio2)
print(f'la circunferencia es: ', circunference)
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Define the equation
equation = "y = 2x - 2"
# Extract the coefficients
m = 2
b = -2
# Calculate the x-intercept
x_intercept = (1, 0)  # x = 1, y = 0
# Calculate the y-intercept
y_intercept = (0, -2)  # x = 0, y = -2
# Print the results
print("Equation:", equation)
print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_dragon = len('dragon')
len_python = len('python')
comp = len_dragon is not len_python
print(comp)
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
strdra = 'dragon'
strpyt = 'python'
find_on = 'on'
if find_on in strdra and strpyt:
    print('Se encontró: ' ,find_on)
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
jargon ='I hope this course is not full of jargon'
if 'jargon' in jargon:
    print('Jargon is in jargon')
# There is no 'on' in both dragon and python
if 'on' not in 'dragon' and 'python':
    print('No esta')
else:
    print('Si que esta')
# Find the length of the text python and convert the value to float and convert it to string
python_float = float(len_python)
python_string = str(len_python)
print(python_float, python_string)
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = input("Escriba un numero entero y le dire si es divisible por dos: ")
if int(x) % 2 == 0:
    print("Es divisible por dos")
else:
    print("No es divisible por dos")
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
if 7 // 3 == int(2.7):
    print("Si es") #print yes
else:
    print("No es")
# Check if type of '10' is equal to type of 10
check_numbers = '10' == 10
print(check_numbers)        # print false
# Check if int('9.8') is equal to 10
check_numbers2 = '9.8' == 10
print(check_numbers2)       # print false
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = input("Escriba las horas trabajadas: ")
rate_per_hour = input("Ratio por hora?:  ")
salary = int(hours) * float(rate_per_hour)
print("Este es su salario semanal: ", float(salary))
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
años_vividos = input("Escriba cuantos años tiene: ")
segundos_vividos = int(años_vividos) * int(31557600) # 1 año = 31557600 segundos
print("Has vivido:", segundos_vividos, "segundos.")
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
matriz = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]
for fila in matriz: # Recorrer la matriz y imprimir cada elemento
    for elemento in fila:
        print(elemento, end=' ')
    print() # Imprime salto de linea despues de cada fila