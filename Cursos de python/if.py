num = int(input("Ingresa un entero : "))
if num <0:
    num = -num
print('Su valor absoluto es : ', num)

############################################################
animal =input('dime un animal : ')
if animal == 'perro':
    print('Guau')
elif animal == 'gato':
    print('Miau')
elif animal == 'vaca':
    print('muu')
else:
    print('no conosco su sonido')
print('conosco pocos animales')

############################################################
print('impares menores a 10')
x = 1
while x <= 10:
    print(x)
    x += 2

############################################################
factorial = 5
contador = factorial -1
while contador > 0:
    factorial *= contador
    contador -= 1
    #imprimir el factorial de 5 es ? resultado de la ejecucuin de while
    print(factorial , 'de 5' )

############################################################
for i in 1 , 2 , 3:
    print(i)

############################################################
for i in range(5):
    print(i)

############################################################
for i in ['ale','neil','andres',\
          'luis','rafa','luci']:
    print(i)

############################################################
for i in 'hola mundo':
    if i == 'm':
        pass
    else:
        print(i,end = '')
