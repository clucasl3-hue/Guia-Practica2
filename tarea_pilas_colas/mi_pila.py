from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTACIÓN DE MÉTODOS DE LA PILA (LIFO) -------
    def desapilar(self):
        if self.cantidad == 0:
            return None
        self.cantidad -= 1
        pasajero = self.datos[self.cantidad]
        self.datos[self.cantidad] = None
        return pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        if self.buscar(numero) == -1:
            return False
        
        aux_pila = MiPila(self.capacidad)
        encontrado = False
        
        # Desapilar hasta encontrar el elemento
        while self.cantidad > 0:
            p = self.desapilar()
            if p.numero == numero:
                encontrado = True
                break
            else:
                aux_pila.apilar(p)
                
        # Devolver los elementos desde la auxiliar a la pila principal manteniendo el orden
        while aux_pila.cantidad > 0:
            p = aux_pila.desapilar()
            self.apilar(p)
            
        return encontrado

    def copiar(self):
        nueva = MiPila(self.capacidad)
        aux_pila = MiPila(self.capacidad)
        
        # Copiar elementos a una auxiliar para no alterar el orden original
        for i in range(self.cantidad - 1, -1, -1):
            aux_pila.apilar(self.datos[i])
            
        while aux_pila.cantidad > 0:
            nueva.apilar(aux_pila.desapilar())
            
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0