# Nombre de la aplicación: Pruebas de con bases de datos SQLite
# 
# Programador: José Ramón Blanco Gutiérrez
#
# Fecha: Julio de 2020
#
# Otros datos: Son pruebas de base de datos para el TPVRaspy
#

#--- Modulos, librerias utilizadas ---

import sqlite3,time

def UltimoID(cursor):
    cursor.execute("SELECT * FROM TICKET")

    tabla = cursor.fetchall()
    id,A,B,C=tabla[-1]
    return id


def mainApp():
    #COnectando con la la Base de Datos de la TPVRasy y si no existiera cra el fichero')
    ConexionBD = sqlite3.connect("TPVRaspyII.DB3")
    PunteroBD = ConexionBD.cursor()

    #--- Crea la tabla TICKET
    #   NumTicket : de tipo integer y automático (Campo Clave y el Numero del Ticket)
    #   Fecha: de tipo texto con un tamaño de 10 XX/XX/XXXX
    #   FormaPago: de tipo texto con un tamaño 25, Posibles valores: CONTADO, TARJETA, VALES
    #   Total: Es la suma total de los articulos, de tipo real
    try:
        PunteroBD.execute('''CREATE TABLE TICKET (
                        NumTicket INTEGER PRIMARY KEY AUTOINCREMENT,
                        Fecha VARCHAR(10),
                        FormaPago VARCHAR(25),
                        Total REAL)''')
    except sqlite3.OperationalError:
        print("La tabla TICKET ya existe")                    
    #--- Crea la tabla DETALLE_TICKET
    #   NumTicket : Es el Numero del Ticket y es el campo que hace la referencia al ticket.
    #   Venta : Es la descripcion del articulo que se ha vendido, de tipo texto
    #   Importe : Es el precio de aritculo vendido, de tipo REAL
    #   La referencia es 1 Ticket infinitos Destalles de ticket
    try:
        PunteroBD.execute('''CREATE TABLE "DETALLE_TICKET" (
	                    "NumTicket"	INTEGER,
	                    "Venta"	VARCHAR(58),
	                    "Importe"	REAL,
	                    FOREIGN KEY("NumTicket") REFERENCES "TICKET"("NumTicket"))''')
    except sqlite3.OperationalError:
        print("La tabla DETALLE_TICKET ya existe") 
    #Inciamos variables
    """
    NumTicket=0
    Fecha=""
    FormaPago=""
    Total=0.0

    SubTicket=[] #Tupla de las ventas en un ticket (NumTicket, 'Concepto', Importe)
    while True:
        print("¿Quieres añadir una venta?")
        opcion = input("Escribe S o N y pulsa Intro:")
        if opcion=="S":
            Fecha=input("Fecha [DD/MM/AAAA]:")
            while True:
                Concepto=input("Concepto de Venta:")
                Importe=float(input("Importe en €:"))
                SubTicket.append((Concepto,Importe))
                opcion2=input("Quieres añadir otra venta en este ticket?[S/N]:")
                if opcion2=="N" or opcion2=="n":
                    break
            
            for i in SubTicket:
                    Total+=i[1]
            print("Total del Ticket: {}".format(Total))
            FormaPago=input("Forma de Pago [CONTADO,TARJETA,VALES]:")

            print(Fecha,FormaPago,Total)
            PunteroBD.execute("INSERT INTO TICKET VALUES(NULL,'{}','{}',{})".format(Fecha,FormaPago,Total))
            
            ID=UltimoID(PunteroBD)

            for detalle in SubTicket:
                PunteroBD.execute("INSERT INTO DETALLE_TICKET VALUES({},'{}','{}')".format(int(ID),detalle[0],detalle[1]))

            SubTicket.clear()
            break
        else:
            print("S o N, no es tan dificil de entender")
    

    
    
    ConexionBD.commit() 

    """
    print("--- listar tabla Ticket y SubTicket ---")
    PunteroBD.execute("SELECT * FROM TICKET")
    TablaTicket = PunteroBD.fetchall()

    for ticket in TablaTicket:
        print("Numero de ticket:",ticket[0])
        print("Fecha:", ticket[1])
        print("Forma de Pago:", ticket[2])
        print("--------------VENTAS---------------")
        PunteroBD.execute("SELECT * FROM DETALLE_TICKET WHERE NumTicket = {}".format(ticket[0]))
        TablaDetalleTicket = PunteroBD.fetchall()
        for detalle in TablaDetalleTicket:
            print("{} \t {}".format(detalle[1],detalle[2]))
        print("\t\t\tTOTAL:", ticket[3])
        print("-----------------------------------")

    
    #Confirma operaciones y guarda en la base de datos

    ConexionBD.close()
    return 0

if __name__ == "__main__":
    mainApp()    

