class Reserva:
    def __init__(self, cliente, ciudad_origen, tour, cantidad_personas):
        self.cliente = cliente
        self.ciudad_origen = ciudad_origen
        self.tour = tour
        self.cantidad_personas = cantidad_personas

def registrar_reserva():
    cliente = input("Nombre y apellido del cliente: ")
    ciudad_origen = input("Ciudad de origen: ")
    tour = input("Detalle del tour (Torres del Paine, Carretera Austral o Chiloe): ")
    cantidad_personas = int(input("Cantidad de personas para el tour: "))
    return Reserva(cliente, ciudad_origen, tour, cantidad_personas)

def listar_reservas(reservas):
    print("\nReservas registradas:")
    for reserva in reservas:
        print(f"{reserva.cliente} ({reserva.ciudad_origen}) - {reserva.tour} ({reserva.cantidad_personas} personas)")

def imprimir_detalle_de_Reservas_por_destino(reservas):
    destino = input("Selecciona un destino (Torres del Paine, Carretera Austral o Chiloe): ")
    filename = f"{destino}_reservas.txt"
    with open(filename, "w") as file:
        for reserva in reservas:
            if reserva.tour == destino:
                file.write(f"{reserva.cliente} ({reserva.ciudad_origen}) - {reserva.cantidad_personas} personas\n")

def main():
    reservas = []
    while True:
        print("\n1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Imprimir Detalle de Reservas por Destino")
        print("4. Salir del Programa")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            reservas.append(registrar_reserva())
        elif opcion == "2":
            listar_reservas(reservas)
        elif opcion == "3":
            imprimir_detalle_de_Reservas_por_destino(reservas)
        elif opcion == "4":
            break
        else:
            print("Opcion invalida. Intentalo nuevamente.")

if __name__ == "__main__":
    main()
