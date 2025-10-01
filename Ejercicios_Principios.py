#Manejar los datos del Cliente
#Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self._nombre = nombre          
        def get_nombre(self):
            return self._nombre

#Aqui manejamos las reservas
#Clase Reserva
class Reserva:
    def __init__(self, cliente, plato):
        self._cliente = cliente
        self._plato = plato
        self._activa = True
        def cancelar (self):
            self._activa = False
            def esta_activa(self):
                return self._activa
            def get_cliente(self):
                return self._cliente
            def get_plato(self):
                return self._plato

#Generar las facturas
#Clase Factura
class Facturas:
    def __init__(self, reserva, precio):
        self._reserva = reserva
        self._precio = precio
        def imprimir_factura(self):
            if self._reserva.esta_activa():
                print(f"Factura para{self._reserva.get_cliente().get_nombre()}")
                print(f"Plato:{self._reserva.get_plato()}- Total:${self._precio}")
            else:
                print("No se puede generar factura, la reserva fue cancelada.")

#Y por ultimo seria cordinar las mesas y reservas 
#Clase Restaurante
class Restaurante:
    def __init__(self, mesas_disponibles=10):
        self._mesas_disponibles = mesas_disponibles
        self._reservas = []
        def hacer_reserva(self, cliente,plato):
            if self._mesas_disponibles > 0:
                reserva = Reserva(cliente, plato)
                self._reservas.append(reserva)
                self._mesas_disponibles -=1
                print(f"Reserva hecha para {cliente.get_nombre()}")
                return reserva
            else:
                print("No hay mesas disponibles")
                return None
            def cancelar_reserva(self, reserva):
                if reserva in self._reservas and reserva.esta_activa():
                    reserva.cancelar()
                    self._mesas_disponibles += 1
                    print(f"Reserva cancelada para {reserva.get_cliente().get_nombre()}")
                else:
                    print("La reserva no existe o ya fue cancelada")
                    def get_mesas_disponibles(self):
                        return self._mesas_disponibles