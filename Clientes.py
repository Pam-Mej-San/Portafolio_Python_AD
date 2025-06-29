
#Datos de clientes:

ingreso_mensual=9500
frecuenciade_uso= 3 #Estas son las visitas por mes
estado= 'activo'


#Regla de clasificación como 'Cliente prioritario'
es_prioritario= (ingreso_mensual >=10000 and frecuenciade_uso >=4) and estado == 'activo'

print('¿Es este cliente prioritario?', es_prioritario)



