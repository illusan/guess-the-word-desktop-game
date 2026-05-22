import customtkinter as ctk
import random


class GameEngFrame(ctk.CTkFrame):
    def __init__(self, master, back_callback, words_list):
        super().__init__(master)

        self.words_list = words_list
        self.valid_words = [word.upper() for word in self.words_list]
        self.current_row = 0

        self.text = ctk.CTkLabel(self, text="After entering the word, press ENTER", font=("Arial", 50))
        self.text.pack(pady=(50, 0))

        self.frame_game = ctk.CTkFrame(self, bg_color="transparent")
        self.frame_game.pack(pady=(100, 0))


        self.entries = []

        for row in range(6):
            row_entries = []

            for col in range(5):
                entry = ctk.CTkEntry(self.frame_game, width=50, height=50, font=("Arial", 24), justify="center")
                entry.grid(row=row, column=col, padx=5, pady=5)
                entry.bind("<KeyRelease>", lambda event, r=row, c=col: self.move_cursor(event, r, c))
                entry.bind("<Return>", self.check_word)

                if row != 0:
                    entry.configure(state="disabled")

                row_entries.append(entry)
                
            self.entries.append(row_entries)

        self.default_fg = self.entries[0][0].cget("fg_color")
        self.default_tc = self.entries[0][0].cget("text_color")

        self.random_word = random.choice(self.words_list).upper()


        self.button_playagain = ctk.CTkButton(self, text="Play again", width=200, height=50, command=self.play_again)
        self.button_playagain.pack(pady=10)

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


    def check_word(self, event=None):
        letters = []
        for col in range(5):
            letter = self.entries[self.current_row][col].get()
            letters.append(letter)
            
        entered_word = "".join(letters)

        if len(entered_word) != 5:
            return

        if entered_word not in self.valid_words:
            self.text.configure(text="Word not in dictionary!")
            return
            
        self.text.configure(text="After entering the word, press ENTER")

        target_letters = list(self.random_word)
        colors = ["gray"] * 5

        for i in range(5):
            if entered_word[i] == target_letters[i]:
                colors[i] = "green"
                target_letters[i] = None

        for i in range(5):
            if colors[i] == "green":
                continue
            if entered_word[i] in target_letters:
                colors[i] = "#b59f3b"
                target_letters[target_letters.index(entered_word[i])] = None

        for col in range(5):
            square = self.entries[self.current_row][col]
            square.configure(fg_color=colors[col], text_color="white", state="disabled")

        if entered_word == self.random_word:
            self.text.configure(text="You won!")
            return

        self.current_row += 1

        if self.current_row < 6:
            for col in range(5):
                next_square = self.entries[self.current_row][col]
                next_square.configure(state="normal")
            self.entries[self.current_row][0].focus()

    def play_again(self):
        self.text.configure(text="After entering the word, press ENTER")
        self.current_row = 0
        self.random_word = random.choice(self.words_list).upper()
        print(self.random_word)

        for row in range(6):
            for col in range(5):
                square = self.entries[row][col]
                square.configure(state="normal")
                square.delete(0, "end")
                square.configure(fg_color=self.default_fg, text_color=self.default_tc)
                
                if row != 0:
                    square.configure(state="disabled")
                    