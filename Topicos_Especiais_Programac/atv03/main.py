import customtkinter as ctk
from src.frontend.gui.app_view import AppView

if __name__ == "__main__":
    # Define o modo de aparência
    ctk.set_appearance_mode("dark")  # Ou "light"
    ctk.set_default_color_theme("blue")  # Ou "dark-blue", "green"

    # Inicia a aplicação
    app = AppView()
    app.mainloop()
    