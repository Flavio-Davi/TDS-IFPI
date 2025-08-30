# gui.py
import customtkinter as ctk
from tkinter import ttk, messagebox
from db_config import Conexao
from query import Querie
from tkcalendar import DateEntry


class TeacherGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Professores - CRUD Completo")
        self.geometry("1050x650")
        ctk.set_appearance_mode("System")  # opções: "Light", "Dark", "System"
        ctk.set_default_color_theme("blue")  # opções: "blue", "green", "dark-blue"

        self.queries = Querie()

        # === Frame de entradas ===
        entry_frame = ctk.CTkFrame(self, corner_radius=10)
        entry_frame.pack(fill="x", padx=15, pady=10)

        labels = [
            "Primeiro Nome", "Sobrenome", "Matrícula",
            "Nascimento (YYYY-MM-DD)", "Email", "ID (Update/Delete)"
        ]
        self.entries = {}

        for i, label in enumerate(labels):
            lbl = ctk.CTkLabel(entry_frame, text=label, font=("Arial", 12))
            lbl.grid(row=0, column=i, padx=5, pady=5)
            if "Nascimento" in label:
                entry = DateEntry(entry_frame, width=15, date_pattern="yyyy-mm-dd")
            else:
                entry = ctk.CTkEntry(entry_frame, width=150)
            entry.grid(row=1, column=i, padx=5, pady=5)
            self.entries[label] = entry

        # === Frame de seleção da operação ===
        action_frame = ctk.CTkFrame(self, corner_radius=10)
        action_frame.pack(fill="x", padx=15, pady=5)

        ctk.CTkLabel(action_frame, text="Escolha a operação:", font=("Arial", 12)).grid(row=0, column=0, padx=5)

        self.action_var = ctk.StringVar(value="Criar Professor")
        self.combo = ctk.CTkOptionMenu(
            action_frame, variable=self.action_var, width=250,
            values=[
                "Criar Professor",
                "Exibir Todos",
                "Buscar por Matrícula",
                "Atualizar Completo",
                "Atualizar Primeiro Nome",
                "Atualizar Sobrenome",
                "Atualizar Matrícula",
                "Atualizar Nascimento",
                "Atualizar Email",
                "Deletar Professor"
            ]
        )
        self.combo.grid(row=0, column=1, padx=10)

        ctk.CTkButton(action_frame, text="Executar", command=self.run_action).grid(row=0, column=2, padx=15)

        # === Frame da tabela ===
        table_frame = ctk.CTkFrame(self, corner_radius=10)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=28)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Primeiro Nome", "Sobrenome", "Matrícula", "Nascimento", "Email"),
            show="headings", height=15
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=160, anchor="center")

        scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_y.set)
        scrollbar_y.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

    # === Função para executar a ação escolhida ===
    def run_action(self):
        action = self.action_var.get()
        try:
            if action == "Criar Professor":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.create_teacher(),
                    (
                        self.entries["Primeiro Nome"].get(),
                        self.entries["Sobrenome"].get(),
                        self.entries["Matrícula"].get(),
                        self.entries["Nascimento (YYYY-MM-DD)"].get(),
                        self.entries["Email"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Professor inserido com sucesso.")
                self.read_all_teachers()

            elif action == "Exibir Todos":
                self.read_all_teachers()

            elif action == "Buscar por Matrícula":
                conn = Conexao()
                rows = conn.execute_query_read(
                    self.queries.read_teacher(),
                    (self.entries["Matrícula"].get(),)
                )
                if not rows:
                    messagebox.showinfo("Resultado", "Nenhum professor encontrado com essa matrícula.")
                self.refresh_tree(rows)

            elif action == "Atualizar Completo":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher(),
                    (
                        self.entries["Primeiro Nome"].get(),
                        self.entries["Sobrenome"].get(),
                        self.entries["Matrícula"].get(),
                        self.entries["Nascimento (YYYY-MM-DD)"].get(),
                        self.entries["Email"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Professor atualizado.")
                self.read_all_teachers()

            elif action == "Atualizar Primeiro Nome":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher_firstname(),
                    (
                        self.entries["Primeiro Nome"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Primeiro nome atualizado.")
                self.read_all_teachers()

            elif action == "Atualizar Sobrenome":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher_lastname(),
                    (
                        self.entries["Sobrenome"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Sobrenome atualizado.")
                self.read_all_teachers()

            elif action == "Atualizar Matrícula":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher_registration(),
                    (
                        self.entries["Matrícula"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Matrícula atualizada.")
                self.read_all_teachers()

            elif action == "Atualizar Nascimento":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher_birthday(),
                    (
                        self.entries["Nascimento (YYYY-MM-DD)"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Data de nascimento atualizada.")
                self.read_all_teachers()

            elif action == "Atualizar Email":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.update_teacher_email(),
                    (
                        self.entries["Email"].get(),
                        self.entries["ID (Update/Delete)"].get()
                    )
                )
                messagebox.showinfo("Sucesso", "Email atualizado.")
                self.read_all_teachers()

            elif action == "Deletar Professor":
                conn = Conexao()
                conn.execute_query_update(
                    self.queries.delete_teacher(),
                    (self.entries["ID (Update/Delete)"].get(),)
                )
                messagebox.showinfo("Sucesso", "Professor deletado.")
                self.read_all_teachers()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # === Função para exibir todos ===
    def read_all_teachers(self):
        try:
            conn = Conexao()
            rows = conn.execute_query_read(self.queries.read_all_teacher())
            if not rows:
                messagebox.showinfo("Resultado", "Nenhum professor encontrado no banco de dados.")
            self.refresh_tree(rows)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # === Função auxiliar para atualizar a tabela ===
    def refresh_tree(self, rows):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in rows:
            self.tree.insert("", "end", values=row)


if __name__ == "__main__":
    app = TeacherGUI()
    app.mainloop()
