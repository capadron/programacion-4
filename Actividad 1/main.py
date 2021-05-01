import sqlite3
from sqlite3 import Error
Temp2 = True
while Temp2 == True:
    print("""Elige una Temp1...
    a) Agregar nueva palabra
    c) Editar palabra existente
    d) Eliminar palabra existente
    e) Ver listado de palabras
    f) Buscar significado de palabra
    g) Salir. """)
    Temp1 = input("Elige una Temp1 (a,c,d,e,f,g) >> ")
    try:
        con = sqlite3.connect('slang-panameño.db')
        
        if Temp1.upper() == "A":
            palabra = input("Ingrese la nueva palabra >> ")
            significado = input("Ingrese el significado de la palabra '"+str(palabra)+"' >> ")
            if  palabra == "" or significado == "":
                print("Los datos no pueden estar vacios...")
            else:
                try:
                    conObj = con.cursor()
                    conObj.execute("SELECT * FROM palabras WHERE palabra = ? AND significado = ?",[palabra,significado])
                    rows = conObj.fetchall()
                    if rows != []:
                        conObj.cursor()
                        result = conObj.execute("INSERT INTO palabras (palabra, significado) VALUES(?,?)",[palabra,significado])
                        result = conObj.commit()
                        print(">> Palabra agregada correctamente")
                    else:
                        print(">> La palabra '"+str(palabra)+"' ya existe")
                except Error as error:
                    print(">> Palabra no agregada correctamente")
                    print(">> Error:",error)
            con.close()
        elif Temp1.upper() == "C":
            palabraAEditar = input("Ingrese la palabra a editar >> ").upper()
            
            if  palabraAEditar == "":
                print("Los datos no pueden estar vacios...")
            else:
                try:
                    conObj = con.cursor()
                    conObj.execute("SELECT * FROM palabras WHERE upper(palabra) = ? ",[palabraAEditar])
                    rows = conObj.fetchall()
                    conObj.close()
                    if rows != []:
                        try:
                            palabra = input("Ingrese la palabra nueva >> ")
                            significado = input("Ingrese el significado de la palabra nueva >> ")
                            id = rows[0][0]
                            print(id)
                            result = con.execute("UPDATE palabras SET palabra = ?, significado = ? WHERE id = ?",[palabra,significado,id])
                            result = con.commit()
                            print(">> Palabra editada correctamente")
                        except Error as error:
                            print(">> Palabra no editada correctamente")
                            print(">> Error:",error)
                    else:
                        print(">> La palabra '"+str(palabraAEditar)+"' no existe")
                except Error as error:
                    print(">> Palabra no editada correctamente")
                    print(">> Error:",error)
        elif Temp1.upper() == "D":
            palabraAEliminar = input("Ingrese palabra a eliminar >> ").upper()

            try:
                result = con.execute("DELETE FROM palabras WHERE upper(palabra) = ?",[palabraAEliminar])
                result = con.commit()
                print(">> Palabra eliminada correctamente")
            except Error as error:
                print(">> Palabra eliminada incorrectamente")
                print(">> Error:",error)
            con.close()
        elif Temp1.upper() == "E":
            cursorObj = con.cursor()

            cursorObj.execute("SELECT * FROM palabras")
            rows = cursorObj.fetchall()
            for row in rows:
                print("-- ID #",row[0]," --")
                print(">>> PALABRA :",row[1])
                print(">>> SIGNIFICADO :",row[2])
                print("")
            cursorObj.close()
        elif Temp1.upper() == "F":
            palabra = input("Ingrese palabra a buscar >> ").upper()
            print(palabra)
            cursorObj = con.cursor()
            sql = "SELECT * FROM palabras WHERE upper(palabra) = ?"
            cursorObj.execute("SELECT * FROM palabras WHERE upper(palabra) = ?",[palabra])
            rows = cursorObj.fetchall()
            for row in rows:
                print("-- ID #",row[0]," --")
                print(">>> PALABRA :",row[1])
                print(">>> SIGNIFICADO :",row[2])
                print("")
            cursorObj.close()
        elif Temp1.upper() == "G":
            print(">> Saliendo...")
            Temp2 = False
        else:
            print(">> Opcion Incorrecta, Intente nuevamente. ")
            con.close()
    except Error as error:
        print(">> Error en el proceso: (",error,")")
        print(">> Cerrando DB...")
        con.close()
        Temp2 = False
