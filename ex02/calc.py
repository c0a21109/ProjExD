import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("計算機の見た目")
root.geometry("300x500")

def button_click(ev):
    btn = ev.widget
    txt = btn