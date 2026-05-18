import customtkinter as ctk


class GameEngFrame(ctk.CTkFrame):
    def __init__(self, master, back_callback):
        super().__init__(master)

        self.text = ctk.CTkLabel(self, text="Game eng", font=("Arial", 50))
        self.text.pack(pady=(100, 0))

        self.frame_game = ctk.CTkFrame(self, bg_color="transparent")
        self.frame_game.pack(pady=(100, 0))


        self.entries = []

        for row in range(6):
            row_entries = []

            for col in range(5):
                entry = ctk.CTkEntry(self.frame_game, width=50, height=50, font=("Arial", 24), justify="center")
                entry.grid(row=row, column=col, padx=5, pady=5)
                entry.bind("<KeyRelease>", lambda event, r=row, c=col: self.move_cursor(event, r, c))

                if row != 0:
                    entry.configure(state="disabled")

                row_entries.append(entry)
                
            self.entries.append(row_entries)


        self.button_back = ctk.CTkButton(self, text="Back to menu", width=200, height=50, command=back_callback)
        self.button_back.pack(pady=10)


    def move_cursor(self, event, row, col):
        text = self.entries[row][col].get()

        if event.keysym == "BackSpace":
            if col > 0:
                self.entries[row][col - 1].focus()
            return

        if not text:
            return

        last_char = text[-1]

        if not last_char.isalpha():
            self.entries[row][col].delete(0, "end")
            if len(text) > 1:
                self.entries[row][col].insert(0, text[0])
            return

        last_char = last_char.upper()

        self.entries[row][col].delete(0, "end")
        self.entries[row][col].insert(0, last_char)

        if col < 4:
            self.entries[row][col + 1].focus()