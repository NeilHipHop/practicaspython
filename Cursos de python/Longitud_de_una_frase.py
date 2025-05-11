# Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. 
# toma en cuenta las siguientes consideraciones:
# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras,
# se debe imprimir un mensaje que indique que la palabra es correcta.
# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga:
# “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga:
# “Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

palabra = input("Introduce una palabra: ")
n = 0
#La palabra correcta debe tener entre cuatro y ocho letras.
if len(palabra) > 3:
    if len(palabra) < 9:
        #la palabra es correcta.
        print('La palbra es correcta')
#Si la palabra tiene menos de 4 letras        
if len(palabra) < 4:
    #Se le asigna a "n" el numero de carateres
    n = len(palabra)
    #Mensaje de error si contiene manos de 4 letras
    print('Hacen falta letras. Solo tiene', n,'letras')
#Si la palabra tiene más de 8 letras
if len(palabra) > 8:
    #Se le asigna a "n" el numero de carateres
    n = len(palabra)
    #mensaje de error si contiene mas de 8 letras
    print('Sobran letras. Tiene', n,'letras')
