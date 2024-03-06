class Alumno :
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = {}
        
    def add_asignatura(self, nombre_asignatura):
        self.asignaturas[nombre_asignatura] = {"nota": 0, "asistencia": 0}
        
    def nota(self, nombre_asignatura, nota):
        self.asignaturas[nombre_asignatura]["nota"] = nota
        
    def add_asistencia(self, nombre_asignatura, asistencia):
        self.asignaturas[nombre_asignatura]["asistencia"] = asistencia
        
    def promedio(self):
        suma_notas = 0
        for asignatura in self.asignaturas.values():
            suma_notas += asignatura["nota"]
        return suma_notas / len(self.asignaturas)
        
    def determinar_aprobado(self):
        for nombre_asignatura, asignatura in self.asignaturas.items():
            if asignatura["nota"] < 60:
                print(f"{self.nombre} ha reprobado la asignatura {nombre_asignatura}.")
                if asignatura["asistencia"] < 75:
                    print(f"Se recomienda aumentar la asistencia en {nombre_asignatura}.")
            else:
                if asignatura["asistencia"] >= 75 and self.promedio() >= 80:
                    print(f"{self.nombre} ha aprobado la asignatura {nombre_asignatura}.")
                    print(f"Se recomienda continuar con la asistencia y el esfuerzo en {nombre_asignatura}.")
                else:
                    print(f"{self.nombre} ha aprobado la asignatura {nombre_asignatura}.")
                    print(f"Se recomienda mantener el esfuerzo en {nombre_asignatura}.")
                    

# Programa principal
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
estudiante = Alumno(nombre_estudiante)

num_asignaturas = int(input("Ingrese el número de asignaturas: "))

for i in range(num_asignaturas):
    nombre_asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    estudiante.add_asignatura(nombre_asignatura)
    nota = int(input(f"Ingrese la nota de {nombre_asignatura}: "))
    estudiante.nota(nombre_asignatura, nota)
    asistencia = int(input(f"Ingrese el promedio de asistencia de {nombre_asignatura}: "))
    estudiante.add_asistencia(nombre_asignatura, asistencia)

estudiante.determinar_aprobado()