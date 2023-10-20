from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia


    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"    

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_incripcion):
        super.__init__(self, nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion = anio_incripcion
        self.mis_cursos = []

    def matricularse_en_curso(self, curso, contrasenia_matriculacion):
        if curso.carrera == self.carrera:
            if curso not in self.mi_cursos and curso.contrasenia_matriculacion == contrasenia_matriculacion:
                self.mi_cursos.append(curso)
                return True
        return False

    def desmatricularse_de_curso(self, curso):
        if curso in self.mi_cursos:
            self.mi_cursos.remove(curso)

    def ver_cursos_matriculados(self):
        return self.mi_cursos    
    
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super.__init__(self, nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def dictar_curso(self, nombre_curso, carrera):
        if carrera == self.carrera:
            contrasenia_matriculacion = self.generar_contrasenia()
            curso = Curso(nombre_curso, carrera, contrasenia_matriculacion)
            self.mis_cursos.append(curso)
            return curso

    def ver_cursos_dictados(self):
        return self.mis_cursos    


class Curso():
    def __init__(self, nombre, contrasenia_matriculacion):
        self.nombre = nombre
        self.contrasenia_matriculacion = contrasenia_matriculacion
        self.estudiantes = []
        self.profesor = []

    

