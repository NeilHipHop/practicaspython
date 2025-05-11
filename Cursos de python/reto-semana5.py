entrada = input('¡ Hola ! Introduce tu edad: ')

edad = 0

if entrada.isnumeric():
    edad = int(entrada)

else :
    print('Dato incorrecto. Debes introducir un numero')
    exit()

if edad <= 0 :
    print("¡Woooww! Que joven eres. Pero, lo siento, pero eso no es posible")
elif edad > 115 :
    print('Vaya !!!! ¿Como le haces para vivir tanto? No te creo, mejor intenta de nuevo')
elif edad < 18 :
    print('Eres menor de edad asi que no puedes comprar cigarros')
else :
    print('Eres mayor de edad. Aqui tienes tus cigarros')
