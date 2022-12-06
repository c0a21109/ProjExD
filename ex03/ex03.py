import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":

    cx = 300
    cy = 400
    key = ""
    
    root = tk.Tk()
    root.title("迷える工科とん")

    #image = tk.PhotoImage(file = "fig/5.ping")
    canvas =tk.Canvas(root, width=1500, height=900, bg=("black"))
    canvas.create_image(cx, cy, image=image)
    canvas.pack()   
    

    tk.mainloop()