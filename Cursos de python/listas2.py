vocales = ['a', 'e' ,'i' ,'o' ,'u']

vocales[1:4] = ['E', 'I', 'O']

print(vocales)
#['a', 'E', 'I', 'O', 'u']
print(vocales, len(vocales))
#['a', 'E', 'I', 'O', 'u'] 5
vocales[1:4] =[]

print(vocales, len(vocales))
#['a', 'u'] 2

vocales[1:2] = ['e','i','o','u']

print(vocales, len(vocales))
#['a', 'e', 'i', 'o', 'u'] 5

vocales.extend(['i','i'])

print(vocales, len(vocales))
#['a', 'e', 'i', 'o', 'u', 'i', 'i'] 7

print(vocales.index('i'))
#2      (nos dara su indice en este caso 'i' esta en el '2')

print(vocales.count('i'))
#3      (cuenta los repetidos en este caso 'i' se repite '3'veces)

print(vocales.index('i', 4))
#5      (empieza a buscar de izquierda a derecha iniciendo en el indice 4 y nos da el indice '5' )
print(vocales.index('i', 5))
#5      (empieza a buscar de izquierda a derecha iniciendo en el indice 4 y nos da el indice '5' )

vocales.reverse()
print(vocales, len(vocales))
#['i', 'i', 'u', 'o', 'i', 'e', 'a'] 7      (invierte la lista)
vocales.sort()
print(vocales, len(vocales))
#['a', 'e', 'i', 'i', 'i', 'o', 'u'] 7      (ordena la lista)

########################################################################################
carros = ['audi', 'ford', 'bmw', 'vw', 'kia']
carros.sort(key=len)
print(carros)
#['vw', 'bmw', 'kia', 'audi', 'ford']   (ordenada de manor a mayor en catidad de caracteres y de a a la z)

#####################################################################################33

listas = [[0,1],[2,3,4],[5,6]]
print(listas[0], listas[1:3])
#[0, 1] [[2, 3, 4], [5, 6]]
print(listas[2][1])
#6      (imprime el valor de la lista '2' indice '1')

# x = [3, 2.5, 6, 6.3] es igaul a un casillero, es mas facil recordar donde esta que lo informacion que contiene
####################################################################################

vocales1 =['a','e','i','o','u']
vocales2 = vocales1
print(vocales1, vocales2)
#['a', 'e', 'i', 'o', 'u'] ['a', 'e', 'i', 'o', 'u']
print(id(vocales1), id(vocales2))
#2483060508352 2483060508352
vocales3 = vocales1.copy()
print(vocales1, vocales3)
#['a', 'e', 'i', 'o', 'u'] ['a', 'e', 'i', 'o', 'u']
print(id(vocales1), id(vocales3))
#1810925257152 1810925182400
print(id(vocales1[2]), id(vocales2[2]))
#140703928942944 140703928942944
print(id(vocales1[2]), id(vocales2[2]))

del vocales1[1]
print(vocales2,vocales3)
#['a', 'i', 'o', 'u'] ['a', 'e', 'i', 'o', 'u'] en vocales2 se elimina 'i', en vocales3 no se elimina 
print(id(vocales1[2]),id(vocales3[3]))
#140703928943232 140703928943232 aqui se esta imprimiendo el id de la 'o'
