# /src/frontend/gui/post_view.py
import customtkinter as ctk

class PostView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label_form = ctk.CTkLabel(self, text="Formulário de Post", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_post_id = ctk.CTkEntry(self, placeholder_text="ID do Post (Buscar/Atualizar/Deletar)")
        self.entry_post_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_user_id = ctk.CTkEntry(self, placeholder_text="ID do Usuário (Dono do Post)")
        self.entry_user_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_conteudo = ctk.CTkEntry(self, placeholder_text="Conteúdo do Post")
        self.entry_conteudo.pack(pady=5, padx=20, fill="x")

        self.entry_midia = ctk.CTkEntry(self, placeholder_text="URL da Mídia (Opcional)")
        self.entry_midia.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.btn_criar = ctk.CTkButton(self.button_frame, text="Criar", command=self.criar_post)
        self.btn_criar.pack(side="left", padx=5)

        self.btn_buscar = ctk.CTkButton(self.button_frame, text="Buscar por ID", command=self.buscar_post)
        self.btn_buscar.pack(side="left", padx=5)
        
        self.btn_atualizar = ctk.CTkButton(self.button_frame, text="Atualizar", command=self.atualizar_post)
        self.btn_atualizar.pack(side="left", padx=5)
        
        self.btn_deletar = ctk.CTkButton(self.button_frame, text="Deletar", fg_color="red", command=self.deletar_post)
        self.btn_deletar.pack(side="left", padx=5)

        self.btn_listar_user = ctk.CTkButton(self, text="Listar Posts por Usuário (use ID Usuário)", command=self.listar_posts_usuario)
        self.btn_listar_user.pack(pady=5, padx=20, fill="x")
        
        self.btn_listar_all = ctk.CTkButton(self, text="Listar Todos os Posts", command=self.listar_todos_posts)
        self.btn_listar_all.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=150, state="disabled")
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)

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

    def criar_post(self):
        user_id = self._get_user_id()
        if not user_id: 
            self.controller.view.show_message("Erro", "ID de Usuário inválido.")
            return
        conteudo = self.entry_conteudo.get()
        midia = self.entry_midia.get() or None
        self.controller.criar_post(user_id, conteudo, midia)
        self.listar_todos_posts()

    def buscar_post(self):
        post_id = self._get_post_id()
        if not post_id:
            self.controller.view.show_message("Erro", "ID de Post inválido.")
            return
        post, msg = self.controller.buscar_post_por_id(post_id)
        if post:
            self._show_results(post)

    def atualizar_post(self):
        post_id = self._get_post_id()
        user_id = self._get_user_id()
        if not post_id or not user_id:
            self.controller.view.show_message("Erro", "IDs de Post e Usuário são obrigatórios.")
            return
        conteudo = self.entry_conteudo.get()
        midia = self.entry_midia.get() or None
        self.controller.atualizar_post(post_id, user_id, conteudo, midia)
        self.listar_todos_posts()

    def deletar_post(self):
        post_id = self._get_post_id()
        if not post_id:
            self.controller.view.show_message("Erro", "ID de Post inválido.")
            return
        self.controller.deletar_post(post_id)
        self.listar_todos_posts()

    def listar_posts_usuario(self):
        user_id = self._get_user_id()
        if not user_id:
            self.controller.view.show_message("Erro", "ID de Usuário inválido.")
            return
        posts, msg = self.controller.listar_posts_por_usuario(user_id)
        self._show_results(posts)

    def listar_todos_posts(self):
        posts, msg = self.controller.listar_todos_posts()
        self._show_results(posts)

        