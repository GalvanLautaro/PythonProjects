import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Ingreso de usuario y clave")
        self.label1=tk.Label(self.ventana1, text="Usuario: ")
        self.label1.grid(column=0, row=0)
        self.usuario=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.usuario)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(self.ventana1, text="Clave: ")
        self.label2.grid(column=0, row=1)
        self.clave=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.clave, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Validar", command=self.validar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.mainloop()

    def validar(self):
        if self.usuario.get()=="lauti" and self.clave.get()=="12":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

aplicacion1=Aplicacion()