# -*- coding: utf-8 -*-
from VentanaMensaje import VentanaMensaje
from Apagar import Apagar_o_Cerrar
from Informes import Informes
from BaseDatos import Base_Datos
from datetime import datetime
from ImprimirTicket import Imprimir
from BotonProductos import BotonProductos
from Config import Vent_Config
from BorrarCE import VentBorrar
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Defaulf
import json
import os.path
import os


#=============================================
NombreApp = "TPVRaspy"
Programador = "José Ramón Blanco Gutiérrez"
Version = "1.1.2021"
#=============================================

class Principal(QtWidgets.QMainWindow): 
    #============================================================================
    # Constructor
    #============================================================================
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.resize(1024, 599)
        self.setWindowTitle("TPV Blanco Joyeros")
        self.centralwidget = QtWidgets.QWidget(self)

        #-----------------------------------------------------------------
        # Configuracion -> Es el diccionario que contiene la configuración del programa
        #              Los Botones de los productos, temas fiscales, Impresora de ticket...
        #              Nada más empezar cargamos el fichero json y en caso de que
        #              no existiera pues le creamos con la escrutura por defecto
        #              y vacio.
        #------------------------------------------------------------------
        if os.path.isfile("config.json"):
            self.Configuracion = self.leerJSON("config.json")
        else:
            QtWidgets.QMessageBox.information(self,"Fichero",
                        'No se encuentra el fichero "config.json"\nSe crea uno nuevo con la configuración por defecto.\n\n Programador:\nJosé Ramón Blanco Gutiérrez',
                        QtWidgets.QMessageBox.Close)
            self.Configuracion = Defaulf.configuracion_inicial #En caso de no existir el se cra con los datos por defecto.
            self.GuardarJSON("config.json",self.Configuracion)

        #Variable para controlar el teclado
        self.numeroDecimal = False

        #------------------------------------------------------------
        #El Menú y los botones
        self.menu_Ui()
        #------------------------------------------------------------

        #------------------------------------------------------------
        #El grupo de Forma de Pago y los RadioButton
        self.grupoFormaDePago_Ui()
        #------------------------------------------------------------

        #------------------------------------------------------------
        #El grupo de los botones de teclado
        self.teclado_Ui()
        #------------------------------------------------------------

        #------------------------------------------------------------
        #Los Edit de Concepto e Importe superiores
        self.introducirConceptoImporte_Ui()
        #------------------------------------------------------------

        #------------------------------------------------------------
        #Los Edit para mostrar la suma del ticket, iva y total
        self.totalesDelTicket_Ui()
        #------------------------------------------------------------
        
        #-----------------------------------------------------------
        #Los Tab y los botones de los productos
        self.seccionBtnsProductos_Ui()
        #------------------------------------------------------------        
        
        #-----------------------------------------------------------
        # Tabla de la ventas
        self.tablaDeVentas()
        #-----------------------------------------------------------
               
        self.setCentralWidget(self.centralwidget)
      
    #==============================================================================
    # Menú principal
    #   - Descripción: Menú donde estan las funciones principales de la TPV
    #==============================================================================
    def menu_Ui(self):
        #---- Variables para este método
        font = QtGui.QFont()
        #-------------------------------
        self.grpMenu = QtWidgets.QGroupBox(self.centralwidget)
        self.grpMenu.setGeometry(QtCore.QRect(3, 0, 101, 579))
        
        font.setPointSize(10)
        self.grpMenu.setFont(font)
        self.grpMenu.setTitle("Menú")
        self.grpMenu.setAlignment(QtCore.Qt.AlignCenter)

        #------- Boton Imprimir ticket -------
        self.btnImprimir = QtWidgets.QToolButton(self.grpMenu)
        self.btnImprimir.setEnabled(True)
        self.btnImprimir.setGeometry(QtCore.QRect(10, 30, 81, 92))
        self.btnImprimir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnImprimir.setText("IMPRIMIR")  
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("Iconos/imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnImprimir.setIcon(icono)
        self.btnImprimir.setIconSize(QtCore.QSize(54, 54))
        self.btnImprimir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        #------- Boton Guardar -------
        self.btnGuardar = QtWidgets.QToolButton(self.grpMenu)
        self.btnGuardar.setEnabled(True)
        self.btnGuardar.setGeometry(QtCore.QRect(10, 130, 81, 92))
        self.btnGuardar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnGuardar.setText("Guardar")
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("Iconos/disquete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icono)
        self.btnGuardar.setIconSize(QtCore.QSize(54, 54))
        self.btnGuardar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        #------- Separador -------
        self.line = QtWidgets.QFrame(self.grpMenu)
        self.line.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)


        #------- Boton Buscar Ticket -------
        self.btnBuscarT = QtWidgets.QToolButton(self.grpMenu)
        self.btnBuscarT.setEnabled(True)
        self.btnBuscarT.setGeometry(QtCore.QRect(10, 270, 81, 92))
        self.btnBuscarT.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnBuscarT.setText("Informes")
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("Iconos/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarT.setIcon(icono)
        self.btnBuscarT.setIconSize(QtCore.QSize(54, 54))
        self.btnBuscarT.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnBuscarT.setAutoRaise(False)

        #------- Boton Configurar -------
        self.btnConfig = QtWidgets.QToolButton(self.grpMenu)
        self.btnConfig.setEnabled(True)
        self.btnConfig.setGeometry(QtCore.QRect(10, 370, 81, 92))
        self.btnConfig.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnConfig.setText("Config.")
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("Iconos/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfig.setIcon(icono)
        self.btnConfig.setIconSize(QtCore.QSize(64, 64))
        self.btnConfig.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        #------- Boton Salir del programa -------
        self.btnSalir = QtWidgets.QToolButton(self.grpMenu)
        self.btnSalir.setEnabled(True)
        self.btnSalir.setGeometry(QtCore.QRect(10, 470, 81, 92))
        self.btnSalir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnSalir.setText("SALIR")
        icono = QtGui.QIcon()
        icono.addPixmap(QtGui.QPixmap("Iconos/iu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icono)
        self.btnSalir.setIconSize(QtCore.QSize(64, 64))
        self.btnSalir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)      

        #-----------------------------------------------------
        # EVENTOS de los BOTONES
        #-----------------------------------------------------
        self.btnSalir.clicked.connect(lambda: QtWidgets.QApplication.closeAllWindows())
        self.btnConfig.clicked.connect(self.onBotonConfig)
        self.btnImprimir.clicked.connect(self.onBotonImprimir)
        self.btnGuardar.clicked.connect(self.on_Boton_Guardar)
        self.btnBuscarT.clicked.connect(self.onBotonInformes)
        
    #===============================================================================
    # Grupo Forma de Pago
    #   - Descripción: Es el grupo donde se selecciona como es la forma de pago
    #===============================================================================
    def grupoFormaDePago_Ui(self):
        self.grpFormaPago = QtWidgets.QGroupBox(self.centralwidget)
        self.grpFormaPago.setGeometry(QtCore.QRect(775, 350, 240, 223))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.grpFormaPago.setFont(font)
        self.grpFormaPago.setTitle("Forma de pago")
        self.layoutWidget = QtWidgets.QWidget(self.grpFormaPago)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 231, 186))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        #------- Boton de Pago en Efectivo o al contado -------
        self.rbtnEfectivo = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtnEfectivo.setFont(font)
        self.rbtnEfectivo.setText("Al Contado")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbtnEfectivo.setIcon(icon)
        self.rbtnEfectivo.setIconSize(QtCore.QSize(64, 64))
        # self.rbtnEfectivo.setCheckable(False)
        # print(self.rbtnEfectivo.isChecked())
        # self.rbtnEfectivo.setChecked(True)
        # print(self.rbtnEfectivo.isChecked())
        
        self.verticalLayout.addWidget(self.rbtnEfectivo)

        #------- Boton de pago con tarjeta de credito/debito -------
        self.rbtnTarjeta = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtnTarjeta.setFont(font)
        self.rbtnTarjeta.setText("Tarjeta de crédito")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbtnTarjeta.setIcon(icon1)
        self.rbtnTarjeta.setIconSize(QtCore.QSize(54, 54))
        self.verticalLayout.addWidget(self.rbtnTarjeta)

        #------- Boton de pago con Vales de Blanco Joyeros -------
        self.rbtnVales = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtnVales.setFont(font)
        self.rbtnVales.setText("Vales ahorro")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Iconos/vales.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbtnVales.setIcon(icon2)
        self.rbtnVales.setIconSize(QtCore.QSize(64, 64))
        self.verticalLayout.addWidget(self.rbtnVales)

    #=================================================================================
    # Grupo de botones del teclado numérico
    #   - Descripción: El teclado numérico para introducir los importes y los botones dee 
    #                   borrar y de OK
    #=================================================================================
    def teclado_Ui(self):
        self.gridLayoutWidgetTeclado = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidgetTeclado.setGeometry(QtCore.QRect(770, 10, 251, 332))
        self.gridTeclado = QtWidgets.QGridLayout(self.gridLayoutWidgetTeclado)
        self.gridTeclado.setContentsMargins(0, 0, 0, 0)
        self.gridTeclado.setSpacing(5)

        iconos = ("Iconos/uno54.png","Iconos/dos54.png","Iconos/tres54.png","Iconos/cuatro54.png",
                  "Iconos/cinco54.png","Iconos/seis54.png","Iconos/siete54.png","Iconos/ocho54.png",
                  "Iconos/nueve54.png","Iconos/borrar54.png","Iconos/cero54.png","Iconos/punto54.png",
                  "Iconos/okay54.png")
        
        #------------------------------------------------------------
        #Lista de los botones del teclado numerico
        #------------------------------------------------------------
        self.btn = []

        #------------------------------------------------------------
        #Bucle for que crea los botones 1,2,3,4,5,6,7,8,9,borrar,0,.,ok
        #------------------------------------------------------------
        fila = 1
        columna = 0
        for c,i in enumerate(iconos):
            self.btn.append(QtWidgets.QPushButton(self.gridLayoutWidgetTeclado))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(i), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btn[c].setIcon(icon)
            self.btn[c].setIconSize(QtCore.QSize(54, 54))
            self.btn[c].setWhatsThis(str(c+1))
            self.btn[c].clicked.connect(self.onBotonTeclado)
            if i == "Iconos/okay54.png":
                self.gridTeclado.addWidget(self.btn[c], 0, 0, 1, 3)
            else:
                self.gridTeclado.addWidget(self.btn[c], fila, columna, 1, 1)
            columna += 1
            if columna > 2:
                fila += 1
                columna = 0

    #=================================================================================
    # Grupo de los Edit de Concepto e Importe
    #   - Descripción: Son los edit superiores donde se va a mostrar la venta antes de 
    #                  almacenarla en la tabla
    #=================================================================================
    def introducirConceptoImporte_Ui(self):
        font = QtGui.QFont()
        font.setPointSize(12)

        self.lbConcepto = QtWidgets.QLabel(self.centralwidget)
        self.lbConcepto.setGeometry(QtCore.QRect(110, 4, 131, 16))
        self.lbConcepto.setFont(font)
        self.lbConcepto.setText("Concepto")

        self.lbImporte = QtWidgets.QLabel(self.centralwidget)
        self.lbImporte.setGeometry(QtCore.QRect(650, 4, 81, 16))
        font.setPointSize(12)
        self.lbImporte.setFont(font)
        self.lbImporte.setText("Importe")

        self.txtConcepto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtConcepto.setGeometry(QtCore.QRect(110, 20, 531, 41))
        font.setPointSize(18)
        self.txtConcepto.setFont(font)

        self.txtImporte = QtWidgets.QLineEdit(self.centralwidget)
        self.txtImporte.setGeometry(QtCore.QRect(650, 20, 111, 41))
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.txtImporte.setFont(font)
        self.txtImporte.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.txtImporte.setAutoFillBackground(False)
        self.txtImporte.setAlignment(QtCore.Qt.AlignCenter)
        self.txtImporte.setValidator(QtGui.QDoubleValidator())   #Al lineText le pone que solo adminita numero decimales
    
    #=============================================================================
    # Grupo de los Edit de totales del ticket
    #   - Descripción: Son los edit en los cuales se muestra la suma total de los 
    #                  productos, el iva y el TOTAL del ticket
    #==============================================================================
    def totalesDelTicket_Ui(self):
        font = QtGui.QFont()

        self.lbSuma = QtWidgets.QLabel(self.centralwidget)
        self.lbSuma.setGeometry(QtCore.QRect(650, 70, 111, 16))
        font.setPointSize(12)
        self.lbSuma.setFont(font)
        self.lbSuma.setText("Suma ticket")

        self.lbIVA = QtWidgets.QLabel(self.centralwidget)
        self.lbIVA.setGeometry(QtCore.QRect(650, 130, 111, 16))
        font.setPointSize(12)
        self.lbIVA.setFont(font)
        self.lbIVA.setText("IVA " + str(self.Configuracion["Configuración"]["IvaPorcentaje"]) + "%") 

        self.lbTotal = QtWidgets.QLabel(self.centralwidget)
        self.lbTotal.setGeometry(QtCore.QRect(650, 190, 111, 16))
        font.setPointSize(12)
        self.lbTotal.setFont(font)
        self.lbTotal.setText("TOTAL TICKET")
        self.lbTotal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbTotal.setIndent(0)

        self.txtSuma = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSuma.setGeometry(QtCore.QRect(650, 90, 113, 31))
        self.txtSuma.setAlignment(QtCore.Qt.AlignCenter)
        self.txtSuma.setReadOnly(True)

        self.txtIva = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIva.setGeometry(QtCore.QRect(650, 150, 113, 31))
        self.txtIva.setAlignment(QtCore.Qt.AlignCenter)
        self.txtIva.setReadOnly(True)
        
        self.txtTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(650, 210, 113, 31))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.txtTotal.setFont(font)
        self.txtTotal.setStyleSheet("color: rgb(255, 0, 0);")
        self.txtTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.txtTotal.setReadOnly(True)

        if not self.Configuracion["Configuración"]["Iva"]: #Si no esta activado el IVA ocultamos todo menos TOTAL
            self.lbSuma.hide()
            self.txtSuma.hide()
            self.lbIVA.hide()
            self.txtIva.hide()

    #===================================================================================
    # Sección de los productos
    #   - Descripción: Es un TAB con los tres tipos de grupos de productos que se venden
    #                   Taller, Joyería y Relojería 
    #===================================================================================
    def seccionBtnsProductos_Ui(self):
        #----------- Crear el TAB General
        self.tabProductos = QtWidgets.QTabWidget(self.centralwidget)
        self.tabProductos.setGeometry(QtCore.QRect(110, 250, 651, 328))
        self.tabProductos.setTabShape(QtWidgets.QTabWidget.Rounded)
        
        #----- Primera etiqueta Taller
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabProductos.setFont(font)
        self.tabTaller = QtWidgets.QWidget()
        self.gridLayoutWidget_Taller = QtWidgets.QWidget(self.tabTaller)
        self.gridLayoutWidget_Taller.setGeometry(QtCore.QRect(0, 0, 641, 281))
        self.gridTaller = QtWidgets.QGridLayout(self.gridLayoutWidget_Taller)
        self.gridTaller.setContentsMargins(0, 0, 0, 0)
        self.tabProductos.addTab(self.tabTaller, "Taller")

        #----------------------------------------------------------
        #----- Creamos los botones para la sección de Taller ------
        #----------------------------------------------------------
        self.BotonesProductosTaller = []
        
        for pt in self.Configuracion["Taller"]:
            self.BotonesProductosTaller.append(BotonProductos(self.gridLayoutWidget_Taller, self.Configuracion["Taller"][pt]['nombre'],
                                               self.Configuracion["Taller"][pt]['concepto'], self.Configuracion["Taller"][pt]['importe'],
                                               self.Configuracion["Taller"][pt]['activado'], self.Configuracion["Taller"][pt]['icono']))

        posx, posy = 0,0
        for objeto in self.BotonesProductosTaller:
              #Añadimos en el TAB
              self.gridTaller.addWidget(objeto, posy, posx)
              objeto.clicked.connect(self.onBotonProductos) #Conectamos con Método que se lanza al pulsar el botón
              if posx == 7:
                   posx = 0
                   posy += 1
              else:
                   posx += 1


        self.tabJoyeria = QtWidgets.QWidget()
        self.gridLayoutWidget_Joyeria = QtWidgets.QWidget(self.tabJoyeria)
        self.gridLayoutWidget_Joyeria.setGeometry(QtCore.QRect(0, 0, 641, 281))
        self.gridJoyeria = QtWidgets.QGridLayout(self.gridLayoutWidget_Joyeria)
        self.gridJoyeria.setContentsMargins(0, 0, 0, 0)
        self.tabProductos.addTab(self.tabJoyeria, "Joyería")

        #--------------------------------------------------------------------------
        #----- Creamos los botones para la sección de Productos de Joyería --------
        #--------------------------------------------------------------------------
        self.BotonesProductosJoyeria = []
        
        for pt in self.Configuracion["Joyería"]:
            self.BotonesProductosJoyeria.append(BotonProductos(self.gridLayoutWidget_Joyeria, self.Configuracion["Joyería"][pt]['nombre'],
                                               self.Configuracion["Joyería"][pt]['concepto'], self.Configuracion["Joyería"][pt]['importe'],
                                               self.Configuracion["Joyería"][pt]['activado'], self.Configuracion["Joyería"][pt]['icono']))

        posx, posy = 0,0
        for objeto in self.BotonesProductosJoyeria:
              #Añadimos en el TAB
              self.gridJoyeria.addWidget(objeto, posy, posx)
              objeto.clicked.connect(self.onBotonProductos)
              if posx == 7:
                   posx = 0
                   posy += 1
              else:
                   posx += 1

        self.tabReloj = QtWidgets.QWidget()
        self.gridLayoutWidget_Relojeria = QtWidgets.QWidget(self.tabReloj)
        self.gridLayoutWidget_Relojeria.setGeometry(QtCore.QRect(0, 0, 641, 281))
        self.gridRelojeria = QtWidgets.QGridLayout(self.gridLayoutWidget_Relojeria)
        self.gridRelojeria.setContentsMargins(0, 0, 0, 0)
        self.tabProductos.addTab(self.tabReloj, "Relojería")

        #--------------------------------------------------------------------------
        #----- Creamos los botones para la sección de Productos de Relojería ------
        #--------------------------------------------------------------------------
        self.BotonesProductosRelojeria = []
        
        for pt in self.Configuracion["Relojería"]:
            self.BotonesProductosRelojeria.append(BotonProductos(self.gridLayoutWidget_Relojeria, self.Configuracion["Relojería"][pt]['nombre'],
                                               self.Configuracion["Relojería"][pt]['concepto'], self.Configuracion["Relojería"][pt]['importe'],
                                               self.Configuracion["Relojería"][pt]['activado'], self.Configuracion["Relojería"][pt]['icono']))

        posx, posy = 0,0
        for objeto in self.BotonesProductosRelojeria:
              #Añadimos en el TAB
              self.gridRelojeria.addWidget(objeto, posy, posx)
              objeto.clicked.connect(self.onBotonProductos)
              if posx == 7:
                   posx = 0
                   posy += 1
              else:
                   posx += 1
        
        self.tabProductos.setCurrentIndex(0) #Por defecto el primero de los tab

    #==========================================================
    # Tabla de Ventas del Ticket
    #       - Descripción: Tabla principal donde se colocan las ventas
    #                       de un ticket.
    #==========================================================
    def tablaDeVentas(self):
        self.TablaVentas = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaVentas.setGeometry(QtCore.QRect(110, 70, 531, 171))
        self.TablaVentas.setWhatsThis("")
        self.TablaVentas.setColumnCount(2)
        #self.TablaVentas.setRowCount(0)
        self.TablaVentas.setColumnWidth(0, 405) #Tamaño de la primera columna
        #------------------------------
        # Seleccionar toda la fila
        self.TablaVentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #------------------------------
        # Seleccionar una fila a la vez
        self.TablaVentas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Concepto")
        font = QtGui.QFont()
        font.setPointSize(16)
        item.setFont(font)
        self.TablaVentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Importe")
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.TablaVentas.setHorizontalHeaderItem(1, item)

        #--------------------
        #Array para los datos de las Ventas
        # que se va llenado a medida que se van
        # introduciendo ventas con el botón OK 
        #--------------------
        self.datosVentas = []

    #==================================================================================
    # Método del BOTON OK
    #   - Descripción: Dado que el botón OK tiene un comportamiento diferente al resto de 
    #                  los botones he creado un método diferente.
    #                  Dicho comportamiento es de verificación e introducción de los edit 
    #                  "txtconcepto" y "txtimporte" en la la tablaVentas.
    #==================================================================================
    def onBoton_OK(self):
            #Si hay datos en ambos Text continua
        if (len(self.txtConcepto.text()) != 0) and (len(self.txtImporte.text()) != 0):
            #---Añade a la lista de Ventas el concepto y el importe
            self.datosVentas.append([self.txtConcepto.text(),self.txtImporte.text()])
            #establece el tamaño de la tabla en función del tamaño de array
            self.TablaVentas.setRowCount(len(self.datosVentas))
            for columna in range(2):
                for fila in range(len(self.datosVentas)):
                    elementoTabla = QtWidgets.QTableWidgetItem(self.datosVentas[fila][columna])
                    elementoTabla.setTextAlignment(0x0084)
                    self.TablaVentas.setItem(fila,columna,elementoTabla)
            #Se borra los textedit de Concepto y de Importe
            self.txtConcepto.setText("")
            self.txtImporte.setText("")
            #Se llama al metodo que Calcula los totales del ticket
            self.calculaTotalTicket()
        else:
            if len(self.txtConcepto.text()) == 0:
                QtWidgets.QMessageBox.warning(self,"ERROR","Tienes que introducir un Concepto", QtWidgets.QMessageBox.Ok)
            if len(self.txtImporte.text()) == 0:
                QtWidgets.QMessageBox.warning(self,"ERROR","Tienes que introducir un Importe", QtWidgets.QMessageBox.Ok)
            
    #==================================================================================
    # Método calculaTotalTicket
    #   - Descripción: Método que hace la suma de todos los importes de la tabla de ventas
    #                   y los suma, despues calcula el 21% de IVA y general el total
    #                   del ticket. 
    #==================================================================================
    def calculaTotalTicket(self):
        sumaimporte = 0
        iva = 0
        total = 0
        for importes in self.datosVentas:
            sumaimporte += float(importes[1])

        if self.Configuracion["Configuración"]["Iva"] == False: #Si está desactivado el IVA no le calcula y mete un cero
            iva=0
        else: 
            porcentajeIVA = self.Configuracion["Configuración"]["IvaPorcentaje"] / 100
            iva = round(sumaimporte * porcentajeIVA, 2) #Redondea a 2 decimales
        
        total = round(sumaimporte + iva, 2)

        self.txtSuma.setText(str(round(sumaimporte, 2)))
        self.txtIva.setText(str(iva))
        self.txtTotal.setText(str(total))

    #==================================================================================
    # Método onBotonImprimir
    #   - Descripción: Método que lanza ek imprimir el ticket
    #==================================================================================
   
    def onBotonImprimir(self):
        formadepago = self.getFormadePago()
        if len(self.datosVentas) != 0 and formadepago != 0:
            #---------------------------
            # 1º Guardamos em la base de datos.
            #--------------------------- 
            self.guardarDatos()
            #---------------------------
            # 2º Imprimimos el ticket que es el ultimo de la base de datos
            #--------------------------- 
            DataBase = Base_Datos()
            ticket,detalleticket = DataBase.LeerUltimoTicket()

            imprimirticket = Imprimir(ticket, detalleticket)
            imprimirticket.Ticket()
            #---------------------------
            # 3º Limpiamos los datos
            #---------------------------
            self.borrarTodo()
            VentanaMensaje("info","Imprimiendo", "Ticket Guardado e Imprimiendo...")
        elif len(self.datosVentas) == 0:
            VentanaMensaje("aviso","Error", "No hay en el TICKET nada para imprimir")
        elif formadepago == 0:
            VentanaMensaje("aviso","AVISO", "Seleciona la FORMA DE PAGO.")
    
    #==================================================================================
    # Método on_Boton_Guardar
    #   - Descripción: Método que se lanza al pulsar el botón de guardar.
    #                  Si hay datos los guarda en la base de datos y despues limpia todo
    #==================================================================================   
    def on_Boton_Guardar(self):
        formadepago = self.getFormadePago()
        if len(self.datosVentas) != 0 and formadepago != 0:
            self.guardarDatos()
            self.borrarTodo() #Una vez guardado limpiamos y reiniciamos ticket
            VentanaMensaje("info","Guardado", "El Ticket se ha guardado correctamente")
        elif len(self.datosVentas) == 0:
            VentanaMensaje("aviso","Error", "No hay en el TICKET nada para guardar")
        elif formadepago == 0:
            VentanaMensaje("aviso","AVISO", "Seleciona la FORMA DE PAGO.")
            

    #==================================================================================
    # Método getFormadePago
    #   - Descripción: Método que devuelve como estan los checkbotton de la forma de pago
    #                   devuelven en forma de string el estado o 0 sino se ha seleccionado
    #                   ninguno. 
    #==================================================================================   
    def getFormadePago(self):
        if self.rbtnEfectivo.isChecked():
            return "Al contado"
        elif self.rbtnTarjeta.isChecked():
            return "Tarjeta de crédito/Débito"
        elif self.rbtnVales.isChecked():
            return "Vales de ahorro"
        else:
            return 0
    #==================================================================================
    # Método guardarDatos
    #   - Descripción: Método que guarda directamente en la base de datos.
    #==================================================================================
    def guardarDatos(self):
        fecha_hora = datetime.now() #Se obtiene del sistema la fecha y la hora
        formadepago = self.getFormadePago()

        DataBase = Base_Datos()
        DataBase.guardarNuevoTicket(fecha_hora.strftime("%d/%m/%Y"), #la fecha con el formato DD/MM/AAAA
                            fecha_hora.strftime("%H:%M"), #la hora con el formado HH:MM
                            formadepago,
                            self.txtSuma.text(),
                            self.txtIva.text(),
                            self.txtTotal.text(),
                            self.datosVentas)

    #==========================================================
    # Metodo que gentiona los botones de las zonas de ventas
    #       Descripción: Es el metodo que al ser pulsado el producto introduce en
    #                    el textedit de Concepto e Importe
    #==========================================================
    def onBotonProductos(self):
        e = self.sender()
        if isinstance(e, BotonProductos):
            #En un textedit añadimos
            datosdelboton= e.getDatos() #tupla con los datos de concepto(0) e importe(1)
            self.txtConcepto.setText(datosdelboton[0])
            if datosdelboton[1] == 0:
                self.txtImporte.setText("")
            else:
                self.txtImporte.setText(str(datosdelboton[1]))
            #if (datosdelboton[0] == "Varias composturas de joyería"): #Por si quiero lanzar algo concreto...
                

    #================================================================================
    #   - Descripción: método para controlar y gestionar las teclas pulsadas en los 
    #                  botones de la pantalla tactil.
    #                  Y va introduciendo el número que se genera en el edit txtImporte.
    #
    #   - Nota: Desde este método se llama al método de control del botón OK
    #================================================================================
    def onBotonTeclado(self):
        e = self.sender()
        #if isinstance(e, QtWidgets.QPushButton):
        valor = e.whatsThis()
        if valor == "11":
            valor = "0"
        if valor == "12":
            valor = "."

        #---- Borrar Importe y Concepto ----
        if valor == "10":
            self.onBoton_CE() 
            return #Se termina este metodo ya que es de borrar

        #---- Botón OK ----
        if valor == "13": #Botón de OK
            self.onBoton_OK() #Se llama al método que controla el botón OK
            return #Se termina este método onBotonTeclado ya que al pulsar OK este tiene otra finalidad

        if not((valor == ".") and (self.numeroDecimal)):
            if (valor == ".") and (self.txtImporte.text() == ""):
                self.txtImporte.setText("0.")
                self.numeroDecimal = True
            else:
                if self.txtImporte.text() == "":
                    self.txtImporte.setText(valor)
                else:
                    if valor == ".":
                        self.txtImporte.setText(self.txtImporte.text()+".")
                        self.numeroDecimal = True
                    else:
                        self.txtImporte.setText(self.txtImporte.text()+valor)
            
    #=================================================================================
    # Método del BOTON Borrar
    #   - Descripción: Dado que el botón CE tiene un comportamiento diferente al resto 
    #                  de los botones he creado un método diferente, en el cual muestra
    #                  una ventana de dialogo que pregunta que es lo que se tiene que borrar
    #                  y así se controla todo el borrado de la aplicación.
    #=================================================================================
    def onBoton_CE(self):
        windowBorrar = VentBorrar(self)
        windowBorrar.exec_()
        
        CE = windowBorrar.get_CE() #Se llama al método getter

        if CE == 1:
            self.txtImporte.setText("") #Borrar el contenido de importe
            self.numeroDecimal = False
        elif CE == 2:
            self.txtConcepto.setText("") #Borrar el contenido de concepto
            self.txtImporte.setText("") #Borrar el contenido de importe
            self.numeroDecimal = False
        elif CE == 3:
            self.borrarTodo()

    #================================================================
    # Método del BOTON Borrar
    #   - Descripción: Borra todo el ticket y reinicia variables y listas
    #================================================================
    def borrarTodo(self):
        self.txtConcepto.setText("") #Borrar el contenido de concepto
        self.txtImporte.setText("") #Borrar el contenido de importe
        self.txtSuma.setText("")
        self.txtIva.setText("")
        self.txtTotal.setText("")
        self.numeroDecimal = False
        self.datosVentas.clear()  #Borra todo el contenido de la Lista de datos
        for fila in range(0, self.TablaVentas.rowCount()): #Borra toda la tabla
            self.TablaVentas.removeRow(0)
        #Desacctivamos todos los radiobutton de la forma de pago y les volvemos a activar
        self.rbtnEfectivo.setCheckable(False)
        self.rbtnEfectivo.setCheckable(True)
        self.rbtnTarjeta.setCheckable(False)
        self.rbtnTarjeta.setCheckable(True)
        self.rbtnVales.setCheckable(False)
        self.rbtnVales.setCheckable(True)
    
        

    #=================================================================================
    # Método del BOTON de Configurar
    #   - Descripción: Lanza la ventana de dialogo en la cual se configura el programa
    #=================================================================================
    def onBotonConfig(self):
        windowConfig = Vent_Config(self,diccionario=self.Configuracion)
        windowConfig.exec_()

        #------------------------------------------------------------------------------
        # Actualizamos los Productos del dicionario principal con los del diccionario que han sido supuestamente
        # modificados en la ventada de configuración
        #------------------------------------------------------------------------------
        self.Configuracion = windowConfig.datos

        #Guardamos en el fichero JSON la configuración de los productos
        self.GuardarJSON("config.json", self.Configuracion)

        #Recargamos los botones de los productos con la información cambiada

        if windowConfig.getCambioDeDatos():
            #----------------------------------------------------------------------------------
            # Actualizamos todos los datps de los botones para que se apliquen todos los cambio
            #----------------------------------------------------------------------------------
            for cont,pt in enumerate(self.Configuracion["Taller"]): #Productos de Taller
                self.BotonesProductosTaller[cont].setDatos(self.Configuracion["Taller"][pt]['nombre'], self.Configuracion["Taller"][pt]['concepto'],
                                                            self.Configuracion["Taller"][pt]['importe'],self.Configuracion["Taller"][pt]['activado'],
                                                            self.Configuracion["Taller"][pt]['icono'])
            
                self.BotonesProductosTaller[cont].actualizaBoton()  

            for cont,pj in enumerate(self.Configuracion["Joyería"]): #Productos de Joyería
                self.BotonesProductosJoyeria[cont].setDatos(self.Configuracion["Joyería"][pj]['nombre'], self.Configuracion["Joyería"][pj]['concepto'],
                                                            self.Configuracion["Joyería"][pj]['importe'],self.Configuracion["Joyería"][pj]['activado'],
                                                            self.Configuracion["Joyería"][pj]['icono'])
            
                self.BotonesProductosJoyeria[cont].actualizaBoton() 

            for cont,pr in enumerate(self.Configuracion["Relojería"]): #Productos de Relojería
                self.BotonesProductosRelojeria[cont].setDatos(self.Configuracion["Relojería"][pr]['nombre'], self.Configuracion["Relojería"][pr]['concepto'],
                                                            self.Configuracion["Relojería"][pr]['importe'],self.Configuracion["Relojería"][pr]['activado'],
                                                            self.Configuracion["Relojería"][pr]['icono'])
            
                self.BotonesProductosRelojeria[cont].actualizaBoton() 
            
            #--------------
            #Vuelve a comprobar si tiene que calcular o no el IVA
            # -------------
            if self.Configuracion["Configuración"]["Iva"]: #Si esta activado el IVA mostramos todo sino lo ocultamos
                self.lbSuma.show()
                self.txtSuma.show()
                self.lbIVA.setText("IVA " + str(self.Configuracion["Configuración"]["IvaPorcentaje"]) + "%")
                self.lbIVA.show()
                self.txtIva.show() 
            else:
                self.lbSuma.hide()
                self.txtSuma.hide()
                self.lbIVA.hide()
                self.txtIva.hide() 

    #=================================================================================
    # Método del BOTON de Informes
    #   - Descripción: Lanza la ventana de dialogo en la cual se pueden generar
    #                   diferentes informes de los tickets 
    #=================================================================================
    def onBotonInformes(self):
        windowInformes = Informes(self)
        windowInformes.exec_()
   
    #====================================================
    # Método del evento de cerrar.
    #   - Descripción: Pregunta antes de cerrar la aplicación
    #==================================================== 
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        windowApagar = Apagar_o_Cerrar()
        windowApagar.exec_()

        if windowApagar.resultado == 1:
            event.accept()
        elif windowApagar.resultado == 0:
            event.ignore()
        elif windowApagar.resultado == 2:
            event.accept()
            os.system("shutdown now")

    def leerJSON(self,nombrefichero):
        with open(nombrefichero,'r') as file:
            fichero_json = json.load(file)
        return fichero_json

    def GuardarJSON(self,nombrefichero,diccionarioJSON):
        with open(nombrefichero, 'w') as file:
            json.dump(diccionarioJSON, file)


  
#====================================================
# Función PRINCIPAL de la Aplicación que lanza la
# Ventanta principal
#==================================================== 
def main(Principal):
    print("Iniciando", NombreApp, "versión:", Version, "\nPor:", Programador)
    app = QtWidgets.QApplication(sys.argv)
    window = Principal()
    #window.showFullScreen()    #A pantalla completa
    window.show()               #Ventana normal
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(Principal)