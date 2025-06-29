#NOTA: Este script calcula KPIs esenciales para evaluar el desempeño financiero de una empresa
#  a partir de datos anuales. Estos cálculos son útiles para reportes ejecutivos o dashboards 
# de rendimiento.


#Datos

ventas_2024 = 1_200_000
ventas_2023= 1_000_000
costos= 680_000
empleados= 12


#Métricas

ingreso_neto = ventas_2024-costos
crecimiento=((ventas_2024-ventas_2023)/ ventas_2023)*100
rendimiento_empleado= ingreso_neto/empleados


#Resultados

print('Ingreso Neto:', ingreso_neto)
print('Crecimiento anual (%):', round (crecimiento,2))
print('Ingreso Neto por empleado:', round (rendimiento_empleado,2))





