# Función para mostrar el menú de opciones del cajero automático
def mostrar_menu():
    print("\nMenú del Cajero Automático")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

# Función para consultar el saldo actual
def consultar_saldo(saldo):
    print(f"Tu saldo actual es: ${saldo}")

# Función para depositar dinero en la cuenta
def depositar_dinero(saldo):
    cantidad = float(input("Ingresa la cantidad a depositar: "))
    if cantidad > 0:  # Verifica que la cantidad a depositar sea positiva
        saldo += cantidad  # Suma la cantidad al saldo actual
        print(f"Has depositado ${cantidad}. Tu nuevo saldo es: ${saldo}")
    else:
        print("Cantidad no válida.")  # Mensaje de error si la cantidad no es válida
    return saldo  # Devuelve el nuevo saldo

# Función para retirar dinero de la cuenta
def retirar_dinero(saldo):
    cantidad = float(input("Ingresa la cantidad a retirar: "))
    if 0 < cantidad <= saldo:  # Verifica que la cantidad a retirar sea positiva y no exceda el saldo
        saldo -= cantidad  # Resta la cantidad del saldo actual
        print(f"Has retirado ${cantidad}. Tu nuevo saldo es: ${saldo}")
    else:
        print("Cantidad no válida o saldo insuficiente.")  # Mensaje de error si la cantidad no es válida o el saldo es insuficiente
    return saldo  # Devuelve el nuevo saldo

# Función principal del cajero automático
def cajero_automatico():
    saldo = 1000.0  # Saldo inicial
    while True:  # Bucle infinito para mantener el programa en ejecución
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == '1':
            consultar_saldo(saldo)  # Llama a la función para consultar el saldo
        elif opcion == '2':
            saldo = depositar_dinero(saldo)  # Llama a la función para depositar dinero y actualiza el saldo
        elif opcion == '3':
            saldo = retirar_dinero(saldo)  # Llama a la función para retirar dinero y actualiza el saldo
        elif opcion == '4':
            print("Gracias por usar el cajero automático. ¡Hasta luego!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje de error si la opción no es válida

# Punto de entrada del programa
if __name__ == "__main__":
    cajero_automatico()  # Llama a la función principal si el archivo se ejecuta directamente
