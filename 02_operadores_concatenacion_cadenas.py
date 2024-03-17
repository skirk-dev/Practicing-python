'''
Operadores y Concatenación de Cadenas:

    Ejercicio 1: Utiliza operadores de comparación para comparar diferentes valores y muestra los resultados.

    Ejercicio 2 : Realiza operaciones de concatenación de cadenas usando diferentes métodos
    (formato, f-strings, concatenación directa).
'''


### EJERCICIO 1 ###

name1 = input("Ingrese su nombre: \n").lower()
edad1 = int(input("Ingrese su edad: \n"))
city1 = input("Ingrese su ciudad: \n").lower()
deci1 = float(input("Ingrese decimal: \n"))

name2 = input("\n\nIngrese su nombre 2: \n").lower()
edad2 = int(input("Ingrese su edad 2: \n"))
city2 = input("Ingrese su ciudad 2: \n").lower()
deci2 = float(input("Ingrese decimal 2: \n"))

print("\n\nEJERCICIO 2")
print("\nEl nombre es igual: "+ name1 == name2)
print("\nLa edad 1 es menor a la edad 2: "+ str(edad1 < edad2))
print("\nLa edad 2 es mayor o igual a la edad 1: "+ str(edad2 >= edad1))
print("\nLa edad 1 y decimal 1 es mayor o igual a la edad 2 y decimal 2: "+ str(edad1 and deci1 >= edad2 and deci2))
print("\nLa ciudad 1 es diferente de la ciudad 2: "+ str(city1 != city2))
print("\nLa edad 1 menos el decimal 2 es diferente de la edad 2 menos el decimal 1: "+ str(edad1 - deci2 != edad2 - deci1))
print("\nEl nombre 1 o la ciudad 2 es diferente de el nombre 2 y la ciudad 1: "+ str(name1 or city2 != name2 or city1))



### EJERCICIO 2 ###

print("\n\nEJERCICIO 2")
print(f"\nSus nombres son {name1} {name2}, sus edades son {edad1} y {edad2} y sus ciudades son {city1} y {city2}")

print("\nSus nombres son " + name1 + " y " + name2 + " y sus edades son " + str(edad1) + " y " + str(edad2) + " sus ciudades son "+ city1 + " y " + city2)

print("\nSus nombres son {} {}, sus edades son {} {} y sus ciudades son {} {}".format(name1, name2, edad1, edad2, city1, city2))

print("\nSus nombres son %s %s, sus edades son %d %d y sus ciudades son %s %s " %(name1, name2, edad1, edad2, city1, city2))
