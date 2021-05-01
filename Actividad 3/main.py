import pymongo
from pymongo import MongoClient,errors


seguir = True

while seguir == True:
    print("Elige una opcion...")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra existente")
    print("e) Ver listado de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")

    opcion = input("Elige una opcion (a,c,d,e,f,g) >> ")

    i = 1
    try:
        con = pymongo.MongoClient("mongodb://localhost")
        nameDB  = "slang_panameno"
        db = con.slang_panameno

        palabras = db.palabras

        if opcion.upper() == "A":
            palabra = input("Ingrese la nueva palabra >> ")
            significado = input(
                "Ingrese el significado de la palabra '"+str(palabra)+"' >> ")
            if palabra == "" or significado == "":
                print("Los datos no pueden estar vacios...")
            else:
                try:
                    try:
                        lastId = palabras.find().sort("_id",-1)
                        idQ = lastId[0]["_id"] + 1
                        query = {'palabra':palabra}
                        queryI = {'palabra':palabra, 'significado':significado, '_id':idQ}
                        row = palabras.find_one(query)
                        if row == None:
                            try:
                                palabras.insert_one(queryI)
                                print(">> Palabra agregada correctamente")
                            except errors.PyMongoError as e:
                                print(">> Palabra no agregada correctamente")
                                print(">> ERROR:",e)
                        else:
                            print(">> La palabra '" +
                                    str(palabra)+"' ya existe")
                    except errors.PyMongoError as e:
                        print(e)

                except errors.PyMongoError as error:
                    print(">> Palabra no agregada correctamente")
                    print(">> Error:", error)
        elif opcion.upper() == "C":
            palabraAEditar = input("Ingrese la palabra a editar >> ")
            if palabraAEditar == "" :
                print("Los datos no pueden estar vacios...")
            else:
                try:
                    try:
                        query = {'palabra':palabraAEditar}
                        row = palabras.find_one(query)
                        if row != None:
                            palabra = input("Ingrese la nueva palabra >> ")
                            significado = input("Ingrese el significado de la palabra '"+str(palabra)+"' >> ")
                            if palabra == "" and significado == "":
                                print("Los datos no pueden estar vacios...")
                            else:
                                try:
                                    queryI = {'palabra':palabra, 'significado':significado}
                                    palabras.find_and_modify(query={'_id':row["_id"]},update={'$set':queryI},upsert=True, full_response=True)
                                    print(">> Palabra editada correctamente")
                                except errors.PyMongoError as e:
                                    print(">> Palabra no editada correctamente")
                                    print(">> ERROR:",e)
                        else:
                            print(">> La palabra '" +
                                    str(palabraAEditar)+"' no existe")
                    except errors.PyMongoError as e:
                        print(e)

                except errors.PyMongoError as error:
                    print(">> Palabra no editada correctamente")
                    print(">> Error:", error)
        elif opcion.upper() == "D":
            palabra = input("Ingrese la palabra a eliminar >> ")
            if palabra == "" :
                print("Los datos no pueden estar vacios...")
            else:
                try:
                    try:
                        lastId = palabras.find().sort("_id",-1)
                        lastId = int(lastId[0]["_id"]) + 1
                        query = {'palabra':palabra}
                        row = palabras.find_one(query)
                        if row != None:
                            palabras.find_one_and_delete(query)
                            try:
                                print(">> Palabra eliminada correctamente")
                            except errors.PyMongoError as e:
                                print(">> Palabra no eliminada correctamente")
                                print(">> ERROR:",e)
                        else:
                            print(">> La palabra '" +
                                    str(palabra)+"' no existe")
                    except errors.PyMongoError as e:
                        print(e)

                except errors.PyMongoError as error:
                    print(">> Palabra no agregada correctamente")
                    print(">> Error:", error)
        elif opcion.upper() == "E":
            palabrasList = palabras.find()
            for palabra in palabrasList:
                print("-- ID #", palabra["_id"], " --")
                print(">>> PALABRA :", palabra["palabra"])
                print(">>> SIGNIFICADO :", palabra["significado"])
                print("")
        elif opcion.upper() == "F":
            palabra = input("Ingrese palabra a buscar >> ")
            query = {'palabra' : palabra}
            queryI = {'palabra':'', 'significado':'', '_id':''}
            palabrasList = palabras.find_one(query)
            print("-- ID #", palabrasList["_id"], " --")
            print(">>> PALABRA :", palabrasList["palabra"])
            print(">>> SIGNIFICADO :", palabrasList["significado"])
            print("")
        elif opcion.upper() == "G":
            print(">> Saliendo...")
            seguir = False
        else:
            print(">> Opcion no valida...")
            print(">> Cerrando DB...")
            seguir = False
    except pymongo.errors.PyMongoError as error:
        print(">> Error en el proceso: (", error, ")")
        print(">> Cerrando DB...")
        seguir = False
    i = i + 1
