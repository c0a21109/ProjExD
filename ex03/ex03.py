import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_press(event):
    global key
    key = event.keysym


def key_release(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    if key == "Up"   :  cy -=20
    if key == "Down" :  cy +=20
    if key == "Left" :  cx -=20
    if key == "Right":  cx +=20
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科とん")

    canvas = tk.Canvas(root, width=1500, height=900, bg=("black"))
    cx, cy = 300, 400
    image=tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy,
                        image=image,
                        tag = "kokaton") 
    canvas.pack()

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)

    #ボタンを押したときの挙動
    key = ""
    root.bind("<KeyPress>", key_press)
    root.bind("<KeyRelease>", key_release)
    main_proc()
    print(key)
    root.mainloop()