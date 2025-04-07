# Tipos de varables
variable = 'Hola munndo'
print(variable)
# nos muestra el valor de la variable 

#tipos de datos
edad = 20 #int
altura = 1.5 #float
nombre = 'ana' #str / objeto
es_mayor = True # bool

print(edad,altura,nombre,es_mayor)

E1_nombre = 'Mauricio'
E1_edad = 30
print(f'{E1_nombre} tine {E1_edad} años.')

precio_producto = 25
descuento = 18

precio_final = precio_producto - (precio_producto * (descuento / 100))

print(f'El precio final del producto es {precio_final} pesos')

# nota
valor = '20'
print(type(valor))
valor = int(valor)
print(type(valor))

# Operadores de python
x = 10
y = 5
resultado =( x > y ) and ( y < 0 ) or not ( x == 10 )
print(resultado)

# if , elif y else
opcion = 'hamburgesa'

if opcion == 'pizza' :
    print('Voy a pedir pizza')
elif opcion == 'hamburgesa' :
    print('Voy a pedir hamburgesa')
else :
    print('Voy a pedir ensalada')

# for
for i in range(10) :
    print(f'entregando invitacion numero {i+1}')
# Resultado:
# entregando invitacion numero 1
# entregando invitacion numero 2
# entregando invitacion numero 3
# entregando invitacion numero 4
# entregando invitacion numero 5
# entregando invitacion numero 6
# entregando invitacion numero 7
# entregando invitacion numero 8
# entregando invitacion numero 9
# entregando invitacion numero 10

# While

dinero = 0
while dinero < 100 :
    dinero += 20 # Agregamos 20 cada vuelta 
    print(f'Ahora tengo ${dinero}')

# Resultado
# Ahora tengo $20
# Ahora tengo $40
# Ahora tengo $60
# Ahora tengo $80
# Ahora tengo $100
