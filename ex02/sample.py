import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("test")
root.geometry("500x200")

def button_click(ev):
    btn = ev.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]button clicked")

label = tk.Label(root,
                text = "Label",
                font = ("", 20)
                )
label.pack()

button = tk.Button(root, text = "emargency")
button.bind("<1>", button_click)
button.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "write here")
entry.pack()

root.mainloop()


