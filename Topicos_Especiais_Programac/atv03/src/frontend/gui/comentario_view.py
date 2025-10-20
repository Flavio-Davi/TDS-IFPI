# /src/frontend/gui/comentario_view.py
import customtkinter as ctk

class ComentarioView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label_form = ctk.CTkLabel(self, text="Formulário de Comentário", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_com_id = ctk.CTkEntry(self, placeholder_text="ID do Comentário (Atualizar/Deletar)")
        self.entry_com_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_post_id = ctk.CTkEntry(self, placeholder_text="ID do Post")
        self.entry_post_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_user_id = ctk.CTkEntry(self, placeholder_text="ID do Usuário (Autor)")
        self.entry_user_id.pack(pady=5, padx=20, fill="x")

        self.entry_conteudo = ctk.CTkEntry(self, placeholder_text="Conteúdo do Comentário")
        self.entry_conteudo.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.btn_criar = ctk.CTkButton(self, text="Criar Comentário", command=self.criar_comentario)
        self.btn_criar.pack(pady=5, padx=20, fill="x")

        self.btn_atualizar = ctk.CTkButton(self, text="Atualizar Comentário", command=self.atualizar_comentario)
        self.btn_atualizar.pack(pady=5, padx=20, fill="x")

        self.btn_deletar = ctk.CTkButton(self, text="Deletar Comentário", fg_color="red", command=self.deletar_comentario)
        self.btn_deletar.pack(pady=5, padx=20, fill="x")
        
        self.btn_listar = ctk.CTkButton(self, text="Listar Comentários por Post", command=self.listar_comentarios)
        self.btn_listar.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=200, state="disabled")
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)

    def _get_com_id(self):
        try: return int(self.entry_com_id.get())
        except ValueError: return None

    def _get_post_id(self):
        try: return int(self.entry_post_id.get())
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

    def criar_comentario(self):
        user_id = self._get_user_id()
        post_id = self._get_post_id()
        if not user_id or not post_id:
            self.controller.view.show_message("Erro", "IDs de Usuário e Post são obrigatórios.")
            return
        conteudo = self.entry_conteudo.get()
        self.controller.criar_comentario(user_id, post_id, conteudo)
        self.listar_comentarios()

    def atualizar_comentario(self):
        com_id = self._get_com_id()
        user_id = self._get_user_id()
        post_id = self._get_post_id()
        if not com_id or not user_id or not post_id:
            self.controller.view.show_message("Erro", "IDs de Comentário, Usuário e Post são obrigatórios.")
            return
        conteudo = self.entry_conteudo.get()
        self.controller.atualizar_comentario(com_id, user_id, post_id, conteudo)
        self.listar_comentarios()

    def deletar_comentario(self):
        com_id = self._get_com_id()
        if not com_id:
            self.controller.view.show_message("Erro", "ID de Comentário inválido.")
            return
        self.controller.deletar_comentario(com_id)
        if self._get_post_id():
            self.listar_comentarios()

    def listar_comentarios(self):
        post_id = self._get_post_id()
        if not post_id:
            self.controller.view.show_message("Erro", "ID de Post inválido para listar.")
            return
        comentarios, msg = self.controller.listar_comentarios_por_post(post_id)
        self._show_results(comentarios)

        