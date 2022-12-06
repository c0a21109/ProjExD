import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_press(event):
    global key, jid
    key = event.keysym
    if jid is not None:
        root.after_cancel(jid)
        jid = None
    key = event.keysym


def key_release(event):
    global key
    key = ""

def main_proc():
    global mx, my, image, tmr, fly

    #壁の上に乗れないようにする
    if key == "w" or key == "Up":
        if fly == True or maze_list[mx][my-1] == 0:
            my -= 1
        else:
            pass

    if key == "s" or key == "Down":
        if fly == True or maze_list[mx][my+1] == 0:
            my += 1
        else:
            pass

    if key == "a" or key == "Left":
        if fly == True or maze_list[mx-1][my] == 0:
            mx -= 1
        else:
            pass
    if key == "d" or key == "Right":
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

    #時間を図る
    global jid
    if jid is not None:
        root.after_cancel(jid)
        jid = None

    if key == "f":

        if fly == True:
            fly = False
            canvas.delete("kokaton")
            canvas.create_image(mx*100+50, my*100+50,
                                image=image,
                                tag = "kokaton")

        else:
            fly = True
            canvas.delete("kokaton")
            canvas.create_image(mx*100+50, my*100+50,
                                image=toberubuta,
                                tag = "kokaton")
        
""""
#右クリックでこうかとんが飛ぶ
def kokaton_fly(event):
    global fly
    im = ""
    if fly == True:
        fly = False
        canvas.delete("kokaton")
        im=tk.PhotoImage(file="fig/0.png")
        canvas.create_image(mx*100+50, my*100+50,
                            image=im,
                            tag = "kokaton")

    else:
        fly = True
        canvas.delete("kokaton")
        im=tk.PhotoImage(file="fig/3.png")
        canvas.create_image(mx*100+50, my*100+50,
                            image=im,
                            tag = "kokaton")
    canvas.pack()
"""



if __name__ == "__main__":
    fly = False
    root = tk.Tk()
    root.title("迷えるこうかとん")

    #時間を表示する
    label = tk.Label(root, text = "-", font=("", 80))
    label.pack()

    tmr = 0
    jid = None

    #count_up()
    root.bind("<KeyPress>", key_press)

    #キャンバスを作る
    canvas = tk.Canvas(root, width=1500, height=900, bg=("black"))

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)

    mx, my = 1, 1
    #こうかとんのイメージを引っ張て来て貼る
    #root.bind("<3>", kokaton_fly)
    image=tk.PhotoImage(file="fig/0.png")#通常時のこうかとん
    toberubuta=tk.PhotoImage(file="fig/3.png")#飛んでる時のこうかとん
    canvas.create_image(mx*100+50, my*100+50,
                        image=image,
                        tag = "kokaton")
    canvas.pack()

    pause = False


    #ボタンを押したときの挙動
    key = ""
    root.bind("<KeyPress>", key_press)
    root.bind("<KeyRelease>", key_release)
    main_proc()
    root.mainloop()