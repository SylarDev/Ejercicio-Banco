"""
Banco.py
"""

class Banco:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__listaClientes = []
        self.__listaCuentas = []

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
    def listaClientes(self):
        return self.__listaClientes

    @listaClientes.setter
    def listaClientes(self, value):
        self.__listaClientes = value

    @listaClientes.deleter
    def listaClientes(self):
        del self.__listaClientes

    @property
    def listaCuentas(self):
        return self.__listaCuentas

    @listaCuentas.setter
    def listaCuentas(self, value):
        self.__listaCuentas = value

    @listaCuentas.deleter
    def listaCuentas(self):
        del self.__listaCuentas

    #metodos para los clientes
    #############################
    ##############################
    def agregarCliente(self, cliente, cuenta):
        self.__listaClientes.append(cliente)
        self.__listaCuentas.append(cuenta)

    #eliminamos un cliente por su dni
    def eliminarCliente(self, dni):
        for cliente in self.__listaClientes:
            if dni == cliente.dni:
                self.__listaClientes.remove(cliente)
                print(f"El cliente: {cliente.dni} ha sido borrado con exito.")
                break
        else:
            print(f"El DNI: {dni} no es cliente del banco.")

    def cantidadDeClientes(self):
         print("La cantidad de clientes es de: ", len(self.__listaClientes))

    def verCliente(self, dni):
        for cliente in self.__listaClientes:
            if dni == cliente.dni:
                print(f"""Nombre: {cliente.nombre}
Apellido: {cliente.apellido}
DNI: {cliente.dni}
Direccion: {cliente.direccion}
Telefono: {cliente.telefono}
Mail: {cliente.mail}              
""")
    def todosLosClientes(self):
        print("Listado completo de clientes")
        print("*"*20)
        for cliente in self.__listaClientes:
            print(f"""Nombre: {cliente.nombre}
Apellido: {cliente.apellido}
DNI: {cliente.dni}
Direccion: {cliente.direccion}
Telefono: {cliente.telefono}
Mail: {cliente.mail}              
""")
            print("*" * 20)

    def esCliente(self, dni):
        for cliente in self.__listaClientes:
            if dni == cliente.dni:
                print(f"El DNI: {cliente.dni} es cliente del banco. ")
                break
        else:
            print(f"El DNI: {dni} no es cliente del banco {self.__nombre}")

    def listaDeCuentasVacia(self):
        if len(self.__listaCuentas ) == 0:
            print("*" * 20)
            print("La lista de cuentas esta vacia.")
            print("*" * 20)
            return True
        else: 
            return False
    
    def listaDeClientesVacias(self):       
        if len(self.__listaClientes) == 0:
            print("*" * 20)
            print("La lista de clientes esta vacia.")
            print("*" * 20)
            return True
        else:
            return False
    ##Metodos para el manejo de cuentas
    #############################
    #############################
    
    def validacionAltaCuenta(self):
        for cuenta in self.__listaCuentas:
            if cuenta == cuenta.numero:
                print(f"La cuenta numero: {cuenta} ya existe.")
                self.listaCuentas.remove(cuenta)
                #self.__listaClientes.remove()
                return True

    def bajaCuenta(self, numero):
        for cuenta in self.__listaCuentas:
            if numero == cuenta.numero:
                self.__listaCuentas.remove(cuenta)
                print(f"La cuenta {cuenta.numero} ha sido dada de baja con exito.")
    
    def depositar(self, numeroDeCuenta, monto):
        for cuenta in self.__listaCuentas:
            if numeroDeCuenta == cuenta.numero:
                cuenta.saldo = monto + cuenta.saldo
                print(f"El saldo ha sido actualizado con exito.")
                print(f"Su nuevo saldo es {cuenta.saldo} pesos.")
                break
    
    def extraccionDeDinero(self, numeroCuenta, monto):
        for cuenta in self.__listaCuentas:
            if numeroCuenta == cuenta.numero:
                if monto > cuenta.saldo or cuenta.saldo == 0:
                    print("Su saldo es insuficiente para una extraccion.")
                    break
                cuenta.saldo = cuenta.saldo - monto
                print(f"El saldo ha sido actualizado con exito.")
                print(f"Su nuevo saldo es {cuenta.saldo} pesos")
                break

    def cantidadCuentas(self):
        print(f"La cantidad de cuentas es: ", len(self.__listaCuentas))

    def verCuenta(self, numeroDeCuenta):
        for cuenta in self.__listaCuentas:
            if numeroDeCuenta == cuenta.numero:
                print(f"""Nombre: {cuenta.nombre}
Apellido: {cuenta.apellido}
DNI: {cuenta.dni}
Numero de cuenta: {cuenta.numero}
Saldo: {cuenta.saldo}              
""")

    def todasLasCuentas(self):
        print("Listado completo de cuentas")
        print("*" * 20)
        for cuenta in self.__listaCuentas:
            print(f"""Nombre: {cuenta.nombre}
Apellido: {cuenta.apellido}
DNI: {cuenta.dni}
Numero de cuenta: {cuenta.numero}
Saldo: {cuenta.saldo}              
""")

    def verSaldo(self, numeroCuenta):
        for cuenta in self.__listaCuentas:
            if numeroCuenta == cuenta.numero:
                print(f"La cuenta {cuenta.numero} presenta un saldo de {cuenta.saldo} pesos")

   
        