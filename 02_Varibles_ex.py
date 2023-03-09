# Ejercicio: Nivel 1
# Día 2: 30 días de programación en python
nombre = 'Adrian'
apellido = 'Ignacio'
nombre_completo = nombre + (' ')+ apellido
pais = 'España'
edad = '18'
año = '1995'
is_married = False
is_true = True
is_light = True
informacion_total = "Me llamo " + (nombre_completo) + " y tengo " + (edad) + " nací en " + (año)
print(informacion_total)

# Ejercicio: Nivel 2
# Verifique el tipo de datos de todas sus variables usando la función incorporada type ()
print(type(nombre))
print(type(apellido))
print(type(is_married))
# Usando la función incorporada len() , encuentre la longitud de su nombre
print(len(nombre))
# Compare la longitud de su nombre y su apellido
print(len(nombre), len(apellido))
# Declarar 5 como num_one y 4 como num_two
num_one = 5
num_two = 4
# Agregue num_one y num_two y asigne el valor a un total variable
num_total = num_one + num_two
# Reste num_two de num_one y asigne el valor a una variable diff
num_diff = num_two - num_one
# Multiplique num_two y num_one y asigne el valor a un producto variable
num_prod = num_two * num_one
# Divide num_one por num_two cy asigna el valor a una división variable
num_div = num_one / num_two
# Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
num_divmod = num_two % num_one
# Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
num_exp = num_one ** num_two
# Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
num_floor_division = num_one // num_two
# El radio de un círculo es de 30 metros.
radius = 30
# Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
area_of_circle = 3.14 * radius ** 2
# Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
diametro = 15
circum_of_circle = 2 * 3.14 * diametro
# Tome el radio como entrada del usuario y calcule el área.
radio = input('Escribe el radio y devuelvo el area: ')
area_of_circle2 = 3.14 * int(radio) ** 2
print("El area del ciruclo es: ", area_of_circle2)
# Use la función de entrada incorporada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
name = input("Escribe tu nombre: ")
subname = input("Escribe tu apellido: ")
age = input("Escribe tu edad: ")
country = input("Escribe tu pais: ")
# Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras reservadas o las palabras clave de Python
help ('keywords')
dir(str)