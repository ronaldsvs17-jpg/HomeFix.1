class Usuario:
    def __init__(self, nombre, correo, telefono):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        if "@" in correo:
            self.__correo = correo
        else:
            raise ValueError("Correo no válido")

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def mostrar_datos(self):
        return {
            "nombre": self.__nombre,
            "correo": self.__correo,
            "telefono": self.__telefono
        }
