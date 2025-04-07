# Calculadora imc
# Definimos una funcion
def captura_nombre():
    # Se crea un ciclo, se repetira hasta que se cumpla la funcion
    while True:
          # Pide al usuario que ingrese su nombre 
          nombre = input("Su nombre, por favor: ")
          # verifica que los caracteres sean letras y espacios
          if not all(x.isalpha() or x.isspace() for x in nombre):
               # Si los caracteres no son letras y espacios muestra el mensaje de error
               print("Error: El nombre solo debe contener letras. Inténtalo de nuevo.")
          # Se repetira el ciclo
          else:
               # La captura se guarda en la variable, y se finaliza el ciclo
               return nombre
# Definimos una funcion
def captura_apellido():
     # Se crea un ciclo, se repetira hasta que se cumpla la funcion
     while True:
          # Pide al usuario que ingrese su apellido
          apellido = input("Su apellido, por favor: ")
          # verifica que los caracteres sean letras y espacios
          if not all(x.isalpha() or x.isspace() for x in apellido):
               # Si los caracteres no son letras y espacios muestra el mensaje de error
               print("Error: El apellido solo debe contener letras. Inténtalo de nuevo.")
          # Se repetira el ciclo
          else:
               # La captura se guarda en la variable, y se finaliza el ciclo
               return apellido

# Definimos una funcion
def captura_edad():
     # Se crea un ciclo, se repetira hasta que se cumpla la funcion
     while True:
          # Pide al usuario que ingrese su edad
          edad = input("Su edad, por favor: ")
          # verifica que los caracteres sean numeros
          if not edad.isdigit():
               # Si los caracteres no son numeros muestra el mensaje de error
               print("Error: La edad solo debe contener numeros. Inténtalo de nuevo.")
          # Se repetira el ciclo     
          else:
               # La captura se guarda en la variable, y se finaliza el ciclo
               return int(edad)

# Definimos una funcion
def captura_peso():
     # Se crea un ciclo, se repetira hasta que se cumpla la funcion
     while True:
          try:
               # Pide al usuario que ingrese su peso
               peso = float(input("Su peso, por favor: "))
               # La captura se guarda en la variable, y se finaliza el ciclo
               return peso
          # A ejecutar la ecepcion si devulve el error si iniciara el ciclo nuevamente
          except ValueError:
               # Si los caracteres no son numero y decimales mostarara el error
               print("Error: El peso solo debe contener números. Inténtalo de nuevo.")

# Definimos una funcion
def captura_altura():
     # Se crea un ciclo, se repetira hasta que se cumpla la funcion
     while True:
          try:
               # Pide al usuario que ingrese su altura
               altura = float(input("Su altura, por favor: "))
               # La captura se guarda en la variable, y se finaliza el ciclo
               return altura
          # A ejecutar la ecepcion si devulve el error si iniciara el ciclo nuevamente
          except ValueError:
               # Si los caracteres no son numero y decimales mostarara el error
               print("Error: La altura solo debe contener números. Inténtalo de nuevo.")

# Capturamos las entradas
nombre = captura_nombre()
apellido = captura_apellido()
edad = captura_edad()
peso = captura_peso()
altura = captura_altura()

# Calcular la masa corporal (IMC)
masacorporal = peso / (altura ** 2)

# Se imprimen los valores de varibles
print("Nombre: " + nombre + " " + apellido)
print("Edad: " + str(edad))
print("Peso: " + str(peso))
print("Altura: " + str(altura))
print("Tu masa corporal es de: " + str(masacorporal))

# Se clasifica el (IMC)
if masacorporal >= 0 and masacorporal <= 15.99 :
    print ("Delgadez severa")
elif masacorporal >= 16.00 and masacorporal <= 16.99 :
     print ("Delgadez moderada")
elif masacorporal >= 17.00 and masacorporal <= 18.99 :
     print ("Delgadez leve")
elif masacorporal >= 18.50 and masacorporal <= 24.99 :
     print ("Normal")
elif masacorporal >= 25.00 and masacorporal <= 29.99 :
     print ("Sobrepeso")
elif masacorporal >= 30.00 and masacorporal <= 34.99 :
     print ("obesidad leve")
elif masacorporal >= 35.00 and masacorporal <= 39.99 :
     print ("obesidad media")
else:
     print ("obesidad morbida")

