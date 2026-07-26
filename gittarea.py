from functools import reduce

estudiantes = (
    ("Ana Torres",     (8.5, 7.0, 9.0)),
    ("Luis Campos", (6.0, 5.5, 6.5)),
    ("Marta Rios",     (9.5, 9.0, 10.0)),
    ("Pedro Salas",    (4.0, 5.0, 3.5)),
    ("Sofia Vera",     (7.0, 7.5, 8.0)),
    ("Marco Moreira",  (5.5, 7.0, 5.0)),
)
 
NOTAMIN = 7.0

def promedio(notas: tuple) -> float:
    suma = reduce(lambda acumulado, nota: acumulado + nota, notas, 0)
    return round(suma / len(notas), 2)
 
 
def obtener_nombre(estudiante: tuple) -> str:
    return estudiante[0]
 
 
def obtener_notas(estudiante: tuple) -> tuple:
    return estudiante[1]
 
 
def estado(promedio_estudiante: float, nota_min: float = NOTAMIN) -> str:
    evaluar = lambda p: "Aprobado" if p >= nota_min else "Reprobado"
    return evaluar(promedio_estudiante)

def calcular_promedios(lista_estudiantes: tuple) -> tuple:
    nombres = map(obtener_nombre, lista_estudiantes)
    notas = map(obtener_notas, lista_estudiantes)
    promedios = map(promedio, notas)
    return tuple(zip(nombres, promedios))
 
 
def genreporte(promedios: tuple) -> tuple:
    return tuple(
        map(lambda par: (par[0], par[1], estado(par[1])), promedios)
    )
 
 
def filtrar_por_estado(reporte: tuple, estado: str) -> tuple:
    return tuple(filter(lambda registro: registro[2] == estado, reporte))
 
 
def promedio_general(reporte: tuple) -> float:
    suma_total = reduce(lambda acc, registro: acc + registro[1], reporte, 0)
    return round(suma_total / len(reporte), 2)
 
 
def mejor_estudiante(reporte: tuple) -> tuple:
    return reduce(
        lambda mejor, actual: actual if actual[1] > mejor[1] else mejor,
        reporte,
    )
 
 
def aplicar_funcion(dato, funcion):
    return funcion(dato)

def formatear_registro(registro: tuple) -> str:
    nombre, prom, estado = registro
    return f"{nombre:<18} | Promedio: {prom:>5} | Estado: {estado}"
 
 
def imprimir_lista(titulo: str, lista: tuple) -> None:
    print(f"\n{titulo}")
    print("-" * 55)
    tuple(map(lambda registro: print(formatear_registro(registro)), lista))
 

 
def main():
    promedios = calcular_promedios(estudiantes)
    reporte = genreporte(promedios)
 
    aprobados = filtrar_por_estado(reporte, "Aprobado")
    reprobados = filtrar_por_estado(reporte, "Reprobado")
 
    imprimir_lista("REPORTE GENERAL DE CALIFICACIONES", reporte)
    imprimir_lista("ESTUDIANTES APROBADOS", aprobados)
    imprimir_lista("ESTUDIANTES REPROBADOS", reprobados)
 
    print("\nESTADISTICAS DEL CURSO")
    print("-" * 55)
    print(f"Promedio general del curso : {promedio_general(reporte)}")
    print(f"Total aprobados             : {len(aprobados)}")
    print(f"Total reprobados            : {len(reprobados)}")
 
    mejor = mejor_estudiante(reporte)
    print(f"Mejor promedio              : {mejor[0]} ({mejor[1]})")
 
    
 
if __name__ == "__main__":
    main()
