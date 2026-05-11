import customtkinter as ctk
import pygame # sound
#from options import OptionsFrame

app = ctk.CTk()
app.title("Game inspired by Wordle")
app.geometry("1280x720")
app.resizable(False, False)

full_screen = False

def set_screen_mode(choice):
    if choice == "Fullscreen":
        app.attributes("-fullscreen", True)
    elif choice == "Windowed":
        app.attributes("-fullscreen", False)



text_title = ctk.CTkLabel(app, text="Guess the word game!", font=("Arial", 50))
text_title.pack(pady=(100, 0))

text2 = ctk.CTkLabel(app, text="( based on the game Wordle )", font=("Arial", 17), bg_color="transparent")
text2.pack(pady=(5, 0))



frame = ctk.CTkFrame(app, bg_color="transparent")
frame.pack(pady=(100, 0))

button_pl = ctk.CTkButton(frame, text="Graj po Polsku (PL)", width=200, height=50)
button_pl.grid(row=0, column=0, padx=10, pady=10)

button_eng = ctk.CTkButton(frame, text="Play in English (ENG)", width=200, height=50)
button_eng.grid(row=1, column=0, padx=10, pady=10)

button_exit = ctk.CTkButton(frame, text="Exit game", width=200, height=50)
button_exit.grid(row=2, column=0, padx=10, pady=10)

button_options = ctk.CTkButton(frame, text="Options", width=200, height=50)
button_options.grid(row=3, column=0, padx=10, pady=10)


#option = ctk.CTkOptionMenu(frame, values=["Fullscreen", "Windowed"], width=200)
#option.grid(row=3, column=0, padx=10, pady=10)



app.mainloop()