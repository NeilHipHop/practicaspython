print('Impares menores a 10')

x = 1

while x <= 10 :
    print(x)
    x +=2

#####################################
factorial = 5
contador = factorial -1
while contador > 0:
    factorial *= contador
    contador -= 1

print('El factorial de 5 es : ', factorial)

######################################
for i in 1, 2, 3, :
    print (i)#imprime:  #1
                        #2
                        #3
 
for i in range(3) :
    print(i)# imprime   #0
                        #1
                        #2

######################################
for i in ['Ale', 'Neil','Ivan', 'Monse', 'Rafa', 'luca', 'Adolfo'] :
    print(i)

#####################################
for i in '!Hola¡ mundo' :
    if i == 'm' :
        pass
    else :
        print(i,end=" ")

#####################################
for i in range(2, 100):
    primo = True
    for j in range(2, i):
        if i == j :
            break
        elif i % j == 0 :
            primo = False

        else :
            continue

    if primo == True:
        print(i, end=" ")

