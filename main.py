from Cliente import Cliente
from Banco import Banco
from Cuenta import Cuenta
import os, time, random

def main():
    nombreBanco = "Santander Rio"
    #creamos el objeto banco
    banco = Banco(nombreBanco)
    
    AGREGAR_CUENTA = 1
    ELIMINAR_CUENTA = 2
    LISTADO_CLIENTES_CON_MAS_CUENTAS = 3
    EXTRACCION = 4
    DEPOSITO = 5
    LISTADO_CUENTAS = 6
    LISTADO_CLIENTES = 7
    SALIR = 8
    CANT_CUENTA = 9
    CANT_CLIENTES = 10
    def menu():
        print(f"""  Bienvenido a: {banco.nombre}
            {AGREGAR_CUENTA}- Agregar una nueva cuenta.
            {ELIMINAR_CUENTA}- Eliminar una cuenta.
            {LISTADO_CLIENTES_CON_MAS_CUENTAS}- Listado de clientes con mas de una cuenta.
            {EXTRACCION}- Realizar una extraccion.
            {DEPOSITO}- Realizar un deposito.
            {LISTADO_CUENTAS}- Listado de cuentas.
            {LISTADO_CLIENTES}- Listado de clientes.
            {SALIR}- Salir.
            {CANT_CUENTA}- Cantidad de cuentas.
            {CANT_CLIENTES}- Cantidad de clientes.
            """)
        print("*" * 20)
        print("*" * 20)
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    opcion = menu()

    while opcion != SALIR:

        if opcion == AGREGAR_CUENTA:

            print("*" * 20)
            print("*" * 20)
            #print(f"Su numero de cuenta es {numeroCuenta}...")
            nombre = input("Ingrese nombre del cliente:")
            apellido = input("Ingrese apellido del cliente: ")
            dni = int(input("Ingres DNI del cliente: "))
            direccion = input("Ingrese direccion del cliente: ")
            telefono = int(input("Ingrese telefono del cliente: "))
            mail = input("Ingres mail del cliente: ")
            numeroCuenta = int(input("Ingrese el numero de la nueva cuenta: "))
            #for numeroDeCuenta in banco.listaClientes:
            #    if numeroDeCuenta == banco.listaClientes[numeroCuenta]:
            #        int(input(f"El numero de cuenta {numeroDeCuenta} ya existe. Ingrese otro numero: "))
            saldo = int(input("Ingrese el deposito inicial de la cuenta: "))

            # creamos la cuenta
            
            cliente = Cliente(nombre, apellido, dni, direccion, telefono, mail)
            cuenta = Cuenta(nombre, apellido, dni, direccion, telefono, mail, numeroCuenta, saldo)
            
            banco.agregarCliente(cliente, cuenta)
            
            
            print("*" * 20)
            print("*" * 20)
            opcion = menu()
            print("*" * 20)
            print("*" * 20)

        if opcion == ELIMINAR_CUENTA:
            if banco.listaDeCuentasVacia(): 
                banco.listaDeCuentasVacia()
                time.sleep(2)
                banco.listaDeClientesVacias()
                print("*" * 20)
                opcion = menu()
            else:
                numeroCuenta = int(input("Ingrese un numero de cuenta a eliminar: "))
                banco.bajaCuenta(numeroCuenta)
                time.sleep(2)
                opcion = menu()

        if opcion == LISTADO_CLIENTES_CON_MAS_CUENTAS:
            pass
        
        if opcion == EXTRACCION:
            if banco.listaDeCuentasVacia(): 
                banco.listaDeCuentasVacia()
                print("*" * 20)
                time.sleep(1)
                opcion = menu()
                print("*" * 20) 
            numeroDeCuenta = int(input("Ingrese numero de cuenta para la extraccion: "))
            monto = int(input("Ingrese el monto que desea extraer: "))
            banco.extraccionDeDinero(numeroCuenta, monto)
        
        if opcion == DEPOSITO:
            pass
        
            
        if opcion == LISTADO_CUENTAS:
            if banco.listaDeCuentasVacia():
                banco.listaDeCuentasVacia()
                print("*" * 20)
                time.sleep(1)
                opcion = menu()
                print("*" * 20) 
            else:
                banco.todasLasCuentas()
                print("*" * 20)
                time.sleep(1)
                opcion = menu()
                print("*" * 20)
        
        if opcion == LISTADO_CLIENTES:
            if banco.listaDeClientesVacias():
                banco.listaDeClientesVacias()
                print("*" * 20)
                time.sleep(1)
                opcion = menu()
                print("*" * 20) 
            else:
                banco.todosLosClientes()
                print("*" * 20)
                time.sleep(1)
                opcion = menu()
                print("*" * 20)     
        if opcion == CANT_CUENTA:
            banco.cantidadCuentas()
            print("*" * 20)
            time.sleep(1)
            opcion = menu()
        if opcion == CANT_CLIENTES:
            banco.cantidadDeClientes()
            print("*" * 20)
            time.sleep(1)
            opcion = menu()    
            
if __name__ == "__main__":
    main()
