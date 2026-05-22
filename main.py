import customtkinter as ctk
import pygame # sound
import random
from settings import SettingsFrame
from game_eng import GameEngFrame
from game_pl import GamePlFrame
from pathlib import Path


words_pl_path = Path('data/words_pl.txt')
words_pl = words_pl_path.read_text(encoding='utf-8').split()

words_eng_path = Path('data/words_eng.txt')
words_eng = words_eng_path.read_text(encoding='utf-8').split()


app = ctk.CTk()
app.title("Game inspired by Wordle")
app.geometry("1280x720")
#app.resizable(False, False)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

full_screen = False

def set_screen_mode(choice):
    if choice == "Fullscreen":
        app.attributes("-fullscreen", True)
    elif choice == "Windowed":
        app.attributes("-fullscreen", False)


def show_settings():
    settings_frame.tkraise()

def back_callback():
    main_menu_frame.tkraise()

def show_game_eng():
    game_eng_frame.tkraise()

def show_game_pl():
    game_pl_frame.tkraise()


main_menu_frame = ctk.CTkFrame(app)
main_menu_frame.grid(row=0, column=0, sticky="nsew")

text_title = ctk.CTkLabel(main_menu_frame, text="Guess the word game!", font=("Arial", 50))
text_title.pack(pady=(100, 0))

text2 = ctk.CTkLabel(main_menu_frame, text="( based on the game Wordle )", font=("Arial", 17), bg_color="transparent")
text2.pack(pady=(5, 0))



frame = ctk.CTkFrame(main_menu_frame, bg_color="transparent")
frame.pack(pady=(100, 0))

button_pl = ctk.CTkButton(frame, text="Graj po Polsku (PL)", width=200, height=50, command=show_game_pl)
button_pl.grid(row=0, column=0, padx=10, pady=10)

button_eng = ctk.CTkButton(frame, text="Play in English (ENG)", width=200, height=50, command=show_game_eng)
button_eng.grid(row=1, column=0, padx=10, pady=10)

button_settings = ctk.CTkButton(frame, text="Settings", width=200, height=50, command=show_settings)
button_settings.grid(row=2, column=0, padx=10, pady=10)

button_exit = ctk.CTkButton(frame, text="Exit game", width=200, height=50, command=app.quit)
button_exit.grid(row=3, column=0, padx=10, pady=10)


settings_frame = SettingsFrame(app, switch_screen_callback=set_screen_mode, back_callback=back_callback)
settings_frame.grid(row=0, column=0, sticky="nsew")

game_eng_frame = GameEngFrame(app, back_callback=back_callback, words_list = words_eng)
game_eng_frame.grid(row=0, column=0, sticky="nsew")

game_pl_frame = GamePlFrame(app, back_callback=back_callback, words_list = words_pl)
game_pl_frame.grid(row=0, column=0, sticky="nsew")


main_menu_frame.tkraise()

app.mainloop()