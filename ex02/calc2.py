import tkinter as tk
import tkinter.messagebox as tkm

def button_click(ev):
    btn = ev.widget
    txt = btn["text"]
    entry.insert(tk.END, F"{txt}")  

def ap(ev):
    check = entry.get()
    checker = check(-1)
    btn = ev.widget
    txt = btn["text"]
    """"
    if checker.isdecimal() == True:
        tkm.showwarning("ぴえん", f"[{txt}]は２回連続で使えないよぅ")
    else:
        entry.insert(tk.END, F"{txt}")
    """""
    entry.insert(tk.END, F"{txt}")


def equal(ev):
    fm = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, F"{eval(fm)}")


root = tk.Tk()
root.title("計算機の見た目")
root.geometry("400x600")


entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=4)

for i in range(10):
    button = str(i)
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button.bind("<1>", button_click)
    if i == 0:
        button.grid(row=6, column=1)
    else:
        button.grid(row=(9-i)//3 + 3, column=(i+5)%3)

count = 1
ks = ["/", "*","-","+"]
for i in ks:
    count += 1
    button_ks = i
    button_ks = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button_ks.bind("<1>", ap)
    button_ks.grid(row=count, column=3)

#.
button_dot = "."
button_dot = tk.Button(root, text=".", width=4, height=2, font=("", 30))
button_dot.bind("<1>", ap)
button_dot.grid(row=6, column=2)

#=
button_equal = "="
button_equal = tk.Button(root, text="=", width=4, height=2, font=("", 30))
button_equal.bind("<1>", equal)
button_equal.grid(row=6, column=3)

root.mainloop()