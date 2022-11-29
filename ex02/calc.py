import tkinter as tk
import tkinter.messagebox as tkm

#練習3
def button_click(ev):
    btn = ev.widget
    txt = btn["text"]
    #練習３　tkm.showinfo(txt, f"[{txt}]button clicked")
    #練習７
    if txt == "=":
        fm = entry.get()
        entry.insert(tk.END, F"{txt}")
        entry.insert(tk.END, F"{eval(fm)}")
    #練習６
    else:
        entry.insert(tk.END, F"{txt}")


#練習１
root = tk.Tk()
root.title("計算機の見た目")
root.geometry("300x500")


#問題４
entry = tk.Entry(root, justify="right", width=10, font=("", 40))
entry.grid(row=0, column=0, columnspan=3)

#練習２
for i in range(10):
    button = str(i)
    button = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    #練習３
    button.bind("<1>", button_click)
    if i == 0:
        button.grid(row=4, column=0)
    else:
        button.grid(row=(9-i)//3 + 1, column=(i-1)%3)

#問題５
count = 9
ks = ["+"]
for i in ks:
    count += 1
    button_ks = i
    button_ks = tk.Button(root, text=f"{i}", width=4, height=2, font=("", 30))
    button_ks.bind("<1>", button_click)
    button_ks.grid(row=count//3 + 1, column=count%3)

button_equal = "="
button_equal = tk.Button(root, text="=", width=4, height=2, font=("", 30))
button_equal.bind("<1>", button_click)
button_equal.grid(row=4, column=2)

root.mainloop()