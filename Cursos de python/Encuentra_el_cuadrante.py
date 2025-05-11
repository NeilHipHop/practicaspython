#Crear un programa que en base a 2 números de 
#entrada, coordenadas, identifique en cuál de los 
#4 cuadrantes se encuentra el punto. 
#El programa debe verificar que ninguna coordenada sea 0.

#Pide que introduscas el valor de eje "X"
x = int (input ('Ingresa el valor de x: '))
#Pide que introduscas el valor de eje "Y"
y = int (input ('Ingresa el valor de y: '))
# Si el aje "X","Y" o ambos arrojara un mensaje de error
if x==0 and y==0:
    #Mensaje de error
    print ('Punto de Origen "X" y "Y" no puede ser cero')
elif x==0:
    #Mensaje de error
    print ('Punto de Origen "X" no puede ser cero')
elif y==0:
    #Mensaje de error
    print ('Punto de Origen "Y" no puede ser cero')
#Si el eje "X" y "Y" son mayores a "0" pertenecen al cuadrante 1
if x>0 and y>0:
    #Muestra el mensaje del cuadrante
    print ('Cuadrante I')
#Si el eje "X" es menor a "0" y "Y" es mayores a "0" pertenecen al cuadrante 2
if x<0 and y>0:
    #Muestra el mensaje del cuadrante
    print ('Cuadrante II')
#Si el eje "X" es menor a "0" y "Y" es menor a "0" pertenecen al cuadrante 3
if x<0 and y<0:
    #Muestra el mensaje del cuadrante
    print ('Cuadrante III')
#Si el eje "X" es mayor a "0" y "Y" es menor a "0" pertenecen al cuadrante 4
if x>0 and y<0:
    #Muestra el mensaje del cuadrante
    print ('Cuadrante IV')
#Muestra los valores de las variables "X" y "Y"
print ('X',x,'Y',y)
