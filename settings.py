import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master, switch_screen_callback, back_callback):
        super().__init__(master)

        self.text_settings = ctk.CTkLabel(self, text="Game settings", font=("Arial", 50))
        self.text_settings.pack(pady=(100, 0))

        self.frame_settings = ctk.CTkFrame(self, bg_color="transparent")
        self.frame_settings.pack(pady=(100, 0))

        self.text_display = ctk.CTkLabel(self.frame_settings, text="Display mode", font=("Arial", 17))
        self.text_display.grid(row=0, column=0, padx=10, pady=10)

        self.option = ctk.CTkOptionMenu(self.frame_settings, values=["Windowed", "Fullscreen"], width=200, command=switch_screen_callback)
        self.option.grid(row=1, column=0, padx=10, pady=10)

        self.button_back = ctk.CTkButton(self.frame_settings, text="Back to menu", width=200, height=50, command=back_callback)
        self.button_back.grid(row=2, column=0, padx=10, pady=10)
