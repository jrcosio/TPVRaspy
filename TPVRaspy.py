from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

NombreApp     = "TPVRaspy"
Version       = "0.1 Alpha"
Programador   = "José Ramón Blanco Gutiérrez"
FechaInicio   = "Julio de 2020"
#Fecha de Finalización:    Septiembre 2020
TipoLicencia  = "GNU"
# Descripción del software: Software de Terminal Punto Venta para la Joyería.
# Descripción del hardware: La TPV esta desarrollada con una Raspberry Pi.

class Aplicacion(Frame):
    def __init__(self, principal=None):
        super().__init__(principal)
        #--------Actualizamos la fecha ----
        self.Fecha=datetime.now()

        #---- Creamos la ventana principal
        self.Ventanaprincipal = principal
        self.Ventanaprincipal.title("{} {}".format(NombreApp,Version))
        #self.Ventanaprincipal.resizable(False, False)
        self.Ventanaprincipal.protocol("WM_DELETE_WINDOW", self.Salir) #Controlamos el evento cerrar la ventana principal y lo mandamos al metodo Salir()
        
        #---- Creamos el menú ----
        self.BarraMenu = Menu(self.Ventanaprincipal)
        self.Ventanaprincipal.config(menu=self.BarraMenu)

        #---- Marco principal ----
        self.frameprincipal=Frame(self.Ventanaprincipal)
        self.frameprincipal.pack(fill="both", expand=True)
        
        #---- Marco Fecha y opciones del tickets ----
        self.frBarraOpcionesTicket=Frame(self.frameprincipal)
        self.frBarraOpcionesTicket.pack(fill="x")

        #---- Marco ventas y botones del ticket
        self.frZonaVentas=Frame(self.frameprincipal)
        self.frZonaVentas.pack()#fill="x",padx=5,pady=5)

        #---- Marco de Artículos ----
        self.frArticulos=Frame(self.frameprincipal)
        self.frArticulos.pack(padx=3,pady=10)

        self.CargarImagenes()
        self.crear_Widgets()

    def crear_Widgets(self):
        #------- Añadimos todas las opciones del menú -------
        MenuArchivo=Menu(self.BarraMenu, tearoff=0)
        MenuAyuda=Menu(self.BarraMenu, tearoff=0)

        self.BarraMenu.add_cascade(label="Archivo", menu=MenuArchivo)
        self.BarraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)

        MenuArchivo.add_command(label="Configuración")
        MenuArchivo.add_separator()
        MenuArchivo.add_command(label="Salir", command=self.Salir)

        MenuAyuda.add_command(label="Acerca de ...", command=lambda:messagebox.showinfo(NombreApp,"""Versión: {}\nProgramador: {}\nTipo de Licencia: {}""".format(Version,Programador,TipoLicencia)))
        
        #---- Añadirmo a la barra del ticket el Label Fecha y botones del ticket ---
        Label(self.frBarraOpcionesTicket,text="{}/{}/{}".format(self.Fecha.day,self.Fecha.month,self.Fecha.year),font=("",24),bg="#333333",fg="white").pack(side="left",padx=2)
        for i in range(12):
            Button(self.frBarraOpcionesTicket,image=self.Iconos[1],width=34, height=34).pack(side="left",padx=2,pady=0)
        Button(self.frBarraOpcionesTicket,image=self.Iconos[1],width=34, height=34).pack(side="right",padx=2,pady=0)
        
        #----- Datagrid -----
        self.datagrid=ttk.Treeview(self.frZonaVentas, columns=(1,2),show="headings", height="7")
        self.datagrid.grid(row=0,column=0,padx=2,pady=5,sticky="n")

        self.datagrid.column(1, width = 425, anchor = "w")
        self.datagrid.column(2, width = 60, anchor = "e")

        self.datagrid.heading(1, text="Artículo")
        self.datagrid.heading(2, text="Importe")
        
        #---- Botones de DataGrid ----
        self.frBtnDataGrid=Frame(self.frZonaVentas)
        self.frBtnDataGrid.grid(row=0,column=0,sticky="sw")
        Label(self.frBtnDataGrid,text="TOTAL: {} €".format(1000),font=("",20)).grid(row=0,column=0,columnspan=7,sticky="e")

        Button(self.frBtnDataGrid,image=self.Iconos[1],width=130, height=66).grid(row=1,column=0,columnspan=2)
        Button(self.frBtnDataGrid,image=self.Iconos[9],width=66, height=66).grid(row=1,column=2)
        Button(self.frBtnDataGrid,image=self.Iconos[8],width=66, height=66).grid(row=1,column=3)
        Button(self.frBtnDataGrid,image=self.Iconos[7],width=66, height=66).grid(row=1,column=4)
        Button(self.frBtnDataGrid,image=self.Iconos[6],width=66, height=66).grid(row=1,column=5)
    
       
        #---- Botones numericos ----
        self.TecladoNumerico(self.frZonaVentas)

        #---- Botones de los Artículos ----

        for columnas in range(10):
            for filas in range(2):
                Button(self.frArticulos,image=self.Iconos[2+columnas],width=66, height=66).grid(row=filas,column=columnas)
        

    def TecladoNumerico(self,marco,x=None,y=None):
        self.MarcoBotones=Frame(marco)
        self.MarcoBotones.grid(row=0,column=2, sticky="ne")

        Button(self.MarcoBotones,image=self.Iconos[24],width=56, height=56).grid(row=0,column=0)
        Button(self.MarcoBotones,image=self.Iconos[25],width=56, height=56).grid(row=0,column=1)
        Button(self.MarcoBotones,image=self.Iconos[26],width=56, height=56).grid(row=0,column=2)

        Button(self.MarcoBotones,image=self.Iconos[27],width=56, height=56).grid(row=1,column=0)
        Button(self.MarcoBotones,image=self.Iconos[28],width=56, height=56).grid(row=1,column=1)
        Button(self.MarcoBotones,image=self.Iconos[29],width=56, height=56).grid(row=1,column=2)

        Button(self.MarcoBotones,image=self.Iconos[30],width=56, height=56).grid(row=2,column=0)
        Button(self.MarcoBotones,image=self.Iconos[31],width=56, height=56).grid(row=2,column=1)
        Button(self.MarcoBotones,image=self.Iconos[32],width=56, height=56).grid(row=2,column=2)

        Button(self.MarcoBotones,image=self.Iconos[33],width=56, height=56).grid(row=3,column=0)
        Button(self.MarcoBotones,image=self.Iconos[34],width=56, height=56).grid(row=3,column=1)
        Button(self.MarcoBotones,image=self.Iconos[35],width=56, height=56).grid(row=3,column=2)

    #------------- Cargamos las imagenes y creamos una tupla con ellas.
    def CargarImagenes(self):
       self.Iconos=(
            PhotoImage(file="./Iconos/0.png"),      #[0] Icono de Salir
            PhotoImage(file="./Iconos/1.png"),      #[1] Icono de Imprimir    
            PhotoImage(file="./Iconos/2.png"),      #[2] Icono de Tarjeta Credito
            PhotoImage(file="./Iconos/3.png"),      #[3] Icono de Dinero
            PhotoImage(file="./Iconos/4.png"),      #[4] Icono de Alianzas
            PhotoImage(file="./Iconos/5.png"),      #[5] Icono de Sortija
            PhotoImage(file="./Iconos/6.png"),      #[6] Icono de Sortija en Caja
            PhotoImage(file="./Iconos/7.png"),      #[7] Icono de Pulsera
            PhotoImage(file="./Iconos/8.png"),      #[8] Icono de Reloj
            PhotoImage(file="./Iconos/9.png"),      #[9] Icono de Reloj
            PhotoImage(file="./Iconos/10.png"),     #[10] Icono de Pila
            PhotoImage(file="./Iconos/11.png"),     #[11] Icono de Herramientas
            PhotoImage(file="./Iconos/uno.png"),    #[12] Icono del 1
            PhotoImage(file="./Iconos/dos.png"),    #[13] Icono del 2
            PhotoImage(file="./Iconos/tres.png"),   #[14] Icono del 3
            PhotoImage(file="./Iconos/cuatro.png"), #[15] Icono del 4
            PhotoImage(file="./Iconos/cinco.png"),  #[16] Icono del 5
            PhotoImage(file="./Iconos/seis.png"),   #[17] Icono del 6
            PhotoImage(file="./Iconos/siete.png"),  #[18] Icono del 7
            PhotoImage(file="./Iconos/ocho.png"),   #[19] Icono del 8
            PhotoImage(file="./Iconos/nueve.png"),  #[20] Icono del 9
            PhotoImage(file="./Iconos/cero.png"),   #[21] Icono del 0
            PhotoImage(file="./Iconos/okay.png"),   #[22] Icono del OK
            PhotoImage(file="./Iconos/cero.png"),   #[23] Icono del punto
            PhotoImage(file="./Iconos/uno54.png"),    #[24]
            PhotoImage(file="./Iconos/dos54.png"),    #[25]
            PhotoImage(file="./Iconos/tres54.png"),   #[26]
            PhotoImage(file="./Iconos/cuatro54.png"), #[27]
            PhotoImage(file="./Iconos/cinco54.png"),  #[28]
            PhotoImage(file="./Iconos/seis54.png"),   #[29]
            PhotoImage(file="./Iconos/siete54.png"),  #[30]
            PhotoImage(file="./Iconos/ocho54.png"),   #[31]
            PhotoImage(file="./Iconos/nueve54.png"),  #[32]
            PhotoImage(file="./Iconos/cero54.png"),   #[33]
            PhotoImage(file="./Iconos/okay54.png"),   #[34]
            PhotoImage(file="./Iconos/punto54.png")   #[35]

            ) 

    #-------- Método que controla la destrucción de la aplicación -------
    def Salir(self):
        respuesta=messagebox.askquestion("Salir", "¿Estas seguro que deseas salir?")
        if respuesta=="yes":
            self.Ventanaprincipal.destroy()





def mainApp():
    root=Tk()
    root.geometry("1024x500") #tamaño de la ventana
    App=Aplicacion(principal=root)
    App.mainloop()
    return 0


if __name__ == "__main__":
    mainApp()
