# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

#==============================================================================
# Clase VentBorrar
#   - Descripcion: Esta clase quea una ventana de dialogo que gestiona
#                  que es lo que tiene que borrar al pulsar el boton de borrar
#
#   - Funcionamiento:
#                       from BorrarCE import VentBorrar 
# 
#                       nombre = VentBorrar(self) <--- Se le tiene que pasar el padre
#                       nombre.exec_()
#   - NOTA:
#           Una vez terminada la ventana de Borrar almacena en atribito 
#           publico CE el resultado. 
#               0=nada 
#               1=Borrar Importe 
#               2=Borrar Concepto e importe
#               3=Borrar todo el ticket
#==============================================================================
class VentBorrar(QtWidgets.QDialog):
    #-------------------------
    # Constructor
    #-------------------------
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.__setupUi()

    #-------------------------
    # Método privado que inicializa y pone todos los widgets en su sitio
    #-------------------------
    def __setupUi(self):
        self.resize(307, 230)
        self.setMinimumSize(QtCore.QSize(307, 230))
        self.setMaximumSize(QtCore.QSize(307, 230))
        self.setWindowTitle("¿Borrar?")

        self.grpBorrar = QtWidgets.QGroupBox(self)
        self.grpBorrar.setGeometry(QtCore.QRect(10, 0, 281, 150))
        self.grpBorrar.setTitle("¿Qué desea BORRAR?")

        self.rbtnBorrarImporte = QtWidgets.QRadioButton(self.grpBorrar)
        self.rbtnBorrarImporte.setGeometry(QtCore.QRect(20, 30, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rbtnBorrarImporte.setFont(font)
        self.rbtnBorrarImporte.setText("Solo el IMPORTE")
        self.rbtnBorrarImporte.setChecked(True)

        self.rbtnBorrarConceptoImporte = QtWidgets.QRadioButton(self.grpBorrar)
        self.rbtnBorrarConceptoImporte.setGeometry(QtCore.QRect(20, 70, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rbtnBorrarConceptoImporte.setFont(font)
        self.rbtnBorrarConceptoImporte.setText("El Concepto y el Importe")

        self.rbtnBorrarTicket = QtWidgets.QRadioButton(self.grpBorrar)
        self.rbtnBorrarTicket.setGeometry(QtCore.QRect(20, 110, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rbtnBorrarTicket.setFont(font)
        self.rbtnBorrarTicket.setText("Todo el TICKET!!!")

        self.btnBorrar = QtWidgets.QPushButton(self)
        self.btnBorrar.setGeometry(QtCore.QRect(155, 160, 130, 61))
        self.btnBorrar.setText("Borrar")
        self.btnBorrar.setDefault(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/OK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBorrar.setIcon(icon)
        self.btnBorrar.setIconSize(QtCore.QSize(42, 42))

        self.btnCancelar = QtWidgets.QPushButton(self)
        self.btnCancelar.setGeometry(QtCore.QRect(20, 160, 130, 61))
        self.btnCancelar.setText("Cancelar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon)
        self.btnCancelar.setIconSize(QtCore.QSize(42, 42))

        #Variable que guarda que se hace 
        #       0=nada 
        #       1=Borrar Importe 
        #       2=Borrar Concepto e importe
        #       3=Borrar todo el ticket
        self.__CE = 0 

        #----------------------------------------
        # Conectamos botones con sus eventos
        #----------------------------------------
        self.btnBorrar.clicked.connect(self.__OnBotonBorrar)
        self.btnCancelar.clicked.connect(lambda:self.close())

    #=========================================================================
    # Método privado del BOTON Borrar
    #   - Descripción: Comprueba que radio boton esta marcado
    #=========================================================================
    def __OnBotonBorrar(self):
        if self.rbtnBorrarImporte.isChecked():
            self.__CE = 1
        elif self.rbtnBorrarConceptoImporte.isChecked():
            self.__CE = 2
        elif self.rbtnBorrarTicket.isChecked():
            self.__CE = 3
        self.close()
    
    #=========================================================================
    # Método getter
    #   - Descripción: devuelve el estado del atributo CE en la cual se 
    #                  guardo la selección de que hacer
    #=========================================================================
    def get_CE(self):
        return self.__CE
