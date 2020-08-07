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

ColorFondo="#404040"
teclado=""

class Aplicacion(Frame):
    def __init__(self, principal=None):
        super().__init__(principal)
        #--------Actualizamos la fecha ----
        self.Fecha=datetime.now()

        #---- Creamos la ventana principal
        self.Ventanaprincipal = principal
        self.Ventanaprincipal.title("{} {}".format(NombreApp,Version))
        self.Ventanaprincipal.geometry("1024x600") #tamaño de la ventana
    
        self.Ventanaprincipal.protocol("WM_DELETE_WINDOW", self.Salir) #Controlamos el evento cerrar la ventana principal y lo mandamos al metodo Salir()
        
        #---- Creamos el menú ----
        self.BarraMenu = Menu(self.Ventanaprincipal)
        self.Ventanaprincipal.config(menu=self.BarraMenu)

        #---- Marco principal de la Aplicación, donde van a ir todos los widget----
        self.frameprincipal=Frame(self.Ventanaprincipal,bg=ColorFondo)
        self.frameprincipal.pack(fill="both", expand=True)


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
        #Label(self.frBarraOpcionesTicket,text="{}/{}/{}".format(self.Fecha.day,self.Fecha.month,self.Fecha.year),font=("",24),bg=ColorFondo,fg="white").pack(side="left",padx=2)
        
        #---- Barra de herramientas ----
        self.frBarraHerramientas=Frame(self.frameprincipal)
        self.frBarraHerramientas.pack(fill="x",ipady=1)
        Button(self.frBarraHerramientas,image=self.Iconos[0],width=56,height=56,command=self.Salir).grid(row=0,column=0,padx=1)
        Button(self.frBarraHerramientas,image=self.Iconos[0],width=56,height=56,command=self.Salir).grid(row=0,column=1,padx=1)


        #---- Teclado númerico ----
        self.TecladoNumerico(self.Ventanaprincipal,X=200,Y=200)

        
        #----- Datagrid -----
      #  self.datagrid=ttk.Treeview(self.frZonaVentas, columns=(1,2),show="headings", height="7")
      #  self.datagrid.grid(row=0,column=0,padx=2,pady=5,sticky="n")

      #  self.datagrid.column(1, width = 425, anchor = "w")
      #  self.datagrid.column(2, width = 60, anchor = "e")

      #  self.datagrid.heading(1, text="Artículo")
      #  self.datagrid.heading(2, text="Importe")
        
        #---- Botones de DataGrid ----
        """self.frBtnDataGrid=Frame(self.frZonaVentas)
        self.frBtnDataGrid.grid(row=0,column=0,sticky="sw")
        Label(self.frBtnDataGrid,text="TOTAL: {} €".format(1000),font=("",20)).grid(row=0,column=0,columnspan=7,sticky="e")

        Button(self.frBtnDataGrid,image=self.Iconos[1],width=130, height=66).grid(row=1,column=0,columnspan=2)
        Button(self.frBtnDataGrid,image=self.Iconos[9],width=66, height=66).grid(row=1,column=2)
        Button(self.frBtnDataGrid,image=self.Iconos[8],width=66, height=66).grid(row=1,column=3)
        Button(self.frBtnDataGrid,image=self.Iconos[7],width=66, height=66).grid(row=1,column=4)
        Button(self.frBtnDataGrid,image=self.Iconos[6],width=66, height=66).grid(row=1,column=5)
        """
       

        #---- Botones de los Artículos ----

        #for columnas in range(10):
        #    for filas in range(2):
        #        Button(self.frArticulos,image=self.Iconos[2+columnas],width=66, height=66).grid(row=filas,column=columnas)
        

    def TecladoNumerico(self,marco,X=None,Y=None):
        self.MarcoBotones=Frame(marco)
        #self.MarcoBotones.grid(row=0,column=2, sticky="ne")
        self.MarcoBotones.place(x=X,y=Y)

        Button(self.MarcoBotones,image=self.Iconos[1],width=56, height=56,command=lambda:self.ClickTeclado(1)).grid(row=0,column=0)
        Button(self.MarcoBotones,image=self.Iconos[2],width=56, height=56,command=lambda:self.ClickTeclado(2)).grid(row=0,column=1)
        Button(self.MarcoBotones,image=self.Iconos[3],width=56, height=56,command=lambda:self.ClickTeclado(3)).grid(row=0,column=2)

        Button(self.MarcoBotones,image=self.Iconos[4],width=56, height=56,command=lambda:self.ClickTeclado(4)).grid(row=1,column=0)
        Button(self.MarcoBotones,image=self.Iconos[5],width=56, height=56,command=lambda:self.ClickTeclado(5)).grid(row=1,column=1)
        Button(self.MarcoBotones,image=self.Iconos[6],width=56, height=56,command=lambda:self.ClickTeclado(6)).grid(row=1,column=2)

        Button(self.MarcoBotones,image=self.Iconos[7],width=56, height=56,command=lambda:self.ClickTeclado(7)).grid(row=2,column=0)
        Button(self.MarcoBotones,image=self.Iconos[8],width=56, height=56,command=lambda:self.ClickTeclado(8)).grid(row=2,column=1)
        Button(self.MarcoBotones,image=self.Iconos[9],width=56, height=56,command=lambda:self.ClickTeclado(9)).grid(row=2,column=2)

        Button(self.MarcoBotones,image=self.Iconos[11],width=56, height=56,command=lambda:self.ClickTeclado("ok")).grid(row=3,column=0)
        Button(self.MarcoBotones,image=self.Iconos[10],width=56, height=56,command=lambda:self.ClickTeclado(0)).grid(row=3,column=1)
        Button(self.MarcoBotones,image=self.Iconos[12],width=56, height=56,command=lambda:self.ClickTeclado(".")).grid(row=3,column=2)
    
    #-------- Metodo que salta al pulsar los botones del teclado numerico -----------
    def ClickTeclado(self,tecla):
          global teclado
          if tecla == "ok":
                messagebox.showinfo("Booooom","Destrucción el mundo mundial {0}".format(teclado))
          else:
                if not ((tecla==".") and ("." in teclado)): #Se verifica que ya tiene el punto del decimal
                  teclado+=str(tecla)
                  print(float(teclado))

    #------------- Cargamos las imagenes y creamos una tupla con ellas.
    def CargarImagenes(self):
       self.Iconos=(
            PhotoImage(file="./Iconos/Salir.png"),      #[0] Icono de Salir
            PhotoImage(file="./Iconos/uno54.png"),      #[1] 1
            PhotoImage(file="./Iconos/dos54.png"),      #[2] 2
            PhotoImage(file="./Iconos/tres54.png"),     #[3] 3
            PhotoImage(file="./Iconos/cuatro54.png"),   #[4] 4
            PhotoImage(file="./Iconos/cinco54.png"),    #[5] 5
            PhotoImage(file="./Iconos/seis54.png"),     #[6] 6
            PhotoImage(file="./Iconos/siete54.png"),    #[7] 7
            PhotoImage(file="./Iconos/ocho54.png"),     #[8] 8
            PhotoImage(file="./Iconos/nueve54.png"),    #[9] 9
            PhotoImage(file="./Iconos/cero54.png"),     #[10] 0
            PhotoImage(file="./Iconos/okay54.png"),     #[11] Ok
            PhotoImage(file="./Iconos/punto54.png"),    #[12] .
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
            ) 

    #-------- Método que controla la destrucción de la aplicación -------
    def Salir(self):
        respuesta=messagebox.askquestion("Salir", "¿Estas seguro que deseas salir?")
        if respuesta=="yes":
            self.Ventanaprincipal.destroy()





def mainApp():
    root=Tk()
    App=Aplicacion(principal=root)
    App.mainloop()
    return 0


if __name__ == "__main__":
    mainApp()
