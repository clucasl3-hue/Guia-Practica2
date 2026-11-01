from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        if any(p.numero == pasajero.numero for p in self.pasajeros):
            print(f"  ⚠ El número de pasajero #{pasajero.numero} ya existe.")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  ⚠ Posición inválida")
            return False
        if any(p.numero == pasajero.numero for p in self.pasajeros):
            print(f"  ⚠ El número de pasajero #{pasajero.numero} ya existe.")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        res = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return res[0] if res else -1

    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        idx = bisect_left(numeros, numero)
        if idx < len(self.pasajeros) and self.pasajeros[idx].numero == numero:
            return idx
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if 0 <= posicion < len(self.pasajeros):
            return self.pasajeros.pop(posicion)
        return None

    def eliminar_por_valor(self, numero):
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        dest = destino.strip().lower()
        return [p for p in self.pasajeros if p.destino.strip().lower() == dest]

    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]