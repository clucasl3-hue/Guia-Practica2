from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  ✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            eliminado = pila.desapilar()
            if eliminado:
                print(f"  ✓ Salió del tope: {eliminado}")
                tope_actual = pila.ver_tope()
                if tope_actual:
                    print(f"  Nuevo tope: {tope_actual}")
                else:
                    print("  La pila ahora está vacía")
            else:
                print("  ⚠ La pila está vacía")
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                print(f"  Tope actual: {tope}")
            else:
                print("  ⚠ La pila está vacía")
        elif op == "5":
            num = leer_entero("  N.º de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en la posición [{pos}]")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_dest = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(num, nuevo_dest, nuevo_asiento):
                print("  ✓ Pasajero modificado con éxito")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print("  ✓ Pasajero eliminado correctamente")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "8":
            copia = pila.copiar()
            print("  ✓ Copia de la pila creada exitosamente:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()} | ¿Vacía?: {pila.esta_vacia()}")
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  ✓ Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "3":
            eliminado = cola.desencolar()
            if eliminado:
                print(f"  ✓ Salió del frente: {eliminado}")
                frente_actual = cola.ver_frente()
                if frente_actual:
                    print(f"  Nuevo frente: {frente_actual}")
                else:
                    print("  La cola ahora está vacía")
            else:
                print("  ⚠ La cola está vacía")
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                print(f"  Frente actual: {frente}")
            else:
                print("  ⚠ La cola está vacía")
        elif op == "5":
            num = leer_entero("  N.º de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en la posición [{pos}]")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_dest = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(num, nuevo_dest, nuevo_asiento):
                print("  ✓ Pasajero modificado con éxito")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print("  ✓ Pasajero eliminado correctamente")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "8":
            copia = cola.copiar()
            print("  ✓ Copia de la cola creada exitosamente:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()} | ¿Vacía?: {cola.esta_vacia()}")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()