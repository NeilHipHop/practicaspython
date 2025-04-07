# Calculadora basica
# Pide la operacionque desa realizar
operacion = input('¿Que operacion quiere realiza R: /,*,-,//,%,** o + ? R: ')
# Pide el primer numero
n1 = float(input('Introduce primer numero R: '))
# Pide el segundo numero
n2 = float(input('Introduce el segundo numero R: '))

if operacion == '/' :
    if n1 == 0 or n2 == 0 :
        print('Evite la divicion entre 0')
    else :
        print(n1 / n2)
elif operacion == '*' :
    print(n1 * n2)
elif operacion == '-' :
    print(n1 - n2)
elif operacion == '+' :
    print(n1 + n2)
elif operacion == '**' :
    print(n1 ** n2)
elif operacion == '%' :
    print(n1 % n2)
elif operacion == '//' :
    print(n1 // n2)
  
















