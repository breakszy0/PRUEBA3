"""
Estimado/a estudiante,
Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
La empresa de tours y expediciones “SurExplora” necesita desarrollar un sistema que permita registrar las reservas de sus
clientes para sus tours en la Patagonia Chilena. Para el funcionamiento del sistema se requiere las siguientes funcionalidades:

1. Registrar Reserva

2. Listar Todas las Reservas

3. Imprimir Detalle de Reservas por Destino


4. Salir del Programa
Registrar Reserva Para registrar una reserva se requiere lo siguiente: Nombre y apellido del cliente, ciudad de origen, detalle del
tour. Por ejemplo, la empresa ofrece tours a Torres del Paine, Carretera Austral y Chiloé. Debe permitir seleccionar entre 1 de las
3 opciones e ingresar la cantidad de personas para el tour. Por lo tanto, un detalle de reserva podría verse registrado de la

siguiente manera:




Cliente Ciudad de Origen Tour Cantidad de Personas

Juan Pérez Santiago Torres del Paine 2
María López Valdivia Chiloé 3
Debe validar que todos los datos sean ingresados.



Listar Reservas Debe mostrar en la pantalla la lista de todas las reservas realizadas similar al ejemplo anterior de registro de
reservas.


Imprimir Detalle de Reservas por Destino Para imprimir el detalle de reservas, el usuario debe seleccionar alguno de los destinos
donde es posible realizar un tour. Estos destinos deben estar previamente definidos en algún tipo de colección de Python en el
código y por lo menos deben ser tres. Por ejemplo: Torres del Paine, Carretera Austral, Chiloé. Al seleccionar uno de los destinos,
se generará un archivo de texto (.txt) con el detalle de las reservas que se deberá llevar a ese destino. Este debe tener la misma




forma del registro completo de las opciones anteriores pero en archivo de texto.
Salir del Programa El programa debe funcionar hasta que el usuario decida salir.
GitHub El código desarrollado por el estudiante debe ser subido en su plenitud a GitHub.



"""
















class Reserva:
    def __init__(self, cliente, ciudad_origen, tour, cantidad_personas):
        
#Clase para representar una reserva de tour.

#cliente : Nombre y apellido del cliente.
#ciudad_origen : Ciudad de origen del cliente.
#tour : Detalle del tour (Torres del Paine, Carretera Austral o Chiloe).
#cantidad_personas : Cantidad de personas para el tour.
        
        self.cliente = cliente
        self.ciudad_origen = ciudad_origen
        self.tour = tour
        self.cantidad_personas = cantidad_personas

    def __str__(self):
       
#Representación en forma de cadena de texto de la reserva.

        return f"{self.cliente} ({self.ciudad_origen}) - {self.tour} ({self.cantidad_personas} personas)"

def registrar_reserva():
    
#Captura los datos de una reserva y crea una instancia de la clase Reserva.

    
    cliente = input("Nombre y apellido del cliente: ")
    ciudad_origen = input("Ciudad de origen: ")
    tour = input("Detalle del tour (Torres del Paine, Carretera Austral o Chiloe): ")
    cantidad_personas = int(input("Cantidad de personas para el tour: "))
    return Reserva(cliente, ciudad_origen, tour, cantidad_personas)

def listar_reservas(reservas):
    
#Muestra en pantalla todas las reservas registradas.

    if not reservas:
        print("No hay reservas registradas.")
    else:
        print("\nReservas registradas:")
        for reserva in reservas:
            print(reserva)

def imprimir_detalle_de_Reservas_por_destino(reservas):
    
#Crea un archivo de texto con el detalle de las reservas para un destino especifico

    
    destino = input("Selecciona un destino (Torres del Paine, Carretera Austral o Chiloe): ")
    filename = f"{destino}_reservas.txt"
    with open(filename, "w") as file:
        for reserva in reservas:
            if reserva.tour == destino:
                file.write(f"{reserva}\n")
    print(f"Detalle de reservas para {destino} guardado en {filename}")

def main():
    reservas = []
    while True:
        print("\n1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Imprimir Detalle de Reservas por Destino")
        print("4. Salir del Programa")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            reservas.append(registrar_reserva())
        elif opcion == "2":
            listar_reservas(reservas)
        elif opcion == "3":
            imprimir_detalle_de_Reservas_por_destino(reservas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()

