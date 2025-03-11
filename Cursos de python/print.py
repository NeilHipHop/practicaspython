# ejemplo de la funcion print()

print("hola mundo")
print("hola mundo","otra vez")
print("son las", 9, "de la mañana")
print("el resultado de 3 * 4 es de:", 3*4)

#ejemplo de cadenas formateadas
print("el numero 15 en sistema decimal es %d, en sistea octal es %o, en el sistema hexadesimal es %x" %(15,15,15))

pi = 3.1416
r = 5
print(f"el radio de un circulo es {r} y el area de  ese circulo es {pi * r ** 2 : .2f}")

# imprision de caracteres especiales
print("la letra beta es:\n\t \u03b2")

# caracteres de  escape
print("hola mundo",  end = " ")
print("otra vez", end = "\t")
print("y otra vez")
