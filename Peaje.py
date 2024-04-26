total_categoria_I = 0
total_categoria_II = 0
total_categoria_III = 0
total_categoria_IV = 0
total_categoria_V = 0
total_categoria_VI_VII =0
while True:
    print("categorias del peaje\n")
    print("1.Categoria I\n")
    print("2.Categoria II\n")
    print("3.Categoria III\n")
    print("4.Categoria IV\n")
    print("5.Categoria V\n")
    print("6.Categoria VI-VII\n")
    print("7.Cerrar programa\n")
    opc=(int(input("elige la categoria a cobrar: ")))
    if opc==1:
        print("El valor a cobrar es 10600\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<10600:
            print("El dinero recibido es insuficiente\n")
            dif=10600-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 10600:
                print("Pago completo. Buen viaje\n")
                total_categoria_I+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_I+=vlr
    if opc==2:
        print("El valor a cobrar es 11500\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<115000:
            print("El dinero recibido es insuficiente\n")
            dif=11500-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 11500:
                print("Pago completo. Buen viaje\n")
                total_categoria_II+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_II+=vlr
    if opc==3:
        print("El valor a cobrar es 25400\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<25400:
            print("El dinero recibido es insuficiente\n")
            dif=25400-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 25400:
                print("Pago completo. Buen viaje\n")
                total_categoria_III+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_III+=vlr
    if opc==4:
        print("El valor a cobrar es 33200\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<33200:
            print("El dinero recibido es insuficiente\n")
            dif=33200-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 33200:
                print("Pago completo. Buen viaje\n")
                total_categoria_IV+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_IV+=vlr
    if opc==5:
        print("El valor a cobrar es 38400\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<38400:
            print("El dinero recibido es insuficiente\n")
            dif=38400-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 34800:
                print("Pago completo. Buen viaje\n")
                total_categoria_V+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_V+=vlr
    if opc==6:
        print("El valor a cobrar es 38400\n")
        vlr=int(input("El dinero recibido es: "))
        if vlr<38400:
            print("El dinero recibido es insuficiente\n")
            dif=38400-vlr
            print("El dinero faltante es: ",dif)
            faltante=int(input("Ingrese el dinero faltante: "))
            vlr += faltante
            if vlr == 38400:
                print("Pago completo. Buen viaje\n")
                total_categoria_VI_VII+=vlr
                break
            else:
                print("Pago incorrecto. Intente de nuevo.")
        else:
            print("Pago completo. Buen viaje\n")
            total_categoria_VI_VII+=vlr
        
    elif opc == '7':
       print("Hasta pronto!")
       break

total = total_categoria_I + total_categoria_II + total_categoria_III + total_categoria_IV + total_categoria_V + total_categoria_VI_VII

print("Total recibido en cada categoría:")
print("Categoria I: ", total_categoria_I)
print("Categoria II: ", total_categoria_II)
print("Categoria III: ", total_categoria_III)
print("Categoria IV: ", total_categoria_IV)
print("Categoria V: ", total_categoria_V)
print("Categoria VI-VII: ", total_categoria_VI_VII)
print("Total recibido: ", total)