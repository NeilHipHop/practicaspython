# Utilizar for para separar en una paalabra o cadena por renglon 

texto = 'Aprendiendo Python'
for letra in texto:
    print(letra)

# upper() combiete todo el texto a mayusculas

texto = texto.upper()
print(texto)

# split() separa las palabras en un arreglo en una cadena de texto

texto = texto.split()
print(texto)

# remplasar palabra con replace(texto original, nuevo texto)

frace = 'Aprendiendo python'
nuevo_texto = frace.replace('Aprendiendo','estudiando')
print(nuevo_texto)

# Ocurrrencias de una ltra en un string

tex1 = 'Bananas'
tex2 = 'a'
conteo = tex1.count(tex2)
print(f"La letra '{tex2}' aparce {conteo} veces")

# invertir cadenas

texto1 ='anita lava la tina'
invertido = texto1 [::-1]
print(invertido) 

# lista []

frutas = ['manzanas','banana','ceresa']
frutas.append('naranja') #agregar
print(frutas)

# tuplas ()

colores =('rojo','verde','azul')
print(colores[1] ) 

#colores.append('amarillo')   # Error, no se pueden modificar


