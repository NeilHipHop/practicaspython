tiempos = {
    'hamilton':'1:49.8',
    'botas':'1:56.4',
    'perez':'1:53.8',
    'verstappen':'1:52.6'
}

print(tiempos.items())
#dict_items([('hamilton', '1:49.8'), ('botas', '1:56.4'), ('perez', '1:53.8'), ('verstappen', '1:52.6')])

print(tiempos.keys())
#dict_keys(['hamilton', 'botas', 'perez', 'verstappen']) 

print(tiempos.values())
#dict_values(['1:49.8', '1:56.4', '1:53.8', '1:52.6'])

print(tiempos.get('hamilton'))
#1:49.8

print(tiempos.get('Hamilton','No encontrado'))
#No encontrado                  (si no encuentra el valor, muestra el mensaje de "no encontrado")
