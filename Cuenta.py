"""
Cuenta.py
"""
from Cliente import Cliente

class Cuenta(Cliente):
    def __init__(self, nombre, apellido, dni, direccion, telefono, mail,  numero, saldo):
        super().__init__(nombre, apellido, dni, direccion, telefono, mail)
        self.__numero = numero
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, value):
        self.__numero = value
    @numero.deleter
    def numero(self):
        del self.__numero

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        self.__saldo = value
    @saldo.deleter
    def saldo(self):
        del self.__saldo




