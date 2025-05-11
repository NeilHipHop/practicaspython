canasta = {'manzana','naranja','manzana','pera','naranja','platano'}

print(canasta)
#{'platano', 'naranja', 'manzana', 'pera'}

print('manzana' in canasta)
#True

print('melon' in canasta)
#False

vocales = ['a','e','i','o','u','a']
print(vocales)
#['a', 'e', 'i', 'o', 'u', 'a']         (lista normal a qui si respeta las repetidas)

vocales  =list(set(vocales))
print(vocales)
#['e', 'u', 'i', 'o', 'a']          (lista sin repetidos)

vocales1 = {'a','e','i','o','u','a'}
vocales2 = {'e','i','o'}
print(vocales2.issubset(vocales1))
#True                       (el conjunto vocales 2 "si" se encuentra en vocales 1)

vocales3 = {'A','E','I','O','U'}
print(vocales1 - vocales3)
#{'o', 'a', 'e', 'u', 'i'}      (imprime todos los valores por que son diferentes)

print(vocales1 | vocales3)
#{'u', 'I', 'E', 'O', 'e', 'A', 'o', 'a', 'i', 'U'}         (imprime las dos listas)

print(vocales1 & vocales3)
#{'o', 'u', 'e', 'a', 'i'}
#{'A', 'o', 'u', 'U', 'e', 'a', 'E', 'i', 'O', 'I'}
#set()                                                      (muestra los que se encuentra en ambos conjuntos en este caso no hay)

print(vocales1 ^ vocales3)
#{'I', 'U', 'u', 'i', 'a', 'O', 'e', 'o', 'E', 'A'}   (nos devulve los valores que estan en ambos conjuntos pero no en ambos)

