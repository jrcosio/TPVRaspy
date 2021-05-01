from PyQt5 import QtCore, QtGui, QtWidgets


class BotonProductos(QtWidgets.QToolButton):
    #Atributos privados
  
    __nombre = ""
    __importe = 0.0
    __concepto = ""
    __activado = False
    __icono = ""

    #==============================================================================
    # Constructor
    #           Descripción: Se le pasa el gridlayout donde iniciar el boton
    #==============================================================================
    def __init__(self, gridLayout, nombre, concepto, importe, activado, icono):
        super().__init__(gridLayout)
        self.setDatos(nombre, concepto, importe, activado, icono)
        self.setIconSize(QtCore.QSize(64, 64))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.actualizaBoton()
    
    def actualizaBoton(self):
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setText(self.__nombre)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.__icono), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        if self.__activado:
            self.show()
        else:
            self.hide()

    #Metodo Getter de __id
    def getDatos(self):
        return self.__concepto,self.__importe

    #Especie de Setter Multiple
    def setDatos(self, nombre, concepto, importe, activado, icono):
        self.__nombre = nombre
        self.__importe = importe 
        self.__concepto = concepto
        self.__activado = activado
        self.__icono = icono