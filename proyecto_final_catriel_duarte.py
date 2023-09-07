"""
•	Parte 1
Resolver el siguiente ejercicio de programación
El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. 


En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa que calcule el sueldo promedio del empleado Juan. Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:

a. Sueldo bajo: por debajo de 300 dólares.
b. Sueldo normal:  entre 300 a 900.
c. Sueldo mejor de lo normal: más de 900 dólares.


Tip: se debe utilizar estructuras condicionales.

enero = 300
febrero = 300
marzo = 300
mayo = 300
abril = 300
junio = 300
julio = 500
agosto = 500
septiembre = 500
octubre = 500
noviembre = 700
diciembre = 700

"""


sueldo_juan = [300,300,300,300,300,500,500,500,700,700]


promedio_salarial = sum(sueldo_juan) / len(sueldo_juan)

if promedio_salarial < 300:
    print("Juan esta Cobrando un sueldo muy bajo")
elif promedio_salarial >= 300 and promedio_salarial <= 900:
    print("\nJuan persibe un sueldo en promedio normal")
else:
    print("Juan esta ganando un sueldo por arriba del promedio de los empleados")




print(f"sueldo promedio de: {promedio_salarial} dolares")
