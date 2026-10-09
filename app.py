import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TIREX CHEATS")
root.geometry("420x280")
root.configure(bg="#111111")
root.resizable(False, False)

title = tk.Label(
    root, text="TIREX CHEATS",
    font=("Arial", 22, "bold"),
    fg="#ff3333", bg="#111111"
)
title.pack(pady=(28, 12))

tk.Label(
    root, text="Projeto independente",
    font=("Arial", 11),
    fg="white", bg="#111111"
).pack(pady=4)

tk.Label(
    root, text="Configuracao: 31/12/2033",
    font=("Arial", 10),
    fg="#bbbbbb", bg="#111111"
).pack(pady=4)

tk.Label(
    root, text="Aplicativo de demonstracao",
    font=("Arial", 9),
    fg="#888888", bg="#111111"
).pack(pady=12)

root.mainloop()
