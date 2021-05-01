# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets


class Apagar_o_Cerrar(QtWidgets.QDialog):
   
    def __init__(self, parent=None,diccionario=""):
        QtWidgets.QDialog.__init__(self, parent)

        self.resultado = 0

        self.setupUi()

        self.btnApagar.clicked.connect(self.onApagar)
        self.btnCancelar.clicked.connect(self.onCancelar)
        self.btnCerrar.clicked.connect(self.onCerrar)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(614, 105)
        self.setMinimumSize(QtCore.QSize(614, 105))
        self.setMaximumSize(QtCore.QSize(614, 105))
        self.setWindowTitle("Apagar o Cerrar")

        self.btnApagar = QtWidgets.QPushButton(self)
        self.btnApagar.setGeometry(QtCore.QRect(10, 10, 181, 91))
        self.btnApagar.setText("Apagar TPV")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/apagar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnApagar.setIcon(icon)
        self.btnApagar.setIconSize(QtCore.QSize(64, 64))

        self.btnCerrar = QtWidgets.QPushButton(self)
        self.btnCerrar.setGeometry(QtCore.QRect(210, 10, 201, 91))
        self.btnCerrar.setText("Cerrar Programa")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/iu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrar.setIcon(icon1)
        self.btnCerrar.setIconSize(QtCore.QSize(64, 64))

        self.btnCancelar = QtWidgets.QPushButton(self)
        self.btnCancelar.setGeometry(QtCore.QRect(430, 10, 171, 91))
        self.btnCancelar.setText("Cancelar")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Iconos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setIconSize(QtCore.QSize(64, 64))
        self.btnCancelar.setDefault(True)

    def onApagar(self):
        self.resultado = 2
        self.close()
    
    def onCancelar(self):
        self.close()

    def onCerrar(self):
        self.resultado = 1
        self.close()