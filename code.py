 """
Se requiere contratar de tus servicios de informática para el desarrollo de un
proyecto en Python para la venta de sus pasajes, el sistema es bastante simple, lo primero que
hay que tener en cuenta es que son en total 41 asientos por avión, como se ve a continuación:
Donde desde el asiento 31 al 42 se consideran asientos para pasajeros vip.
Los precios de un asiento normal son de $78.900, mientras que los de un asiento vip son
de $240.000.
El sistema deberá permitir al usuario seleccionar un asiento disponible (mostrando los
asientos disponibles) e indicar el valor, una vez que el usuario acepte, deberá solicitar
los datos del usuario, en los cuales tenemos nombrePasajero, rutPasajero,
telefonoPasajero y bancoPasajero, además, el sistema deberá implementar el siguiente
menú:
1. Ver asientos disponibles
2. Comprar asiento
3. Anular vuelo
4. Modificar datos de pasajero
5. Salir
"""
class Avion:
    def __init__(self):
        self.asientos = {i: 'Disponible' for i in range(1, 43)}

    def ver_asientos_disponibles(self):
        print("Asientos disponibles:")
        for asiento, estado in self.asientos.items():
            print(f"Asiento {asiento}: {estado}")

    def comprar_asiento(self, num_asiento, tipo_pasajero):
        if 1 <= num_asiento <= 42 and self.asientos[num_asiento] == 'Disponible':
            if 31 <= num_asiento <= 42 and tipo_pasajero == 'vip':
                precio = 240000
            else:
                precio = 78900

            print(f"El precio del asiento es: ${precio}")
            confirmacion = input("¿Desea comprar este asiento? (S/N): ").upper()
            if confirmacion == 'S':
                self.asientos[num_asiento] = 'Ocupado'
                nombre = input("Ingrese el nombre del pasajero: ")
                rut = input("Ingrese el RUT del pasajero: ")
                telefono = input("Ingrese el teléfono del pasajero: ")
                banco = input("Ingrese el banco del pasajero: ")
                print("Compra realizada con éxito.")
                return True
            else:
                print("Compra cancelada.")
        else:
            print("El asiento seleccionado no está disponible.")
        return False

    def anular_vuelo(self, num_asiento):
        if 1 <= num_asiento <= 42 and self.asientos[num_asiento] == 'Ocupado':
            confirmacion = input("¿Está seguro que desea anular el vuelo para este asiento? (S/N): ").upper()
            if confirmacion == 'S':
                self.asientos[num_asiento] = 'Disponible'
                print("Anulación realizada con éxito.")
                return True
            else:
                print("Anulación cancelada.")
        else:
            print("No se puede anular el vuelo para este asiento.")
        return False

    def modificar_datos_pasajero(self, num_asiento):
        if 1 <= num_asiento <= 42 and self.asientos[num_asiento] == 'Ocupado':
            nombre = input("Ingrese el nuevo nombre del pasajero: ")
            rut = input("Ingrese el nuevo RUT del pasajero: ")
            telefono = input("Ingrese el nuevo teléfono del pasajero: ")
            banco = input("Ingrese el nuevo banco del pasajero: ")
            print("Datos modificados con éxito.")
            return True
        else:
            print("No se pueden modificar los datos para este asiento.")
        return False
def main():
    avion = Avion()

    while True:
        print("\nMenú:")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            avion.ver_asientos_disponibles()
        elif opcion == '2':
            num_asiento = int(input("Ingrese el número de asiento que desea comprar: "))
            tipo_pasajero = input("Ingrese el tipo de pasajero ('vip' o 'regular'): ")
            avion.comprar_asiento(num_asiento, tipo_pasajero)


        elif opcion == '3':
            num_asiento = int(input("Ingrese el número de asiento que desea anular: "))
            avion.anular_vuelo(num_asiento)
        elif opcion == '4':
            num_asiento = int(input("Ingrese el número de asiento cuyos datos desea modificar: "))
            avion.modificar_datos_pasajero(num_asiento)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
