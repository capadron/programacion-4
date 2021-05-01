

print("""MENU Registros

1)-Nuevo
2)-Mostrar
3)-Eliminar Registros
4)-Buscar""")
opcion = input("Seleccione una opcion con el numero: ")

if opcion == "1":
    print("""Nuevo Registro:
    """)
    archivo = open("lista.csv","a")

    modelo = input("Ingrese el modelo: ")
    imei = input("Ingrese el imei: ")

    print("Se han capturado: " + modelo + ", con el tel: " + imei)

    archivo.write(modelo)
    archivo.write(",")
    archivo.write(imei)
    archivo.write(",")
    archivo.write("\n")

    archivo.close()

elif opcion == "2":
    print("Mostrar Registros")
    archivo = open("lista.csv")

    print(archivo.read())

    archivo.close()

elif opcion == "3":
    archivo = open("lista.csv","a")
    archivo.truncate()

    print("Registros Eliminados")

    archivo.close()

elif opcion == "4":
    archivo = open("lista.csv")
    archivo.close()
else:
    print("Debes de elegir una opcion anterior")