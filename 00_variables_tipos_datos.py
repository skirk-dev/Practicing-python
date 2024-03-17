'''
Variables y tipos de datos:

    Ejercicio 1: Crea variables para almacenar tu nombre, apellido, edad y ciudad de origen.
    Imprime el valor de cada variable utilizando diferentes métodos de concatenación.

    Ejercicio 2: Convierte tu edad a diferentes tipos de datos (int, float, str) y verifica cómo cambia el valor
    y la representación.

    Ejercicio 3: Crea una variable para almacenar un número decimal y otra para un número entero.
    Realiza operaciones matemáticas básicas (suma, resta, multiplicación, división) con estas
    variables y observa los resultados.
'''

### EJERCICIO 1 ###
name = (input("Ingrese su nombre: "))
surname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
city = input("Ingrese su ciudad natal: ")

print("Su nombre es {} {}, tiene {} anos y su ciudad natal es {}".format(name, surname, age, city))
print(f"Su nombre es {name} {surname}, tiene {age} anos y su ciudad natal es {city}")
print("Su nombre es %s %s, tiene %d anos y su ciudad natal es %s" %(name, surname, age, city))



# EJERCICIO 2 ###
age=str(age)
print(type(age))

age = float(age)
print(type(age))


age=int(age)
print(type(age))


### EJERCICIO 3 ###
num_int=int(input("Ingrese numero entero: "))
num_float=float(input("Ingrese numero decimal: "))
print(num_int + num_float)
print(num_int - num_float)
print(num_int * num_float)
print(num_int/num_float)