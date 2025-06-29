
#Criterios


compras_mensuales= 12000
frecuencia_visitas=6 #veces al mes


#Clientes

clientes = [
    {'ID':1 , 'Compras':13000, 'Frecuencia': 8, 'estado' : 'activo' },
    {'ID': 2, 'Compras': 7800, 'Frecuencia': 2, 'estado': 'activo'},
    {'ID': 3, 'Compras': 11200, 'Frecuencia': 6, 'estado': 'inactivo'}
]



#reglas


for c in clientes:
    es_VIP = (c['Compras']> 10000 or c['Frecuencia'] > 8)


    print(f'\n¿Es cliente VIP?', es_VIP)
    print(f"Compras: {c['Compras']}")
    print(f"Frecuencia: {c['Frecuencia']}")
    print(f"Estado: {c['estado']}")
    print(f'¿Es VIP? {es_VIP}\n')




