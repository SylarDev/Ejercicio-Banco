"""
Cliente.py
"""
class Cliente:

    def __init__(self, nombre, apellido, dni, direccion, telefono, mail):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__direccion = direccion
        self. __telefono = telefono
        self.__mail = mail

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, value):
        self.__dni = value
    @dni.deleter
    def dni(self):
        del self.__dni

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, value):
        self.__direccion = value
    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self,value):
        self.__telefono = value
    @telefono.deleter
    def telefono(self):
        del self.__telefono
    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, value):
        self.__mail = value
    @mail.deleter
    def mail(self):
        del self.__mail

    

