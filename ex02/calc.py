import tkinter as tk
import tkinter.messagebox as tkm

#練習3
def button_click(ev):
    btn = ev.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]button clicked")


#練習１
root = tk.Tk()
root.title("計算機の見た目")
root.geometry("300x500")

#練習2
for i in range(0, 10):
    button = str(i)
    #問題２　button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button.bind("<1>", button_click)
    button.grid(row=(9-i)//3, column=(9-i)%3)

root.mainloop()