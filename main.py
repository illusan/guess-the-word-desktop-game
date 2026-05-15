import customtkinter as ctk
import pygame # sound
from settings import SettingsFrame
from game_eng import GameEngFrame
from game_pl import GamePlFrame

app = ctk.CTk()
app.title("Game inspired by Wordle")
app.geometry("1280x720")
#app.resizable(False, False)

full_screen = False

def set_screen_mode(choice):
    if choice == "Fullscreen":
        app.attributes("-fullscreen", True)
    elif choice == "Windowed":
        app.attributes("-fullscreen", False)


def show_settings():
    main_menu_frame.pack_forget() # hiding main menu
    settings_frame.pack(fill="both", expand=True) # showing settings
    app.after(20, app.update)

def back_callback():
    settings_frame.pack_forget() 
    game_eng_frame.pack_forget()
    game_pl_frame.pack_forget()
    main_menu_frame.pack(fill="both", expand=True) 
    app.after(20, app.update)

def show_game_eng():
    main_menu_frame.pack_forget()
    game_eng_frame.pack(fill="both", expand=True)
    app.after(20, app.update)

def show_game_pl():
    main_menu_frame.pack_forget()
    game_pl_frame.pack(fill="both", expand=True)
    app.after(20, app.update)

main_menu_frame = ctk.CTkFrame(app, fg_color="transparent")
main_menu_frame.pack(fill="both", expand=True)

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
game_eng_frame = GameEngFrame(app, back_callback=back_callback)
game_pl_frame = GamePlFrame(app, back_callback=back_callback)

app.mainloop()