nombrecurso= ('Ultimate python')

print(nombrecurso[0:8])
print(nombrecurso[0])
print(nombrecurso[7:0])
print(nombrecurso[:8])

#Variables y string
nombre= 'Pamela'
segundo='Rocío'
apellido= 'Mejía'
appellido2='Sánchez'

nombre_complet0=(f'{nombre} {apellido} {appellido2}')
print(nombre_complet0)


perro= ' Mafalda, Daisy, Molly'


#Método de strings
#índice
print(perro.upper())
print(perro.lower())
print(perro.capitalize())
print(perro.title())
print(perro.strip())
print(perro.strip().upper())
print(perro.strip().capitalize())
print(perro.lstrip())
print(perro.rstrip())
print(perro.find('Falda')) #Número negativo no se pudo encontrar, no existe
print(perro.find('falda'))  #Número positivo, se encontró
print(perro.replace('ll','li'))


#Boleano
print('Mafalda' in perro)
print('Mafalda' not in perro)







