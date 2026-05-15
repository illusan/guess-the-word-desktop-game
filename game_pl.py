import customtkinter as ctk


class GamePlFrame(ctk.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)

        self.text = ctk.CTkLabel(self, text="Game PL", font=("Arial", 50))
        self.text.pack(pady=(100, 0))

        self.frame_game = ctk.CTkFrame(self, bg_color="transparent")
        self.frame_game.pack(pady=(100, 0))

        self.button_back = ctk.CTkButton(self, text="Back to menu", width=200, height=50, command=back_callback)
        self.button_back.pack(pady=10)

        pass


