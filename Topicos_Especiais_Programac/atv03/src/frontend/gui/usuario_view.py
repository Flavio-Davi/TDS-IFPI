# /src/frontend/gui/usuario_view.py
import customtkinter as ctk

class UsuarioView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # --- Widgets de Criação/Atualização ---
        self.label_form = ctk.CTkLabel(self, text="Formulário de Usuário", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_id = ctk.CTkEntry(self, placeholder_text="ID (para Atualizar/Buscar/Deletar)")
        self.entry_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome Completo")
        self.entry_nome.pack(pady=5, padx=20, fill="x")
        
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.pack(pady=5, padx=20, fill="x")
        
        self.entry_data = ctk.CTkEntry(self, placeholder_text="Data Nascimento (YYYY-MM-DD)")
        self.entry_data.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)
        
        self.btn_criar = ctk.CTkButton(self.button_frame, text="Criar", command=self.criar_usuario)
        self.btn_criar.pack(side="left", padx=5)

        self.btn_buscar = ctk.CTkButton(self.button_frame, text="Buscar por ID", command=self.buscar_usuario)
        self.btn_buscar.pack(side="left", padx=5)
        
        self.btn_atualizar = ctk.CTkButton(self.button_frame, text="Atualizar", command=self.atualizar_usuario)
        self.btn_atualizar.pack(side="left", padx=5)
        
        self.btn_deletar = ctk.CTkButton(self.button_frame, text="Deletar", fg_color="red", command=self.deletar_usuario)
        self.btn_deletar.pack(side="left", padx=5)

        self.btn_listar = ctk.CTkButton(self, text="Listar Todos", command=self.listar_usuarios)
        self.btn_listar.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=200, state="disabled")
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)

    def _get_id(self):
        try:
            return int(self.entry_id.get())
        except ValueError:
            return None

    def _show_results(self, data):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        if isinstance(data, list):
            for item in data:
                self.textbox.insert("end", f"{item}\n")
        elif data:
            self.textbox.insert("end", f"{data}\n")
        self.textbox.configure(state="disabled")

    def criar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        data = self.entry_data.get()
        self.controller.criar_usuario(nome, email, data)
        self.listar_usuarios() # Atualiza a lista

    def buscar_usuario(self):
        user_id = self._get_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID inválido.")
            return
        usuario, msg = self.controller.buscar_usuario_por_id(user_id)
        if usuario:
            self._show_results(usuario)

    def atualizar_usuario(self):
        user_id = self._get_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID inválido.")
            return
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        data = self.entry_data.get()
        self.controller.atualizar_usuario(user_id, nome, email, data)
        self.listar_usuarios()

    def deletar_usuario(self):
        user_id = self._get_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID inválido.")
            return
        self.controller.deletar_usuario(user_id)
        self.listar_usuarios()

    def listar_usuarios(self):
        usuarios, msg = self.controller.listar_todos_usuarios()
        if usuarios:
            self._show_results(usuarios)

            