# /src/frontend/gui/amizade_view.py
import customtkinter as ctk

class AmizadeView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.label_form = ctk.CTkLabel(self, text="Formulário de Amizade", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_form.pack(pady=10)
        
        self.entry_user_id_1 = ctk.CTkEntry(self, placeholder_text="ID do Usuário 1")
        self.entry_user_id_1.pack(pady=5, padx=20, fill="x")
        
        self.entry_user_id_2 = ctk.CTkEntry(self, placeholder_text="ID do Usuário 2")
        self.entry_user_id_2.pack(pady=5, padx=20, fill="x")

        # --- Botões de Ação ---
        self.btn_add = ctk.CTkButton(self, text="Adicionar Amizade", command=self.add_amizade)
        self.btn_add.pack(pady=5, padx=20, fill="x")

        self.btn_remover = ctk.CTkButton(self, text="Desfazer Amizade", fg_color="red", command=self.del_amizade)
        self.btn_remover.pack(pady=5, padx=20, fill="x")

        self.btn_verificar = ctk.CTkButton(self, text="Verificar Amizade", command=self.verificar_amizade)
        self.btn_verificar.pack(pady=5, padx=20, fill="x")
        
        self.label_listar = ctk.CTkLabel(self, text="Listar Amigos (use apenas Usuário 1):")
        self.label_listar.pack(pady=(10,0))
        
        self.btn_listar = ctk.CTkButton(self, text="Listar Amigos do Usuário 1", command=self.listar_amigos)
        self.btn_listar.pack(pady=5, padx=20, fill="x")

        # --- Textbox de Resultados ---
        self.textbox = ctk.CTkTextbox(self, height=200, state="disabled")
        self.textbox.pack(pady=10, padx=20, fill="both", expand=True)
        
    def _get_user_id_1(self):
        try: return int(self.entry_user_id_1.get())
        except ValueError: return None
            
    def _get_user_id_2(self):
        try: return int(self.entry_user_id_2.get())
        except ValueError: return None
        
    def _show_results(self, data):
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        if isinstance(data, list):
            self.textbox.insert("end", f"IDs de Amigos: {data}\n")
        elif data:
            self.textbox.insert("end", f"{data}\n")
        self.textbox.configure(state="disabled")

    def _get_ids(self):
        user_id_1 = self._get_user_id_1()
        user_id_2 = self._get_user_id_2()
        if not user_id_1 or not user_id_2:
            self.controller.view.show_message("Erro", "IDs de Usuário 1 e 2 são obrigatórios.")
            return None, None
        return user_id_1, user_id_2

    def add_amizade(self):
        user_id_1, user_id_2 = self._get_ids()
        if user_id_1:
            self.controller.adicionar_amizade(user_id_1, user_id_2)

    def del_amizade(self):
        user_id_1, user_id_2 = self._get_ids()
        if user_id_1:
            self.controller.desfazer_amizade(user_id_1, user_id_2)

    def verificar_amizade(self):
        user_id_1, user_id_2 = self._get_ids()
        if user_id_1:
            self.controller.verificar_amizade(user_id_1, user_id_2)

    def listar_amigos(self):
        user_id_1 = self._get_user_id_1()
        if not user_id_1:
            self.controller.view.show_message("Erro", "ID do Usuário 1 é obrigatório para listar.")
            return
        amigos_ids, msg = self.controller.listar_amigos_por_usuario(user_id_1)
        self._show_results(amigos_ids)

        