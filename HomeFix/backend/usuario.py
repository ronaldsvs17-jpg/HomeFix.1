# ==========================
# ABSTRACCIÓN
# ==========================
from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, correo):
        # ==========================
        # ENCAPSULACIÓN
        # ==========================
        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    @abstractmethod
    def mostrar_rol(self):
        pass


# ==========================
# HERENCIA
# ==========================
class Trabajador(Usuario):
    def __init__(self, nombre, correo, especialidad):
        super().__init__(nombre, correo)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Trabajador de HomeFix - Especialidad: {self.especialidad}"


class Empleador(Usuario):
    def __init__(self, nombre, correo, servicio):
        super().__init__(nombre, correo)
        self.servicio = servicio

    def mostrar_rol(self):
        return f"Empleador - Busca servicio de {self.servicio}"


# ==========================
# POLIMORFISMO
# ==========================
usuarios = [
    Trabajador("Juan Pérez", "juan@homefix.com", "Plomería"),
    Empleador("Ana López", "ana@homefix.com", "Electricidad")
]

for usuario in usuarios:
    print("Nombre:", usuario.get_nombre())
    print(usuario.mostrar_rol())
    print("-" * 40)
