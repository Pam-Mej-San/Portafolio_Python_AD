#NOTA: Este ejercicio muestra cómo usar operadores de asignación para agregar
#  y transformar datos financieros de manera progresiva, 
# útil en contextos donde se trabaja con reportes periódicos.


ventas_trimestres=[250000,310000,295000, 330000]

#Proyección Acumulada

total_ventas=0
for trimestre in ventas_trimestres:
    total_ventas += trimestre

promedio_trimestral= total_ventas/ len(ventas_trimestres)

print('Ventas totales:', total_ventas)
print('Promedio Trimestral:', promedio_trimestral)


