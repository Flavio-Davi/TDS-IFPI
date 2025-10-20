# /src/frontend/gui/curtida_view.py
import customtkinter as ctk

class CurtidaView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label_form = ctk.CTkLabel(self, text="Formulário de Curtidas", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_user_id = ctk.CTkEntry(self, placeholder_text="ID do Usuário")
        self.entry_user_id.pack(pady=5, padx=20, fill="x")
        
        self.entry_post_id = ctk.CTkEntry(self, placeholder_text="ID do Post")
        self.entry_post_id.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.btn_curtir = ctk.CTkButton(self, text="Curtir", command=self.curtir)
        self.btn_curtir.pack(pady=5, padx=20, fill="x")

        self.btn_descurtir = ctk.CTkButton(self, text="Descurtir", fg_color="red", command=self.descurtir)
        self.btn_descurtir.pack(pady=5, padx=20, fill="x")

        self.btn_verificar = ctk.CTkButton(self, text="Verificar Curtida", command=self.verificar)
        self.btn_verificar.pack(pady=5, padx=20, fill="x")
        
        self.btn_listar = ctk.CTkButton(self, text="Listar Curtidas do Post", command=self.listar_curtidas)
        self.btn_listar.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=200, state="disabled")
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

    def curtir(self):
        user_id = self._get_user_id()
        post_id = self._get_post_id()
        if not user_id or not post_id:
            self.controller.view.show_message("Erro", "IDs de Usuário e Post são obrigatórios.")
            return
        self.controller.curtir_post(user_id, post_id)
        self.listar_curtidas()

    def descurtir(self):
        user_id = self._get_user_id()
        post_id = self._get_post_id()
        if not user_id or not post_id:
            self.controller.view.show_message("Erro", "IDs de Usuário e Post são obrigatórios.")
            return
        self.controller.descurtir_post(user_id, post_id)
        self.listar_curtidas()

    def verificar(self):
        user_id = self._get_user_id()
        post_id = self._get_post_id()
        if not user_id or not post_id:
            self.controller.view.show_message("Erro", "IDs de Usuário e Post são obrigatórios.")
            return
        # O _show_message padrão no controller já exibe o resultado
        self.controller.verificar_curtida(user_id, post_id)

    def listar_curtidas(self):
        post_id = self._get_post_id()
        if not post_id:
            self.controller.view.show_message("Erro", "ID de Post inválido para listar.")
            return
        curtidas, msg = self.controller.listar_curtidas_por_post(post_id)
        self._show_results(curtidas)

        