import customtkinter as ctk
import tkinter as tk
from src.frontend.controller.main_controller import MainController

class MainGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Usuários")
        self.geometry("800x600")

        self.controller = MainController(self)

        self.create_widgets()

    def create_widgets(self):
        # Frame para entrada de dados
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkLabel(input_frame, text="Nome Completo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.nome_completo_entry = ctk.CTkEntry(input_frame, width=200)
        self.nome_completo_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = ctk.CTkEntry(input_frame, width=200)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Data Nascimento (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.data_nascimento_entry = ctk.CTkEntry(input_frame, width=200)
        self.data_nascimento_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Botões de ação
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, padx=20, fill="x")

        self.create_button = ctk.CTkButton(button_frame, text="Criar Usuário", command=self.handle_create_user)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.read_button = ctk.CTkButton(button_frame, text="Listar Usuários", command=self.handle_list_users)
        self.read_button.grid(row=0, column=1, padx=5, pady=5)

        self.update_button = ctk.CTkButton(button_frame, text="Atualizar Usuário", command=self.handle_update_user)
        self.update_button.grid(row=0, column=2, padx=5, pady=5)

        self.delete_button = ctk.CTkButton(button_frame, text="Deletar Usuário", command=self.handle_delete_user)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        # Campo para ID do usuário (para buscar, atualizar, deletar)
        ctk.CTkLabel(button_frame, text="ID Usuário:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.user_id_entry = ctk.CTkEntry(button_frame, width=100)
        self.user_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.search_button = ctk.CTkButton(button_frame, text="Buscar por ID", command=self.handle_search_user_by_id)
        self.search_button.grid(row=1, column=2, padx=5, pady=5)

        # Área de exibição de resultados
        self.result_text = ctk.CTkTextbox(self, width=700, height=200)
        self.result_text.pack(pady=20, padx=20, fill="both", expand=True)
        self.result_text.insert("end", "Resultados aparecerão aqui...")
        self.result_text.configure(state="disabled")

    def show_message(self, title, message):
        # Exibe mensagens em uma caixa de diálogo ou na área de resultados
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", f"[{title}] {message}\n")
        self.result_text.configure(state="disabled")

    def handle_create_user(self):
        nome = self.nome_completo_entry.get()
        email = self.email_entry.get()
        data_nascimento = self.data_nascimento_entry.get()
        self.controller.criar_usuario(nome, email, data_nascimento)
        self.clear_entries()

    def handle_list_users(self):
        usuarios, message = self.controller.listar_todos_usuarios()
        self.result_text.configure(state="normal")
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", f"[Lista de Usuários] {message}\n\n")
        if usuarios:
            for user in usuarios:
                self.result_text.insert("end", f"ID: {user.id}, Nome: {user.nome_completo}, Email: {user.email}, Data Nasc: {user.data_nascimento}\n")
        self.result_text.configure(state="disabled")

    def handle_update_user(self):
        user_id = self.user_id_entry.get()
        nome = self.nome_completo_entry.get()
        email = self.email_entry.get()
        data_nascimento = self.data_nascimento_entry.get()
        try:
            user_id = int(user_id)
            self.controller.atualizar_usuario(user_id, nome, email, data_nascimento)
            self.clear_entries()
        except ValueError:
            self.show_message("Erro", "ID de usuário deve ser um número inteiro.")

    def handle_delete_user(self):
        user_id = self.user_id_entry.get()
        try:
            user_id = int(user_id)
            self.controller.deletar_usuario(user_id)
            self.clear_entries()
        except ValueError:
            self.show_message("Erro", "ID de usuário deve ser um número inteiro.")

    def handle_search_user_by_id(self):
        user_id = self.user_id_entry.get()
        try:
            user_id = int(user_id)
            usuario, message = self.controller.buscar_usuario_por_id(user_id)
            self.result_text.configure(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("end", f"[Busca por ID] {message}\n\n")
            if usuario:
                self.result_text.insert("end", f"ID: {usuario.id}, Nome: {usuario.nome_completo}, Email: {usuario.email}, Data Nasc: {usuario.data_nascimento}\n")
                # Preenche os campos para facilitar a edição
                self.nome_completo_entry.delete(0, "end")
                self.nome_completo_entry.insert(0, usuario.nome_completo)
                self.email_entry.delete(0, "end")
                self.email_entry.insert(0, usuario.email)
                self.data_nascimento_entry.delete(0, "end")
                self.data_nascimento_entry.insert(0, str(usuario.data_nascimento))
            self.result_text.configure(state="disabled")
        except ValueError:
            self.show_message("Erro", "ID de usuário deve ser um número inteiro.")

    def clear_entries(self):
        self.nome_completo_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.data_nascimento_entry.delete(0, "end")
        self.user_id_entry.delete(0, "end")

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()

