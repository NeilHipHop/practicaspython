# Calculadora de IMC

## Descripción

Este proyecto es una calculadora de Índice de Masa Corporal (IMC) que permite a los usuarios ingresar su nombre, apellido, edad, peso y altura, y luego calcula su IMC. Basado en el valor del IMC, la calculadora clasifica el estado de salud del usuario en diferentes categorías.

## Funcionalidades

- Captura de nombre y apellido, asegurando que solo contengan letras y espacios.
- Captura de edad, asegurando que solo contenga números.
- Captura de peso y altura, asegurando que solo contengan números y decimales.
- Cálculo del IMC basado en el peso y la altura del usuario.
- Clasificación del IMC en diferentes categorías de salud.

## Uso

Para usar la calculadora de IMC, simplemente ejecuta el script y sigue las instrucciones para ingresar tu información personal. El script calculará tu IMC y te proporcionará una clasificación basada en el valor calculado.

## Ejemplo de uso

```python
# Capturamos las entradas
nombre = captura_nombre()
apellido = captura_apellido()
edad = captura_edad()
peso = captura_peso()
altura = captura_altura()

# Calcular la masa corporal (IMC)
masacorporal = peso / (altura ** 2)

# Se imprimen los valores de variables
print("Nombre: " + nombre + " " + apellido)
print("Edad: " + str(edad))
print("Peso: " + str(peso))
print("Altura: " + str(altura))
print("Tu masa corporal es de: " + str(masacorporal))

# Se clasifica el IMC
if masacorporal >= 0 and masacorporal <= 15.99:
    print("Delgadez severa")
elif masacorporal >= 16.00 and masacorporal <= 16.99:
    print("Delgadez moderada")
elif masacorporal >= 17.00 and masacorporal <= 18.99:
    print("Delgadez leve")
elif masacorporal >= 18.50 and masacorporal <= 24.99:
    print("Normal")
elif masacorporal >= 25.00 and masacorporal <= 29.99:
    print("Sobrepeso")
elif masacorporal >= 30.00 and masacorporal <= 34.99:
    print("Obesidad leve")
elif masacorporal >= 35.00 and masacorporal <= 39.99:
    print("Obesidad media")
else:
    print("Obesidad mórbida")