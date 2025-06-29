

#lista

clientes= [
    {'ID': 1, 'Ingreso': 10500, 'frecuencia': 5, 'estado': 'activo'},
    {'ID': 2, 'Ingreso':7800, 'frecuencia':2, 'estado':'activo' },
    {'ID': 3, 'Ingreso': 11200, 'frecuencia': 3, 'estado':'inactivo'},

]

for c in clientes:
        ingreso_valido = c['Ingreso'] >=10000
        frecuencia_valida = c['frecuencia'] >= 4
        estado_valido = c ['estado'] == 'activo'

        es_prioritario = ingreso_valido and frecuencia_valida and estado_valido


        print(f"\n Cliente {c['ID']}:")
        print(f'Ingreso suficiente: {ingreso_valido}')
        print (f'frecuencia suficiente: {frecuencia_valida}')
        print(f'Estado activo: {estado_valido}')
        print(f' ¿Es prioritario?: {es_prioritario}')