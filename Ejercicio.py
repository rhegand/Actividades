class Llamada:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad

class Cola_Prioridad:
    def __init__(self):
        self.cola = []

    def ingresar_llamada(self, llamada):
        if llamada.gravedad == 1:
            self.cola.insert(0, llamada)
        elif llamada.gravedad == 5:
            self.cola.append(llamada)
        else:
            # Buscar posición según prioridad
            posicion = 0
            for i, llam in enumerate(self.cola):
                if llam.gravedad > llamada.gravedad:
                    posicion = i
                    break
                elif llam.gravedad == llamada.gravedad:
                    if llam.edad < llamada.edad:
                        posicion = i
                        break
            self.cola.insert(posicion, llamada)

    def Siguiente_llamada(self):
        if self.cola:
            llamada = self.cola.pop(0)
            print("Siguiente solicitud a atender:")
            self.mostrar_llamada(llamada)
        else:
            print("No hay solicitudes pendientes.")

    def mostrar_cola(self):
        if self.cola:
            print("Cola de atención:")
            for i, llamada in enumerate(self.cola, 1):
                print(f"Posición {i}:")
                self.mostrar_llamada(llamada)
        else:
            print("No hay solicitudes pendientes.")

    def mostrar_llamada(self, llamada):
        print(f"Nombre: {llamada.nombre}")
        print(f"Edad: {llamada.edad}")
        print(f"Dirección: {llamada.direccion}")
        print(f"Motivo: {llamada.motivo}")
        print(f"Gravedad: {llamada.gravedad}")
        if llamada.gravedad == 1:
            print("Prioridad: Unidad de refuerzo (máxima)")
        elif llamada.gravedad == 5:
            print("Prioridad: Unidad móvil motorizada (baja)")
        else:
            if llamada.edad < 12:
                print("Prioridad: Niño")
            elif llamada.edad >= 65:
                print("Prioridad: Adulto mayor")
            else:
                print("Prioridad: Adulto")
        print("")


def main():
    Cola = Cola_Prioridad()
    while True:
        print("\nMenú:")
        print("1. Ingresar Llamada")
        print("2. Pasar Siguiente_llamada solicitud")
        print("3. Mostrar la cola")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")
        print("")

        if opcion == "1":
            nombre = input("Nombre completo: ")
            edad = int(input("Edad: "))
            direccion = input("Dirección: ")
            motivo = input("Motivo de la llamada: ")
            gravedad = int(input("Gravedad (1-5): "))

            llamada = Llamada(nombre, edad, direccion, motivo, gravedad)
            Cola.ingresar_llamada(llamada)
            print("Llamada ingresada correctamente.")

        elif opcion == "2":
            Cola.Siguiente_llamada()

        elif opcion == "3":
            Cola.mostrar_cola()

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
