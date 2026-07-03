"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(ventas)
def calcular_promedio(lista_ventas):
    """ Retorna el promedio de las ventas de la lista ventas"""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_promedio_emprendimiento(total_emprendimiento):
    """ Retorna el promedio del emprendimiento"""
    return total_emprendimiento / meta * 100

def calcular_clasificacion(porcentaje_logro):
    """"Clasifica el emprendimiento según porcentaje de cumplimiento de meta de ventas."""
    if porcentaje_logro >= 100:
        clasificacion_empredimiento = "Meta alcanzada, emprendimeinto rentable"
    elif porcentaje_logro >= 80:
        clasificacion_empredimiento = "Observación, no se logró la meta."
    else:
        clasificacion_empredimiento = "ADVERTENCIA, problemas de rentabilidad. URGE ATENCIÓN."
    return clasificacion_empredimiento
def imprimir_reporte(reporte):
    """Imprime el reorte final de ventas por emprendimiento"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    for fila in reporte:
        print(f"Empredimiento: {fila["nombre"].upper()}")
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        
        print(f"Total semanal: ₡{fila["total"]:,.2f}")
        print(f"Promedio diario: ₡{fila["promedio"]:,.2f}")
        print(f"Porcentaje cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Estado: {fila["estado"]}")
        print("-" * 60)
    print(f"Cantidad de emprendimientos: {len(reporte)}")
print("sedes:", len(sedes))
print(type(sedes), "vrs", type(sedes[0]))
print("Datos por sede: ", sedes[0].keys())
print("\nPrimer emprendimiento:", sedes[0]["nombre"])



emprendimiento= sedes[0] 
ventas = emprendimiento["ventas"]
meta = emprendimiento["meta"]

reporte = []
provincia = set()


for emprendimiento in sedes:
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

    total_emprendimiento = calcular_total(ventas)
    promedio_emprendimiento = calcular_promedio_emprendimiento(total_emprendimiento)
    promedio_diario = calcular_promedio(ventas)
    clasificacion = calcular_clasificacion(promedio_emprendimiento)

    provincia.add(emprendimiento["provincia"])
    print("\nEmprendimiento:", emprendimiento["nombre"])

    print("Total Ventas: ", total_emprendimiento)
    print("Porcentaje: ", promedio_emprendimiento)
    print("Promedio diario: ", promedio_diario)
print(provincia)


reporte.append(
        {
            "nombre": emprendimiento["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_emprendimiento,
            "promedio": promedio_diario,
            "porcentaje": promedio_emprendimiento,
            "estado": clasificacion
            
        }
    )
imprimir_reporte(reporte)
print(provincia)
