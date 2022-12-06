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
    global mx, my
    if key == "Up":
        if maze_list[mx][my-1] == 0:
            my -=1
        else:
            pass
    if key == "Down":
        if maze_list[mx][my+1] == 0:
            my +=1
        else:
            pass
    if key == "Left":
        if maze_list[mx-1][my] == 0:
            mx -= 1
        else:
            pass
    if key == "Right":
        if maze_list[mx+1][my] == 0:
            mx +=1
        else:
            pass
    canvas.coords("kokaton", mx*100+50, my*100+50)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科とん")
    
    canvas = tk.Canvas(root, width=1500, height=900, bg=("black"))

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)

    mx, my = 1, 1
    image=tk.PhotoImage(file="fig/8.png")
    canvas.create_image(mx*100+50, my*100+50,
                        image=image,
                        tag = "kokaton") 
    canvas.pack()

    #ボタンを押したときの挙動
    key = ""
    root.bind("<KeyPress>", key_press)
    root.bind("<KeyRelease>", key_release)
    main_proc()
    print(key)
    root.mainloop()