import Profesor
import Alumno
class Escuela:#Clase Escuela

    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.alumnos = []
        self.profesores = []

    def eliminarAlumno(self, nombre):
        alumno = [s for s in self.alumnos if s.nombre == nombre]
        self.alumnos.remove(alumno[0])

    def añadirAlumno(self, nombre, curso, profesor):
        alumno = Alumno.Alumno(nombre, curso, profesor)
        self.alumnos.append(alumno)

    def eliminarProfesor(self, profesor):
        print(f"La matrícula del coche es {self.matrícula} y su color es {self.color}")

    def añadirProfesor(self, nombre, tipo):
        profesor = Profesor.Profesor(nombre, tipo)
        self.profesores.append(profesor)