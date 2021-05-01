import sqlite3


class Base_Datos():
    def __init__(self) -> None:
        #Conectando con la la Base de Datos de la TPVRaspy
        # y si no existiera cera el fichero')
        self.ConexionBD = sqlite3.connect("db_ticket.sqlite")
        self.PunteroBD = self.ConexionBD.cursor()

        #------------------------------------
        # Tabla TICKET
        #------------------------------------ 
        #   NumTicket : de tipo integer y automático (Campo Clave y el Numero del Ticket)
        #   Fecha: de tipo texto con un tamaño de 10 XX/XX/XXXX
        #   Hora: de tipo texto con 5 de datamaño XX:XX
        #   FormaPago: de tipo texto con un tamaño 8, Posibles valores: CONTADO, TARJETA, VALES
        #   SumaImporte: es la suma de todos los productos del detalle, de tipo real
        #   IVA: Es el IVA, de tipo real
        #   Total: Es la suma total de los articulos, de tipo real
        #------------------------------------
        try: 
            self.PunteroBD.execute('''CREATE TABLE TICKET (
                        NumTicket INTEGER PRIMARY KEY AUTOINCREMENT,
                        Fecha VARCHAR(10),
                        Hora VARCHAR(5),
                        FormaPago VARCHAR(30),
                        SumaImporte REAL,
                        IVA REAL,
                        Total REAL)''')
        except sqlite3.OperationalError:
            pass
            #Explicación de este bloque:
            # Si durante la ejecución de la sentacia de creación
            # de la tabla ocurre un error, se controla el error con el TRY ya que existe
            # la tabla en el fichero y continuamos con la ejecución.
        #------------------------------------
        # Tabla DETALLE_TICKET
        #------------------------------------ 
        #   NumTicket : Es el Numero del Ticket y es el campo que hace la referencia al ticket.
        #   Venta : Es la descripcion del articulo que se ha vendido, de tipo texto
        #   Importe : Es el precio de aritculo vendido, de tipo REAL
        #   La relación (referencia) es 1 Ticket infinitos Destalles de ticket
        try:
            self.PunteroBD.execute('''CREATE TABLE "DETALLE_TICKET" (
	                    "NumTicket"	INTEGER,
	                    "Venta"	VARCHAR(58),
	                    "Importe"	REAL,
	                    FOREIGN KEY("NumTicket") REFERENCES "TICKET"("NumTicket"))''')
        except sqlite3.OperationalError:
            pass
            # Hacemos lo mismo que antes.

    #========================================================
    # Método Guardar
    #   - Descripción: Guarda en la base de datos el ticket.
    #========================================================
    def guardarNuevoTicket(self, fecha, hora, formadepago, sumaimporte, iva, total, datosdetalle):
        #Guarda el nuevo Ticket
        self.PunteroBD.execute("INSERT INTO TICKET VALUES(NULL,'{}','{}','{}',{},{},{})".format(
                        fecha, #Se guarda la fecha con el formato DD/MM/AAAA
                        hora, #Se guarda la hora con el formado HH:MM
                        formadepago, #Se guarda la forma de pago pasada como parametro
                        float(sumaimporte), #La suma de los importes del detalle
                        float(iva), #El iva
                        float(total))) #Total del ticket

        id = self.ultimoID() #Obtenemos el ID que se ha creado en la operación INSERT anterior

        #Se recorre ahora la lista pasada como argumento "datosdetalle"
        for detalle in datosdetalle:
            self.PunteroBD.execute("INSERT INTO DETALLE_TICKET VALUES({},'{}',{})".format(
                            int(id), #id
                            detalle[0], #Concepto
                            float(detalle[1])) #Importe como real (float)
                            )

        self.ConexionBD.commit() #Finaliza la transacción

        self.ConexionBD.close() #Cerramos la base de datos.
    
    #========================================================
    # Método ultimoID
    #   - Descripción: Devuelve el ID del ultimo ticket insertado.
    #                  Utilizado para mantener la integridad al insertar
    #                  en la tabla detalles y que tenga el ID del ticket 
    #========================================================
    def ultimoID(self):
        #------------------------------------
        # Lee la tabla Ticket en orden inverso y extraigo el primero que es el ultimo de la tabla
        #------------------------------------
        self.PunteroBD.execute("SELECT * FROM TICKET ORDER BY NumTicket DESC")

        id = self.PunteroBD.fetchone()
        
        return id[0] #El primera Campo es el ID


    #========================================================
    # Método LeerUltimoTicket
    #   - Descripción: Devuelve dos tuplas:
    #                   1ª con los datos del registro
    #                   2ª con todos los registros del detalle
    #========================================================
    def LeerUltimoTicket(self):
        #------------------------------------
        # Lee la tabla Ticket en orden inverso y extraigo el primero que es el ultimo de la tabla
        #------------------------------------
        self.PunteroBD.execute("SELECT * FROM TICKET ORDER BY NumTicket DESC LIMIT 1") 
    
        ultimoRegistro = self.PunteroBD.fetchone() 
        
        self.PunteroBD.execute("SELECT * FROM DETALLE_TICKET WHERE NumTicket = {}".format(ultimoRegistro[0]))
        detalleUltimoRegistro = self.PunteroBD.fetchall() #Obtemos el detalle completo del ultimo registro

        self.ConexionBD.close() #Cerramos la base de datos.
        
        return ultimoRegistro,detalleUltimoRegistro

    #========================================================
    # Método LeerTicketNumero
    #   - Descripción: Lee el ticket con el numero dado. 
    #           · Devuelve dos tuplas:
    #                   1ª con los datos del registro
    #                   2ª con todos los registros del detalle
    #========================================================
    def LeerTicketNumero(self,Numero):
        #------------------------------------
        # Lee la tabla Ticket en orden inverso y extraigo el primero que es el ultimo de la tabla
        #------------------------------------
        self.PunteroBD.execute("SELECT * FROM TICKET WHERE NumTicket = {}".format(int(Numero))) 
    
        registro = self.PunteroBD.fetchone() 
        
        self.PunteroBD.execute("SELECT * FROM DETALLE_TICKET WHERE NumTicket = {}".format(int(Numero)))
        detalleregistro = self.PunteroBD.fetchall() #Obtemos el detalle completo del ultimo registro

        self.ConexionBD.close() #Cerramos la base de datos.
        
        return registro,detalleregistro

    #========================================================
    # Método ListarTodosTicket
    #   - Descripción: Devuelve una tupla con el Número de ticket,
    #                  la fecha, forma de pago y el Total.
    #                  0 = Todos los registros 
    #========================================================
    def ListarTicket(self,num=0):
        if num == 0:
            self.PunteroBD.execute("SELECT NumTicket, Fecha, FormaPago, Total  FROM TICKET ORDER BY NumTicket")
        else:
            self.PunteroBD.execute("SELECT NumTicket, Fecha, FormaPago, Total  FROM TICKET WHERE NumTicket= {} ORDER BY NumTicket".format(num))

        
        consulta =  self.PunteroBD.fetchall()

        self.ConexionBD.close()

        return consulta

    #========================================================
    # Método ListarTicketPorFecha
    #   - Descripción: Devuelve una tupla con el Número de ticket,
    #                  forma de pago y el Total.
    #                   
    #========================================================
    def ListarTicketPorFecha(self,Fecha):
        self.PunteroBD.execute("SELECT NumTicket, Fecha, FormaPago, Total  FROM TICKET WHERE Fecha= '{}' ORDER BY NumTicket".format(Fecha))
        
        consulta =  self.PunteroBD.fetchall()

        self.ConexionBD.close()

        return consulta

    #========================================================
    # Método consultaTicketPorFecha
    #   - Descripción: Devuelve una tupla con el numero de ticket,
    #                  Producto, precio, iva y forma de pago 
    #========================================================
    def consultaTicketPorFecha(self, Fecha):
        resultado_consulta = []
        self.PunteroBD.execute("SELECT NumTicket, Fecha, FormaPago, Total , IVA  FROM TICKET WHERE Fecha= '{}' ORDER BY NumTicket".format(Fecha))
        consulta = self.PunteroBD.fetchall()

        for c in consulta:
            self.PunteroBD.execute("SELECT * FROM DETALLE_TICKET WHERE NumTicket = {}".format(c[0]))
            detalle = self.PunteroBD.fetchall()
            for d in detalle:
                resultado_consulta.append((d[0],d[1],d[2],c[2],c[4]))
        
        self.ConexionBD.close()
        return resultado_consulta
    
    #========================================================
    # Método consultaListaTicketPorNumero
    #   - Descripción: Devuelve una tupla con el numero de ticket,
    #                  Producto, precio, iva y forma de pago 
    #========================================================
    def consultaListaTicketPorNumero(self, datos):
        resultado_consulta = []
        

        for a in datos:
            self.PunteroBD.execute("SELECT NumTicket, Fecha, FormaPago, Total , IVA  FROM TICKET WHERE NumTicket= {} ORDER BY NumTicket".format(a[0]))
            consulta = self.PunteroBD.fetchall()
            for c in consulta:
                self.PunteroBD.execute("SELECT * FROM DETALLE_TICKET WHERE NumTicket = {}".format(a[0]))
                detalle = self.PunteroBD.fetchall()
                for d in detalle:
                    resultado_consulta.append((d[0],d[1],d[2],c[2],c[4],c[1]))
        
        return resultado_consulta