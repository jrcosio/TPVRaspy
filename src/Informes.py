# -*- coding: utf-8 -*-
from datetime import datetime
from ImprimirTicket import Imprimir
from BaseDatos import Base_Datos
from PyQt5 import QtCore, QtGui, QtWidgets


class Informes(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        
        self.ticket = 0
        self.detalleticket = 0

        self.__setupUi() 
        self.Tabla = self.LeerDatosPorNumero()
        self.CargarDatosTabla(self.Tabla)

        #--------------------------
        # Definición de los eventos
        #--------------------------
        self.btnCerrar.clicked.connect(lambda:self.close())
        self.btnImprimirUltimoTickets.clicked.connect(self.onUltimoTicket)
        self.btnBuscar.clicked.connect(self.onBuscar)
        self.btnImprimirTicket.clicked.connect(self.onImprimir)
        self.btnImprimirTodoDia.clicked.connect(self.onImprimirHoy)
        self.btnImprimirListado.clicked.connect(self.onImprimirTabla)
        self.TableTicket.clicked.connect(self.onFilaSeleccionada) #Al selecionar una fila de la tabla


    def __setupUi(self):
        self.resize(850, 459)
        self.setMinimumSize(QtCore.QSize(850, 459))
        self.setMaximumSize(QtCore.QSize(850, 459))
        self.setWindowTitle("Informes de los Tickets")

       

        self.btnImprimirUltimoTickets = QtWidgets.QPushButton(self)
        self.btnImprimirUltimoTickets.setGeometry(QtCore.QRect(0, 3, 261, 64))
        self.btnImprimirUltimoTickets.setText("Imprimir último TICKET")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimirUltimoTickets.setIcon(icon)
        self.btnImprimirUltimoTickets.setIconSize(QtCore.QSize(48, 48))

        self.btnImprimirTodoDia = QtWidgets.QPushButton(self)
        self.btnImprimirTodoDia.setGeometry(QtCore.QRect(266, 3, 291, 64))
        self.btnImprimirTodoDia.setText("Imprimir TODAS la ventas del día")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/lista2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimirTodoDia.setIcon(icon)
        self.btnImprimirTodoDia.setIconSize(QtCore.QSize(48, 48))
         
        self.txtMostrarTicket = QtWidgets.QTextEdit(self)
        self.txtMostrarTicket.setGeometry(QtCore.QRect(560, 20, 281, 371))
        self.txtMostrarTicket.setReadOnly(True)
        
        self.lbTicket = QtWidgets.QLabel(self)
        self.lbTicket.setGeometry(QtCore.QRect(560, 0, 281, 16))
        self.lbTicket.setText("Ticket")
        self.lbTicket.setAlignment(QtCore.Qt.AlignCenter)
        
        self.btnImprimirTicket = QtWidgets.QPushButton(self)
        self.btnImprimirTicket.setGeometry(QtCore.QRect(710, 400, 130, 56))
        self.btnImprimirTicket.setText("Imprimir")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/imprimir2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimirTicket.setIcon(icon)
        self.btnImprimirTicket.setIconSize(QtCore.QSize(32, 32))

        self.TableTicket = QtWidgets.QTableWidget(self)
        self.TableTicket.setGeometry(QtCore.QRect(6, 140, 545, 251))
        self.TableTicket.setColumnCount(4)
        self.TableTicket.setRowCount(0)

        self.TableTicket.setColumnWidth(0, 50) #Tamaño de la primera columna
        self.TableTicket.setColumnWidth(1, 140) #Tamaño de la primera columna
        self.TableTicket.setColumnWidth(2, 200) #Tamaño de la primera columna
        self.TableTicket.setColumnWidth(3, 80) #Tamaño de la primera columna
        self.TableTicket.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Seleccionar toda la fila
        self.TableTicket.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  # Seleccionar una fila a la vez
        
        

        item = QtWidgets.QTableWidgetItem()
        item.setText("Num")
        self.TableTicket.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Fecha")
        self.TableTicket.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Forma de Pago")
        self.TableTicket.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Total")
        self.TableTicket.setHorizontalHeaderItem(3, item)

        self.lbNum = QtWidgets.QLabel(self)
        self.lbNum.setGeometry(QtCore.QRect(20, 90, 130, 16))
        self.lbNum.setText("Número de Ticket")

        self.txtFecha = QtWidgets.QLineEdit(self)
        self.txtFecha.setGeometry(QtCore.QRect(300, 80, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtFecha.setFont(font)
        self.txtFecha.setAlignment(QtCore.Qt.AlignCenter)

        self.txtNum = QtWidgets.QLineEdit(self)
        self.txtNum.setGeometry(QtCore.QRect(140, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtNum.setFont(font)
        self.txtNum.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNum.setValidator(QtGui.QIntValidator()) #Al lineText le pone que solo adminita numero integer


        self.lbFecha = QtWidgets.QLabel(self)
        self.lbFecha.setGeometry(QtCore.QRect(200, 90, 111, 16))
        self.lbFecha.setText("Fecha Ticket")

        self.btnBuscar = QtWidgets.QPushButton(self)
        self.btnBuscar.setGeometry(QtCore.QRect(416, 72, 141, 64))
        self.btnBuscar.setText("Buscar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(48, 48))


        self.btnImprimirListado = QtWidgets.QPushButton(self)
        self.btnImprimirListado.setGeometry(QtCore.QRect(535, 400, 171, 56))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimirListado.setText("Imprimir Listado")
        self.btnImprimirListado.setIcon(icon)
        self.btnImprimirListado.setIconSize(QtCore.QSize(32, 32))

        self.btnCerrar = QtWidgets.QPushButton(self)
        self.btnCerrar.setGeometry(QtCore.QRect(0, 400, 111, 56))
        self.btnCerrar.setText("Cerrar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon)
        self.btnCerrar.setIconSize(QtCore.QSize(32, 32))
        self.btnCerrar.setDefault(True)
        


    def CargarDatosTabla(self,Tabla):
        self.TableTicket.setRowCount(len(Tabla))
        for columna in range(4):
            for fila in range(len(Tabla)):
                elementoTabla = QtWidgets.QTableWidgetItem(str(Tabla[fila][columna]))
                elementoTabla.setTextAlignment(0x0084)
                self.TableTicket.setItem(fila,columna,elementoTabla)

    #==========================================
    # Método LeerDatosPorNumero
    #   - Descripción: Obtiene una lista con todos los registros que tengan el numero dado
    #                   sino se pasa ningun dato se devuelve todos los ticket.
    #========================================== 
    def LeerDatosPorNumero(self, NumTicket=0):
        db = Base_Datos()
        Tabla = db.ListarTicket(NumTicket)
        return Tabla
   
    #==========================================
    # Método LeerDatosPorFecha
    #   - Descripción: Obtiene una lista con todos los registros que la misma fecha
    #                  introducida.
    #========================================== 
    def LeerDatosPorFecha(self, Fecha):
        db = Base_Datos()
        Tabla = db.ListarTicketPorFecha(Fecha)
        return Tabla


    #==================================================================================
    # Método onFilaSeleccionada
    #   - Descripción: Método que lanza al pulsar en una lina en la tabla y lo que hace
    #                   es obtener el numero de ticket para buscar el registro en la DB
    #                   y mostrar la en pantalla. 
    #==================================================================================
    def onFilaSeleccionada(self):
        fila = self.TableTicket.selectedItems()
        ticketDB = Base_Datos()
        self.ticket, self.detalleticket = ticketDB.LeerTicketNumero(fila[0].text())
        self.CargarTicketenMostrarTicket(self.ticket,self.detalleticket)

    #==================================================================================
    # Método CargarTicketenMostrarTicket
    #   - Descripción: Método para visualizar el ticket
    #==================================================================================
    def CargarTicketenMostrarTicket(self,ticket,detalle):
        self.txtMostrarTicket.clear()
        self.txtMostrarTicket.append("-------------------------------------------")
        self.txtMostrarTicket.append("         Joyería Blanco")
        self.txtMostrarTicket.append("  Paseo Gral. Dávila 264 Nº 2")
        self.txtMostrarTicket.append("    Santander - Cantabria")
                                      
        self.txtMostrarTicket.append("-------------------------------------------")
        self.txtMostrarTicket.append("Número Ticket: " + str(ticket[0]))
        self.txtMostrarTicket.append("Fecha: " + str(ticket[1]))
        self.txtMostrarTicket.append("Hora: " + str(ticket[2]))
        self.txtMostrarTicket.append("Forma de pago: " + str(ticket[3]))
        self.txtMostrarTicket.append("-------------------------------------------")
        self.txtMostrarTicket.append("Artículo                        Importe")
        self.txtMostrarTicket.append("-------------------------------------------")
        for lista in detalle:
            self.txtMostrarTicket.append(str(lista[1]))                   
            self.txtMostrarTicket.append("                                       " + str(lista[2]) + "€") 
        self.txtMostrarTicket.append("===================")
        if str(ticket[5]) != "0.0":                 #No Imprimir el IVA si este vale CERO
            self.txtMostrarTicket.append("Suma Importes: " + str(ticket[4]) + "€")
            self.txtMostrarTicket.append("IVA 21%: " + str(ticket[5])  + "€")
        
        self.txtMostrarTicket.append("TOTAL TICKET: " + str(ticket[6]) + "€")
 

    #==================================================================================
    # Método onUltimoTicket
    #   - Descripción: Método que lanza al pulsar en el boton de ultimo ticket
    #                  Lee de la base de datos el ultimo registro y lo imprime.
    #==================================================================================
    def onUltimoTicket(self):
        ticketBD = Base_Datos()
        self.ticket, self.detalleticket = ticketBD.LeerUltimoTicket()
        
        imprimirticket = Imprimir(self.ticket, self.detalleticket)
        imprimirticket.Ticket()
        self.CargarTicketenMostrarTicket(self.ticket,self.detalleticket)

    #==================================================================================
    # Método onBuscar
    #   - Descripción: Método que lanza al pulsar en el boton de buscar
    #                  Lee los textedit y si  
    #==================================================================================
    def onBuscar(self):
        numeroticket = 0
        if self.txtNum.text() == "":
            if self.txtFecha.text() != "":
                self.Tabla = self.LeerDatosPorFecha(self.txtFecha.text())
            else:
                self.Tabla=self.LeerDatosPorNumero(numeroticket)
        else:
            numeroticket = int(float(self.txtNum.text())) #Si meten un decimal que lo corrija, para eso es el doble cacheo
            self.Tabla=self.LeerDatosPorNumero(numeroticket)
           
        self.CargarDatosTabla(self.Tabla)


        self.txtNum.setText("") #Limpiamos el txt de numero de ticket
        self.txtFecha.setText("") #Limpiamos el txt de fecha
    
    #==================================================================================
    # Método onImprimir
    #   - Descripción: Método que lanza al pulsar en el boton de imprimir
    #                  y se lanza a la impresora el ticket que este visualizado 
    #==================================================================================
    def onImprimir(self):
        if self.ticket != 0 and self.detalleticket != 0:
            imprimirticket = Imprimir(self.ticket, self.detalleticket)
            imprimirticket.Ticket()
        
    #==================================================================================
    # Método onImprimirHoy
    #   - Descripción: Método que lanza al pulsar en el boton de imprimir todas las ventas del día
    #                  y se lanza a la impresora un resumen de las ventas
    #==================================================================================
    def onImprimirHoy(self):
        fecha_hora = datetime.now()
        db = Base_Datos()
        tabla = db.consultaTicketPorFecha(fecha_hora.strftime("%d/%m/%Y"))
        
        imprimirlista = Imprimir()
        imprimirlista.Lista(fecha_hora.strftime("%d/%m/%Y"),tabla)

    #==================================================================================
    # Método onImprimirTabla
    #   - Descripción: Método que lanza al pulsar en el boton de imprimir listado
    #                  y se lanza a la impresora el listado de las ventas que están en la tabla
    #==================================================================================
    def onImprimirTabla(self):
        db = Base_Datos()
        tabla = db.consultaListaTicketPorNumero(self.Tabla)
        db.ConexionBD.close()

        if (tabla[0][5] != tabla[-1][5]):   #Si es el listado completo de ticket NO LO IMPRIMIR,
            QtWidgets.QMessageBox.warning(self,"NO IMPRIMIR","No puedo imprimir todos los ticket, reduce la busqueda por fechas", QtWidgets.QMessageBox.Ok)
            return                          #la verificación la hago comparado la primera fecha y la ultima

        imprimirlista = Imprimir()
        imprimirlista.Lista(tabla[0][5],tabla)

            
        
        
        



        


