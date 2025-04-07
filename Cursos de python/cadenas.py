# texto_variado = '123 +-* #%&'
# print(type(texto_variado))

# # Podemos utilizar comillas triple para que el texto se muetre como la cadena que hemos escrito
# print("""
# Funcionamiento de \
# Programa: (opciones)
#     -1 Para acceder a opcines
#     -2 Para salir
# """)

###################################################################################################################
# # subscripting e indexado

# texto = 'Python'

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# # print(texto[6]) # error no podemos a acceder a una posicion que no existe
# # print(texto[-7]) # error no podemos a acceder a una posicion que no existe

# letra = texto[0]
# print(letra)

# # texto[0] = "P" # error no podemos modificar una cadena

# letra = "p"
# print(letra)

# texto_compuesto = letra + texto[1] # concatenacion
# print(texto_compuesto)

##############################################################################################

# # slicing o substringing
# texto = "Python"

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2]) # no da resultado 

################################################################################################
#cadena y formatos

# texto ="hola mundo! Buenastardes"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# texto = texto.upper()
# print(texto)

print("{} + {} = {}".format(2,3,2+3))
print("{} + {} ={}".format("hola","mundo","hola mundo"))
print("{:.3f} + {:4f} = {}".format(2,3,2 +3 ))
print("{1} + {0} = {2}".format(2,3,2+3))
print("{1} + {0} = {2}".format("hola","mundo","hola mundo"))
print("{:d} = {:b} = {:o}= {:x}". format(15, 15, 15, 15,)) # :d muestra en el sistema decimal, :b sistema binario, :o sitema octal, :x sistema exadecimal
