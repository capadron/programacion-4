import sqlite3
from sqlite3 import Error
sql_create_projects_table = """CREATE TABLE IF NOT EXISTS diccionario(
            ID integer PRIMARY KEY,
            Slang text NOT NULL,
            Significado text NOT NULL);"""
Temp2 = True
def connectarabd():

def menu():
    print("""Listado de opciones...
    a) Agregar nueva palabra
    c) Editar palabra existente
    d) Eliminar palabra existente
    e) Ver listado de diccionario
    f) Buscar significado de palabra
    g) Salir. """)
    Temp1 = input("Elige una de estas opciones. (a,c,d,e,f,g): ")
        try:
            con = sqlite3.connect('slangpan.db')
        con.execute(sql_create_projects_table)


while Temp2 == True:
    menu()
        if Temp1.upper() == "A":
            temppal = input("Escriba el slang nuevo : ")
            tempsig = input("Escriba el significado de la palabra '"+str(temppal)+"' : ")
            if  temppal == "" or tempsig == "":
                print("La informacion no puede estar en blanco.")
            else:
                try:
                    contemp = con.cursor()
                    contemp.execute("SELECT * FROM diccionario WHERE Slang = ? AND Significado = ?",[temppal,tempsig])
                    rows = contemp.fetchall()
                    if rows == []:
                        contemp = con.cursor()
                        tempres = contemp.execute("INSERT INTO diccionario (Slang, Significado) VALUES(?,?)",[temppal,tempsig])
                        tempres1 = con.commit()
                        print("El Slang fue agregado Satisfactoriamente al Disccionario.")
                    else:
                        print("El Slang '"+str(temppal)+"' ya se encuentra en el Diccionario.")
                except Error as error:
                    print(" Ocurrio un error, no se pudo agregar la palabra.")
                    print(" Error:",error)
            con.close()
        elif Temp1.upper() == "C":
            slangedit = input("Que Slang decea editar :").upper() 
            if  slangedit == "":
                print("La opcion no puede estar en blanco.")
            else:
                try:
                    contemp = con.cursor()
                    contemp.execute("SELECT * FROM diccionario WHERE upper(Slang) = ? ",[slangedit])
                    rows = contemp.fetchall()
                    contemp.close()
                    if rows != []:
                        try:
                            temppal = input("Escriba el slang nuevo :")
                            tempsig = input("Escriba el significado del Slang '"+str(temppal)+"' : ")
                            id = rows[0][0]
                            print(id)
                            tempres = con.execute("UPDATE diccionario SET Slang = ?, Significado = ? WHERE id = ?",[temppal,tempsig,id])
                            tempres1 = con.commit()
                            print(" Palabra editada correctamente")
                        except Error as error:
                            print(" Palabra no editada correctamente")
                            print(" Error:",error)
                    else:
                        print(" La palabra '"+str(slangedit)+"' no existe")
                except Error as error:
                    print(" El Slang no pudo ser Editado correctamente")
                    print(" Error:",error)
        elif Temp1.upper() == "D":
            slangelim = input("Ingrese palabra a eliminar  ").upper()
            try:
                tempres = con.execute("DELETE FROM diccionario WHERE upper(Slang) = ?",[slangelim])
                tempres1 = con.commit()
                print(" Palabra eliminada correctamente")
            except Error as error:
                print(" Palabra eliminada incorrectamente")
                print(" Error:",error)
            con.close()
        elif Temp1.upper() == "E":
            contemp = con.cursor()
            contemp.execute("SELECT * FROM diccionario")
            rows = contemp.fetchall()
            for row in rows:
                print("-- ID #",row[0]," --")
                print("PALABRA :",row[1])
                print("SIGNIFICADO :",row[2])
                print("")
            contemp.close()
        elif Temp1.upper() == "F":
            temppal = input("Ingrese palabra a buscar.").upper()
            print(temppal)
            contemp = con.cursor()
            sql = "SELECT * FROM diccionario WHERE upper(Slang) = ?"
            contemp.execute("SELECT * FROM diccionario WHERE upper(Slang) = ?",[temppal])
            rows = contemp.fetchall()
            for row in rows
                print("-- ID #",row[0]," --")
                print("PALABRA :",row[1])
                print("SIGNIFICADO :",row[2])
                print("")
            contemp.close()
        elif Temp1.upper() == "G":
            print("Saliendo...")
            Temp2 = False
        else:
            print("Opcion Incorrecta, Intente nuevamente. ")
            con.close()
    except Error as error:
        print("Error en el proceso: (",error,")")
        print("Cerrando DB...")
        con.close()
        Temp2 = False