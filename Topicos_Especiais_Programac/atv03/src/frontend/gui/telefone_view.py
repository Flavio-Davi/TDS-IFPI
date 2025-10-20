# /src/frontend/gui/telefone_view.py
import customtkinter as ctk

class TelefoneView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label_form = ctk.CTkLabel(self, text="Formulário de Telefone", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_user_id = ctk.CTkEntry(self, placeholder_text="ID do Usuário")
        self.entry_user_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_tel_id = ctk.CTkEntry(self, placeholder_text="ID do Telefone (para Atualizar/Deletar)")
        self.entry_tel_id.pack(pady=5, padx=20, fill="x")

        self.entry_numero = ctk.CTkEntry(self, placeholder_text="Número de Telefone")
        self.entry_numero.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.btn_criar = ctk.CTkButton(self, text="Adicionar Telefone", command=self.criar_telefone)
        self.btn_criar.pack(pady=5, padx=20, fill="x")

        self.btn_atualizar = ctk.CTkButton(self, text="Atualizar Telefone", command=self.atualizar_telefone)
        self.btn_atualizar.pack(pady=5, padx=20, fill="x")

        self.btn_deletar = ctk.CTkButton(self, text="Deletar Telefone", fg_color="red", command=self.deletar_telefone)
        self.btn_deletar.pack(pady=5, padx=20, fill="x")
        
        self.btn_listar = ctk.CTkButton(self, text="Listar Telefones por Usuário", command=self.listar_telefones)
        self.btn_listar.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=200, state="disabled")
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)
        
    def _get_tel_id(self):
        try: return int(self.entry_tel_id.get())
        except ValueError: return None
            
    def _get_user_id(self):
        try: return int(self.entry_user_id.get())
        except ValueError: return None
        
    def _show_results(self, data):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        if isinstance(data, list):
            for item in data: self.textbox.insert("end", f"{item}\n")
        elif data:
            self.textbox.insert("end", f"{data}\n")
        self.textbox.configure(state="disabled")

    def criar_telefone(self):
        user_id = self._get_user_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID de Usuário inválido.")
            return
        numero = self.entry_numero.get()
        self.controller.criar_telefone(user_id, numero)
        self.listar_telefones()

    def atualizar_telefone(self):
        tel_id = self._get_tel_id()
        user_id = self._get_user_id()
        if not tel_id or not user_id:
            self.controller.view.show_message("Erro", "IDs de Telefone e Usuário são obrigatórios.")
            return
        numero = self.entry_numero.get()
        self.controller.atualizar_telefone(tel_id, user_id, numero)
        self.listar_telefones()

    def deletar_telefone(self):
        tel_id = self._get_tel_id()
        if not tel_id:
            self.controller.view.show_message("Erro", "ID de Telefone inválido.")
            return
        self.controller.deletar_telefone(tel_id)
        if self._get_user_id():
            self.listar_telefones()

    def listar_telefones(self):
        user_id = self._get_user_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID de Usuário inválido para listar.")
            return
        telefones, msg = self.controller.listar_telefones_por_usuario(user_id)
        self._show_results(telefones)

        