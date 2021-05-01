from thermalprinter import ThermalPrinter
#----------------------------------------
# Info: 
#https://pypi.org/project/thermalprinter/
#----------------------------------------

#ID de Ticket o Numero
#Fecha y Hora

class Imprimir():
    #===================================================================
    # Constructor
    # Descripción: si no se pasan argumentos al constructor estos son por defecto 0
    #               por lo tanto no se podrá imprimir el ticket, el no pasar argumentos
    #               al constructor es para usar el método de Lista. 
    #===================================================================
    def __init__(self, ticket=0, detalleticket=0):
       self.ticket = ticket
       self.detalleTicket = detalleticket
    #===================================================================
    # método Ticket
    # Descripción: Imprime el TICKET. 
    #===================================================================
    def Ticket(self):
        #printer = ThermalPrinter(baudrate=9600,port='/dev/serial0')
        #printer.out("xxxx", justify = 'C' )
        with ThermalPrinter(port='/dev/serial0', baudrate=9600) as printer:
            printer.out('--------------------------------', bold=True)
            #printer.out('Blanco Joyeros', justify='C', double_height=True)
            printer.out('Blanco Joyeros', justify='C', double_width=True)
            printer.out('Paseo Gral. Dávila 264 Nº 2', justify='C')
            printer.out('Santander - Cantabria', justify='C')
            printer.out('--------------------------------', bold=True)
            printer.out('Número Ticket: ' + str(self.ticket[0]), justify='L')
            printer.out('Fecha: ' + str(self.ticket[1]), justify='L')
            printer.out('Hora: ' + str(self.ticket[2]), justify='L')
            printer.out('Forma de pago: ', justify='L')
            printer.out(str(self.ticket[3]), justify='R')
            printer.out('───────────────────────┬────────')
            printer.out('Artículo               │ Importe')
            printer.out('───────────────────────┴────────')
            for lista in self.detalleTicket:
                printer.out(str(lista[1]), justify='L')
                printer.out(str(lista[2]), justify='R')
            printer.out('════════════════════════════════', bold=True)
            if str(self.ticket[5]) != "0.0":                 #No Imprimir el IVA si este vale CERO
                printer.out('Suma Importes: ' + str(self.ticket[4]), justify='R')
                printer.out('IVA 21%:' + str(self.ticket[5]), justify='R')
            printer.out('TOTAL TICKET: ' + str(self.ticket[6]), justify='R')
            printer.out('════════════════════════════════', bold=True)
            printer.out('Para devolución conserve ticket',bold=True)
            printer.out('Plazo de Devolución: 15 días', bold=True)
            printer.out('Teléfono Atención: 942 34 34 24')
            printer.out('════════════════════════════════', bold=True)
            printer.out('MUCHAS GRACIAS POR SU COMPRA', bold=True, justify='C')
            printer.out('════════════════════════════════', bold=True)

            # Line feeds
            printer.feed(3)
    #===================================================================
    # método Lista
    # Descripción: Imprime un listado que se da como argumento y la fecha  
    #===================================================================
    def Lista(self,Fecha,tabla):
        with ThermalPrinter(port='/dev/serial0', baudrate=9600) as printer:
            printer.out('--------------------------------', bold=True)
            printer.out('Blanco Joyeros', justify='C', double_height=True)
            printer.out('--------------------------------', bold=True)
            printer.out('Resumen del Día: ' + str(Fecha), justify='L')
            printer.out('════════════════════════════════', bold=True)
            printer.out('Num-Descripción       Importe|FP', bold=True)
            printer.out('════════════════════════════════', bold=True)
            Total=0
            for a in tabla:
                if a[4] != 0.0:
                    iva = "+ " + str(a[4])
                else: 
                    iva = ""
    
                if a[3] == "Al contado":
                    forma = "C"
                elif a[3] == "Tarjeta de crédito/Débito":
                    forma = "T"
                else:
                    forma = "V"

                Total = round(Total+a[2]+a[4],2)
                
                printer.out(str(a[0]) + ' - ' + str(a[1]), justify='L')
                printer.out(str(a[2]) + str(iva) + ' - ' + str(forma), justify='R')

            printer.out('════════════════════════════════', bold=True)
            printer.out('Total: ' + str(Total), justify='R', bold=True)
            printer.feed(3)

        
