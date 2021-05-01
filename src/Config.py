# -*- coding: utf-8 -*-

import os.path, json

from PyQt5 import QtCore, QtGui, QtWidgets


#==============================================================================
# Clase Vent_Config
#   - Descripcion: Esta clase quea una ventana de dialogo en la
#
#   - Funcionamiento:
#                       from BorrarCE import Vent_Config 
# 
#                       nombre = Vent_Config(self, diccionario) <--- Se le tiene que pasar el padre
#                       nombre.exec_()
#   - NOTA:
#           diccionario: Es el Diccionario de la clase principal donde se guardan
#                        los productos de los botones.
#==============================================================================
class Vent_Config(QtWidgets.QDialog):
    

    def __init__(self, parent=None,diccionario=""):
        QtWidgets.QDialog.__init__(self, parent)
        
        #-----------------------------------------------------------
        #Creamos una variable para los productos y la iniciamos con 
        # los productos que se pasan en la inicialización de la clase
        #-----------------------------------------------------------
        self.datos = diccionario
        self.__cambioDeDatos = False
        
        self.__setupUi()

        self.cargarDatosConfiguracion()


    def __setupUi(self):
        font = QtGui.QFont()

        self.resize(527, 380)
        self.setMinimumSize(QtCore.QSize(527, 380))
        self.setMaximumSize(QtCore.QSize(527, 380))
        self.setWindowTitle("Configuración")
     
        self.tabConfig = QtWidgets.QTabWidget(self)
        self.tabConfig.setGeometry(QtCore.QRect(12, 6, 501, 321))
        self.tabProductos = QtWidgets.QWidget()
    
        self.txtImporte = QtWidgets.QLineEdit(self.tabProductos)
        self.txtImporte.setEnabled(False)
        self.txtImporte.setGeometry(QtCore.QRect(370, 230, 111, 41))
        
        font.setPointSize(20)
        self.txtImporte.setFont(font)
        self.txtImporte.setValidator(QtGui.QDoubleValidator())   #Al lineText le pone que solo adminita numero decimales
        # self.txtImporte.setText("")
      
        self.txtEtiqueta = QtWidgets.QLineEdit(self.tabProductos)
        self.txtEtiqueta.setEnabled(False)
        self.txtEtiqueta.setGeometry(QtCore.QRect(10, 160, 131, 41))
        font.setPointSize(16)
        self.txtEtiqueta.setFont(font)
        #self.txtEtiqueta.setText("")

        self.lb_ruta = QtWidgets.QLabel(self.tabProductos)
        self.lb_ruta.setGeometry(QtCore.QRect(260, 165, 151, 16))
        font.setPointSize(10)
        self.lb_ruta.setFont(font)
        self.lb_ruta.setText("Ruta de la imagen")

        self.lb_boton = QtWidgets.QLabel(self.tabProductos)
        self.lb_boton.setGeometry(QtCore.QRect(10, 63, 361, 16))
        self.lb_boton.setText("Selecciona el botón que desee configurar:")

        #-----------------------------------
        # ComboBox de sección de Venta
        #-----------------------------------
        self.cb_Venta = QtWidgets.QComboBox(self.tabProductos)
        self.cb_Venta.setGeometry(QtCore.QRect(130, 20, 104, 26))

        #-----------------------------------
        # ComboBox de los botones
        #-----------------------------------
        self.cb_Boton = QtWidgets.QComboBox(self.tabProductos)
        self.cb_Boton.setGeometry(QtCore.QRect(310, 60, 121, 26))

       
        self.line = QtWidgets.QFrame(self.tabProductos)
        self.line.setGeometry(QtCore.QRect(20, 90, 441, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.lb_importe = QtWidgets.QLabel(self.tabProductos)
        self.lb_importe.setGeometry(QtCore.QRect(370, 210, 61, 16))
        self.lb_importe.setText("Importe €")
        
        self.txtConcepto = QtWidgets.QLineEdit(self.tabProductos)
        self.txtConcepto.setEnabled(False)
        self.txtConcepto.setGeometry(QtCore.QRect(10, 230, 341, 41))
        font.setPointSize(16)
        self.txtConcepto.setFont(font)

        self.lb_concepto = QtWidgets.QLabel(self.tabProductos)
        self.lb_concepto.setGeometry(QtCore.QRect(10, 210, 121, 16))
        self.lb_concepto.setText("Concepto")

        self.btnCargarImagen = QtWidgets.QPushButton(self.tabProductos)
        self.btnCargarImagen.setEnabled(False)
        self.btnCargarImagen.setGeometry(QtCore.QRect(260, 130, 141, 32))
        self.btnCargarImagen.setText("Cambiar Imagen")
        self.btnCargarImagen.setAutoDefault(False)
        self.btnCargarImagen.setObjectName("btnCargarImagen")

        self.lb_etiboton = QtWidgets.QLabel(self.tabProductos)
        self.lb_etiboton.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.lb_etiboton.setText("Etiqueta del botón")

        self.lb_icono = QtWidgets.QLabel(self.tabProductos)
        self.lb_icono.setGeometry(QtCore.QRect(160, 123, 81, 81))
        self.lb_icono.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_icono.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lb_icono.setMidLineWidth(0)
        self.lb_icono.setEnabled(False)
        #self.lb_icono.setPixmap(QtGui.QPixmap("Iconos/LogoBlancoJoyeros.png"))
        self.lb_icono.setScaledContents(True)
        self.lb_icono.setIndent(-1)

        self.txtIcono = QtWidgets.QLineEdit(self.tabProductos)
        self.txtIcono.setEnabled(False)
        self.txtIcono.setGeometry(QtCore.QRect(260, 180, 221, 21))

        self.lb_TipoVenta = QtWidgets.QLabel(self.tabProductos)
        self.lb_TipoVenta.setGeometry(QtCore.QRect(10, 23, 101, 16))
        self.lb_TipoVenta.setText("Tipo de Venta:")

        self.checkbActivado = QtWidgets.QCheckBox(self.tabProductos)
        self.checkbActivado.setGeometry(QtCore.QRect(10, 110, 87, 20))
        self.checkbActivado.setText("Activado")

        self.tabConfig.addTab(self.tabProductos, "Productos")

        # self.tabImprimir = QtWidgets.QWidget()
        # self.tabImprimir.setObjectName("tabImprimir")
        # self.tabConfig.addTab(self.tabImprimir, "Imprimir")

        self.tabVarios = QtWidgets.QWidget()
        self.tabVarios.setObjectName("tab")
        self.tabConfig.addTab(self.tabVarios, "Varios")

        self.grpIVA = QtWidgets.QGroupBox(self.tabVarios)
        self.grpIVA.setGeometry(QtCore.QRect(10, 10, 161, 101))
        self.grpIVA.setTitle("IVA")
        self.cb_IVA = QtWidgets.QCheckBox(self.grpIVA)
        self.cb_IVA.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.cb_IVA.setText("Calcular IVA")
        self.lb_IVAP = QtWidgets.QLabel(self.grpIVA)
        self.lb_IVAP.setGeometry(QtCore.QRect(10, 63, 51, 16))
        self.txtIVA = QtWidgets.QLineEdit(self.grpIVA)
        self.txtIVA.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.lb_IVAP.setText("IVA %:")
        self.tabConfig.addTab(self.tabVarios, "Varios")
        
        
        

        self.btnCerrar = QtWidgets.QPushButton(self)
        self.btnCerrar.setGeometry(QtCore.QRect(270, 330, 138, 48))
        self.btnCerrar.setStatusTip("")
        self.btnCerrar.setWhatsThis("")
        self.btnCerrar.setText("Cerrar")
        self.btnCerrar.setDefault(True)
        self.btnCerrar.setObjectName("btnCerrar")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setIconSize(QtCore.QSize(32, 32))

        self.btnGuardar = QtWidgets.QPushButton(self)
        self.btnGuardar.setGeometry(QtCore.QRect(130, 330, 138, 48))
        self.btnGuardar.setStatusTip("")
        self.btnGuardar.setWhatsThis("")
        self.btnGuardar.setText("Guardar")
        self.btnGuardar.setObjectName("btnGuardar")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/disquete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon1)
        self.btnGuardar.setIconSize(QtCore.QSize(32, 32))

        self.tabConfig.setCurrentIndex(0)
        self.setTabOrder(self.tabConfig, self.cb_Venta)
        self.setTabOrder(self.cb_Venta, self.cb_Boton)
        self.setTabOrder(self.cb_Boton, self.checkbActivado)
        self.setTabOrder(self.checkbActivado, self.txtEtiqueta)
        self.setTabOrder(self.txtEtiqueta, self.btnCargarImagen)
        self.setTabOrder(self.btnCargarImagen, self.txtIcono)
        self.setTabOrder(self.txtIcono, self.txtConcepto)
        self.setTabOrder(self.txtConcepto, self.txtImporte)
        self.setTabOrder(self.txtImporte, self.btnGuardar)
        self.setTabOrder(self.btnGuardar, self.btnCerrar)

        #--------------------------------------------------------
        # Concectamos los eventos de los widgets con sus metodos
        #--------------------------------------------------------
        self.btnCerrar.clicked.connect(lambda:self.close()) #Cierra sin guardar nada
        self.btnGuardar.clicked.connect(self.onGuardar)
        self.checkbActivado.stateChanged.connect(self.onCheckBoxActivado)
        self.cb_Venta.activated[str].connect(self.onCambioVenta)
        self.cb_Boton.activated[str].connect(self.onCambioBotones)
        self.btnCargarImagen.clicked.connect(self.onBotonCambiarIcono)
    
    #====================================================
    # Método del evento Guardar
    #   - Descripción: Guarda el último cambio realizado
    #==================================================== 
    def onGuardar(self):
        returnValue = QtWidgets.QMessageBox.question(self,"¿Guardar?","¿Quieres Guardar?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if returnValue == QtWidgets.QMessageBox.Yes:
            self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["activado"]=self.checkbActivado.isChecked()
            self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["nombre"]=self.txtEtiqueta.text()
            self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["concepto"]=self.txtConcepto.text()
            self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["importe"]=float(self.txtImporte.text())
            self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["icono"]=self.txtIcono.text()
            self.datos["Configuración"]["Iva"]=self.cb_IVA.isChecked()
            self.datos["Configuración"]["IvaPorcentaje"]=int(self.txtIVA.text())
            self.__cambioDeDatos = True
    
    #===================================================
    # Método para saber si se ha cambiado algun dato
    #   - Descripción: Si se ha guardado un dato se cambia el estado
    #===================================================  
    def getCambioDeDatos(self):
        return self.__cambioDeDatos
    
    
    #============================================================
    # Método que se lanza cuando hay un cambio de el combobox de tipo de venta
    #============================================================
    def onCambioVenta(self, text): 
        self.CargaBotones()

    #============================================================
    # Método que se lanza cuando hay un cambio en el combobox de Botones
    #============================================================
    def onCambioBotones(self):
        self.checkbActivado.setChecked(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["activado"])
        self.txtEtiqueta.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["nombre"])
        self.txtConcepto.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["concepto"])
        self.txtImporte.setText(str(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["importe"]))
        self.txtIcono.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["icono"])
        self.lb_icono.setPixmap(QtGui.QPixmap(self.txtIcono.text()))

    #============================================================
    # Método que se lanza cuando hay un cambio en el checkbox de Activado
    #============================================================
    def onCheckBoxActivado(self):
        if self.checkbActivado.isChecked(): #Activa todo
            self.txtEtiqueta.setEnabled(True)
            self.lb_icono.setEnabled(True)
            self.btnCargarImagen.setEnabled(True)
            self.txtConcepto.setEnabled(True)
            self.txtConcepto.setEnabled(True)
            self.txtImporte.setEnabled(True)
        else:                               #Desactiva todo
            self.txtEtiqueta.setEnabled(False)
            self.lb_icono.setEnabled(False)
            self.btnCargarImagen.setEnabled(False)
            self.txtConcepto.setEnabled(False)
            self.txtConcepto.setEnabled(False)
            self.txtImporte.setEnabled(False)
        #-----------------------------------------
        # Se carga los datos que haya de Productos
        #-----------------------------------------
        self.txtEtiqueta.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["nombre"])
        self.txtConcepto.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["concepto"])
        self.txtImporte.setText(str(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["importe"]))
        self.txtIcono.setText(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["icono"])
        self.lb_icono.setPixmap(QtGui.QPixmap(self.txtIcono.text()))

    def onBotonCambiarIcono(self):
        options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fichero, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Selecciona fichero", "Iconos/","Imagenes (*.png *.jpg)",options=options)
        self.txtIcono.setText(fichero) #Actualizamos el textbox
        self.lb_icono.setPixmap(QtGui.QPixmap(self.txtIcono.text())) #Cambiamos la imagen por la nueva
    
    #==================================================================================
    # Método cargarDatosConfiguracion
    #   - Descripción: Carga los datos del fichero JSON y en caso de que este fichero
    #                  no exista le genera con todo vacío.
    #==================================================================================
    def cargarDatosConfiguracion(self):
        #--------------------------------------
        # Cargamos de Productos las secciones 
        #--------------------------------------
        for etiqueta_venta in self.datos:
            if (etiqueta_venta != "Configuración"): 
                 self.cb_Venta.addItem(etiqueta_venta)
        
        self.cb_IVA.setChecked(self.datos["Configuración"]["Iva"])
        self.txtIVA.setText(str(self.datos["Configuración"]["IvaPorcentaje"]))
        
         
        self.CargaBotones()

    #============================================================
    # Método que Carga de Productos los botones correspondiente a la seccion
    #============================================================
    def CargaBotones(self):
       
        self.cb_Boton.clear() #Se borra todos los items      
            
        #----------------------------------------- 
        # Cargamos de Productos los botones que corresponden a elemento seleccionado
        # en el comboBox del tipo de venta.
        #----------------------------------------- 
        for etiqueta_botones in self.datos[self.cb_Venta.currentText()]:
            self.cb_Boton.addItem(etiqueta_botones)

        #----------------------------------------- 
        # Cargamos de Productos el estado de activado para el botón
        #-----------------------------------------
        self.onCambioBotones()
        #self.checkbActivado.setChecked(self.datos[self.cb_Venta.currentText()][self.cb_Boton.currentText()]["activado"])
    

            


