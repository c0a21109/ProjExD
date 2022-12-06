import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科とん")
    canvas =tk.Canvas(root, width=1500, height=900, bg=("black"))
    cx, cy = 300, 400
    image=tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy,
                        image=image,
                        tag = "kokaton") 
    canvas.pack()   
    tk.mainloop()