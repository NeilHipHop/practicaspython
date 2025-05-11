vocales = ('a','e','i','o','u')

print(vocales[2])
#i

# vocales[2] ='I' (no se pueden modificar las tuplas)

print(vocales[:3] + vocales[2:])
#('a', 'e', 'i', 'i', 'o', 'u')

print(vocales)
#('a', 'e', 'i', 'o', 'u')

print(vocales.index('o'))


lista_vocales = list(vocales)

lista_vocales[2] = 'I'

print(lista_vocales)
#['a', 'e', 'I', 'o', 'u']
