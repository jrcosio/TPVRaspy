# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class VentanaMensaje(QtWidgets.QDialog):
   
    def __init__(self, tipo, titulo, texto, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.setObjectName("VentanaMensaje")
        self.resize(431, 152)
        self.setMinimumSize(QtCore.QSize(431, 152))
        self.setMaximumSize(QtCore.QSize(431, 152))
        self.setWindowTitle(titulo)

        self.lbTexto = QtWidgets.QLabel(self)
        self.lbTexto.setGeometry(QtCore.QRect(90, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbTexto.setFont(font)
        self.lbTexto.setText(texto)

        self.btnOK = QtWidgets.QPushButton(self)
        self.btnOK.setGeometry(QtCore.QRect(140, 90, 151, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/OK2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon)
        self.btnOK.setIconSize(QtCore.QSize(42, 42))
        self.btnOK.setText("OK")

        #------------------------------------------------------------
        # Si en eñ constructor en tipo ponemos:
        #           - "pregunta" = icono de interrogación
        #           - "aviso"    = icono de exclamación
        #           - "info"     = icono de información
        # ----------------------------------------------------------- 
        self.lbImagen = QtWidgets.QLabel(self)
        self.lbImagen.setGeometry(QtCore.QRect(10, 10, 61, 61))
        if tipo == "pregunta":
            self.lbImagen.setPixmap(QtGui.QPixmap("Iconos/pregunta.png"))
        elif tipo == "aviso":
            self.lbImagen.setPixmap(QtGui.QPixmap("Iconos/aviso.png"))
        else:
            self.lbImagen.setPixmap(QtGui.QPixmap("Iconos/info.png"))
        self.lbImagen.setScaledContents(True)


        self.btnOK.clicked.connect(lambda:self.close())

        self.exec_() #Se auto ejecuta


