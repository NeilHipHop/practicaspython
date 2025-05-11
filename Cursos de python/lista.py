mix = [0, 1.0, 'dos', 3 + 4j]
t = 0


t += 1
print('Trabajo : ',t, '''
''')

for i in mix :
    print(f'{i:6} - Tipo: {type(i)}')


t += 1
print('Trabajo : ',t, '''
''')

print(len(mix))


t += 1
print('Trabajo : ',t, '''
''')

sin_dos = mix[:2] + mix[3:]
print(mix, sin_dos)

t += 1
print('Trabajo : ',t, '''
''')
duplicado = mix *2
print(duplicado)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados =[0, 1, 4, 9, 16, 25]
for i in range(len(cuadrados)) :
    print(f'{i}**2 = {cuadrados[i]}')

t += 1
print('Trabajo : ',t, '''
''')
cuadrados =[0, 1, 4, 9, 16, 25]
for i in range(len(cuadrados)) :
    cuadrados[i] =cuadrados[i] * i
    print(f'Ahora estan al cubo {cuadrados[i]}')

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.append(7 ** 3)
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.insert(6, 6 ** 3)
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.extend([27, 1000, -1])
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.extend(range(-1, -4, -1))
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
del cuadrados [9:]
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.remove(27)
print(cuadrados)

t += 1
print('Trabajo : ',t, '''
''')
valor_removido = cuadrados.pop(2)
print(valor_removido)

t += 1
print('Trabajo : ',t, '''
''')
cuadrados.clear()
print(cuadrados)
