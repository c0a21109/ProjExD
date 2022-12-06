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
    global mx, my, image
    fly = False

    if key == "space":
        if fly == True:
            fly = False
            image = tk.PhotoImage(file="fig/0.png")
        else:
            fly = True
            image = tk.PhotoImage(file="fig/3.png")

    #壁の上に乗れないようにする
    if key == "Up":
        if fly == True or maze_list[mx][my-1] == 0:
            my -= 1
        else:
            pass

    if key == "Down":
        if fly == True or maze_list[mx][my+1] == 0:
            my += 1
        else:
            pass

    if key == "Left":
        if fly == True or maze_list[mx-1][my] == 0:
            mx -= 1
        else:
            pass
    if key == "Right":
        if fly == True or maze_list[mx+1][my] == 0:
            mx += 1
        else:
            pass
    
    #リスタートできるようにする
    if key == "r":
        my, mx = 1, 1

    #こうかとんが移動する
    canvas.coords("kokaton", mx*100+50, my*100+50)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷える工科とん")

    #キャンバスを作る
    canvas = tk.Canvas(root, width=1500, height=900, bg=("black"))

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)

    mx, my = 1, 1
    #こうかとんのイメージを引っ張て来て貼る
    image=tk.PhotoImage(file="fig/0.png")
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