# /src/frontend/gui/app_view.py
import customtkinter as ctk
from tkinter import messagebox
from src.frontend.controller.main_controller import MainController
from src.frontend.gui.usuario_view import UsuarioView
from src.frontend.gui.post_view import PostView
from src.frontend.gui.telefone_view import TelefoneView
from src.frontend.gui.comentario_view import ComentarioView
from src.frontend.gui.curtida_view import CurtidaView
from src.frontend.gui.amizade_view import AmizadeView

class AppView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rede Social - Admin")
        self.geometry("800x700")

        # Instancia o Controller e passa a si mesma (a view)
        self.controller = MainController(self)

        # Cria o sistema de Abas
        self.tab_view = ctk.CTkTabview(self, width=780, height=680)
        self.tab_view.pack(padx=10, pady=10)

        # Adiciona as abas
        self.tab_view.add("Usuários")
        self.tab_view.add("Posts")
        self.tab_view.add("Telefones")
        self.tab_view.add("Comentários")
        self.tab_view.add("Curtidas")
        self.tab_view.add("Amizades")

        # Cria e posiciona os frames de cada aba
        self.usuario_frame = UsuarioView(master=self.tab_view.tab("Usuários"), controller=self.controller)
        self.usuario_frame.pack(fill="both", expand=True)

        self.post_frame = PostView(master=self.tab_view.tab("Posts"), controller=self.controller)
        self.post_frame.pack(fill="both", expand=True)

        self.telefone_frame = TelefoneView(master=self.tab_view.tab("Telefones"), controller=self.controller)
        self.telefone_frame.pack(fill="both", expand=True)

        self.comentario_frame = ComentarioView(master=self.tab_view.tab("Comentários"), controller=self.controller)
        self.comentario_frame.pack(fill="both", expand=True)

        self.curtida_frame = CurtidaView(master=self.tab_view.tab("Curtidas"), controller=self.controller)
        self.curtida_frame.pack(fill="both", expand=True)

        self.amizade_frame = AmizadeView(master=self.tab_view.tab("Amizades"), controller=self.controller)
        self.amizade_frame.pack(fill="both", expand=True)

    def show_message(self, title, message):
        """Método que o controller chama para exibir pop-ups."""
        if title.lower() == "erro":
            messagebox.showerror(title, message)
        elif title.lower() == "info":
            messagebox.showinfo(title, message)
        else:
            messagebox.showinfo(title, message)
            