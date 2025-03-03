import tkinter as tk
import random as r


score = 0
countdown = 30


def click1(event):
    global score
    if countdown > 0:
        score += 1
        scorlbl.config(text=f"Pontuação: {score}")


def move1():
    global countdown
    if countdown > 0:
        x = r.randint(10, 400)
        y = r.randint(10, 400)
        canvas.coords(sqr, x, y, x+50, y+50)
        root.after(r.randint(500, 700), move1)
    else:
        canvas.itemconfig(sqr, fill="#000000")


def timer():
    global countdown
    if not countdown == 0:
        countdown -= 1
        timelbl.config(text=f"Tempo: {countdown}")
        root.after(1000, timer)


root = tk.Tk()
root.title("Clique no quadrado")
root.geometry("500x600")
root.wm_resizable(width=False, height=False)

canvas = tk.Canvas(root, width=500, height=500, bg="#FFFFFF")
canvas.pack()

countdown += 1

sqr = canvas.create_rectangle(50, 50, 100, 100, fill="#FF0000")

scorlbl = tk.Label(root, text=f"Pontuação: {score}", font="Fixedsys 18 bold")
scorlbl.pack()
timelbl = tk.Label(root, text=f"Tempo: {countdown}", font="Fixedsys 18 bold")
timelbl.pack()

canvas.tag_bind(sqr, "<Button-1>", click1)

move1()
timer()

root.mainloop()
