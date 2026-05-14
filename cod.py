gastos = []
def registrar_gasto(gastos):
    placa = input("Ingrese placa del vehiculo: ")
    concepto = input("Ingrese concepto (Gasolina, Peaje, etc): ")
    valor = float(input("Ingrese valor del gasto: "))

    gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }
    gastos.append(gasto)
    print("Gasto registrado correctamente")

def calcular_total(gastos):
    total = 0
    for gasto in gastos:
        total += gasto["valor"]
    print("Total gastado en todos los vehiculos:", total)

def buscar_por_placa(gastos):
    placa_buscar = input("Ingrese la placa a buscar: ")
    encontrado = False
    for gasto in gastos:
        if gasto["placa"] == placa_buscar:
            print("GASTO ENCONTRADO")
            print("Placa:", gasto["placa"])
            print("Concepto:", gasto["concepto"])
            print("Valor:", gasto["valor"])
            encontrado = True
    if not encontrado:
        print("No se encontraron gastos para esa placa")

while True:
    print("MENU")
    print("1. Registrar gasto")
    print("2. Total gastos")
    print("3. Buscar gastos por placa")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_gasto(gastos)
    elif opcion == "2":
        calcular_total(gastos)
    elif opcion == "3":
        buscar_por_placa(gastos)
    elif opcion == "4":
        print("Programa finalizado")
        break
    else:
        print("Opcion invalida")