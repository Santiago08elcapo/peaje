total_categoria_I = 0
total_categoria_II = 0
total_categoria_III = 0
total_categoria_IV = 0
total_categoria_V = 0
total_categoria_VI_VII = 0

categorias = {
    1: {"nombre": "Categoría I", "valor": 10600},
    2: {"nombre": "Categoría II", "valor": 11500},
    3: {"nombre": "Categoría III", "valor": 25400},
    4: {"nombre": "Categoría IV", "valor": 33200},
    5: {"nombre": "Categoría V", "valor": 38400},
    6: {"nombre": "Categoría VI-VII", "valor": 38400}
}

while True:
    print("Categorías del peaje:\n")
    for categoria_id, categoria in categorias.items():
        print(f"{categoria_id}. {categoria['nombre']}")
    print("7. Cerrar programa\n")

    opc = input("Elige la categoría a cobrar: ")

    if opc == "7":
        print("¡Hasta pronto!")
        break

    try:
        opc = int(opc)
        if opc not in categorias:
            print("Opción inválida. Intente de nuevo.")
            continue

        categoria = categorias[opc]
        print(f"El valor a cobrar es {categoria['valor']}")
        vlr = int(input("El dinero recibido es: "))

        if vlr < categoria['valor']:
            print("El dinero recibido es insuficiente")
            dif = categoria['valor'] - vlr
            print(f"El dinero faltante es: {dif}")
            faltante = int(input("Ingrese el dinero faltante: "))
            vlr += faltante

        if vlr == categoria['valor']:
            print("Pago completo. Buen viaje\n")
            if opc == 1:
                total_categoria_I += vlr
            elif opc == 2:
                total_categoria_II += vlr
            elif opc == 3:
                total_categoria_III += vlr
            elif opc == 4:
                total_categoria_IV += vlr
            elif opc == 5:
                total_categoria_V += vlr
            elif opc == 6:
                total_categoria_VI_VII += vlr
        else:
            print("Pago incorrecto. Intente de nuevo.")

    except ValueError:
        print("Opción inválida. Intente de nuevo.")

total = total_categoria_I + total_categoria_II + total_categoria_III + total_categoria_IV + total_categoria_V + total_categoria_VI_VII

print("\nTotal recibido en cada categoría:")
print(f"Categoría I: {total_categoria_I}")
print(f"Categoría II: {total_categoria_II}")
print(f"Categoría III: {total_categoria_III}")
print(f"Categoría IV: {total_categoria_IV}")
print(f"Categoría V: {total_categoria_V}")
print(f"Categoría VI-VII: {total_categoria_VI_VII}")
print(f"Total recibido: {total}")