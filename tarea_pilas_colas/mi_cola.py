from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTACIÓN DE MÉTODOS DE LA COLA (FIFO) -------
    def desencolar(self):
        if self.cantidad == 0:
            return None
        
        pasajero_frente = self.datos[0]
        # Correr elementos a la izquierda
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
            
        self.datos[self.cantidad - 1] = None
        self.cantidad -= 1
        return pasajero_frente

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
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
            
        n = self.cantidad
        encontrado = False
        
        for _ in range(n):
            p = self.desencolar()
            if p.numero == numero:
                encontrado = True
                # No se vuelve a encolar, por lo que queda eliminado
            else:
                self.encolar(p)
                
        return encontrado

    def copiar(self):
        nueva = MiCola(self.capacidad)
        n = self.cantidad
        
        for _ in range(n):
            p = self.desencolar()
            nueva.encolar(p)
            self.encolar(p) # Restaurar en el original
            
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0