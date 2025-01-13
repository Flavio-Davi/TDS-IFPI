from tkinter import *
from Objetos import objeto

class Tela():
    def __init__(self):
        self.home()
        self.frame()
        self.opc()
        self.screen.mainloop()


    def home(self):
        self.screen = Tk()
        self.screen.title("04 O Poder da Tartaruga")
        self.screen.geometry("480x360")
        self.screen.resizable(False, False)
        self.screen.config(background="#363636")
        

        tt = Label(self.screen, text="TURTLE", font=("impact", 20, "bold"), background="#363636", fg="white", width=50)
        tt.pack(anchor="nw", padx=200, pady=20)
        

    def frame(self):
        self.fr = Frame(self.screen, background="#A9A9A9", border=5, width=200, height=275, highlightbackground="white", highlightthickness=2)
        self.fr.place(anchor=CENTER, relx=0.5, rely=0.60)
        self.fr.pack_propagate(0)


    def obj_quadrado(self):
        return objeto().quadrado()
    

    def obj_triangulo(self):
        return objeto().triangulo()


    def obj_pentagono(self):
        return objeto().pentagono()
    
    
    def obj_hexagono(self):
        return objeto().hexagono()


    def obj_circulo(self):
        return objeto().circulo()


    def obj_desenho(self):
        return objeto().desenho()

    def opc(self):
        qd = Button(self.fr, background="#4F4F4F", text="Quadrado", width=10, height=1, command=self.obj_quadrado)
        qd.pack(anchor=CENTER, padx=25, pady=6)
        qd = Button(self.fr, background="#4F4F4F", text="Triângulo", width=10, height=1, command=self.obj_triangulo)
        qd.pack(anchor=CENTER, padx=25, pady=7)
        qd = Button(self.fr, background="#4F4F4F", text="Circulo", width=10, height=1, command=self.obj_circulo)
        qd.pack(anchor=CENTER, padx=25, pady=8)
        qd = Button(self.fr, background="#4F4F4F", text="Pentagono", width=10, height=1, command=self.obj_pentagono)
        qd.pack(anchor=CENTER, padx=25, pady=9)
        qd = Button(self.fr, background="#4F4F4F", text="Hexagono", width=10, height=1, command=self.obj_hexagono)
        qd.pack(anchor=CENTER, padx=25, pady=10)
        qd = Button(self.fr, background="#4F4F4F", text="Desenho", width=10, height=1, command=self.obj_desenho)
        qd.pack(anchor=CENTER, padx=25, pady=11)


Tela()
