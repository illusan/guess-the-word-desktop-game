import customtkinter as ctk
import pygame # sound
from PIL import Image

app = ctk.CTk()
app.title("Game inspired by Wordle")
app.geometry("1280x720")

text_title = ctk.CTkLabel(app, text="Guess the word!")

frame = ctk.CTkFrame(app, bg_color="transparent")
frame.pack(pady=10)

button_pl = ctk.CTkButton(app, text="Graj po Polsku")
button_pl.pack()

button_eng = ctk.CTkButton(app, text="Play in English")
button_eng.pack()


app.mainloop()