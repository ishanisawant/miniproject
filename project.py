import tkinter as tk
from tkinter import font

app = tk.Tk()
app.title("Font Modifier")

text_entry = tk.Entry(app, font=("Arial", 12))
text_entry.pack(pady=10)


def change_text_style():
    entered_text = text_entry.get()
    selected_font = selected_font_var.get()
    selected_size = selected_size_var.get()
    text_output.config(text=entered_text, font=(selected_font, selected_size))


font_styles = [
    "Arial",
    "Helvetica",
    "Times New Roman",
    "Courier New",
    "Verdana",
    "Georgia",
    "Comic Sans MS",
]
selected_font_var = tk.StringVar()
selected_font_var.set(font_styles[0])
font_menu = tk.OptionMenu(app, selected_font_var, *font_styles)
font_menu.pack(pady=5)


text_sizes = [10, 12, 16, 20, 24, 28, 32]
selected_size_var = tk.IntVar()
selected_size_var.set(text_sizes[1])
size_menu = tk.OptionMenu(app, selected_size_var, *text_sizes)
size_menu.pack(pady=5)

apply_button = tk.Button(app, text="Apply", command=change_text_style)
apply_button.pack(pady=10)

text_output = tk.Label(app, text="", font=("Arial", 12))
text_output.pack(pady=10)

app.mainloop()