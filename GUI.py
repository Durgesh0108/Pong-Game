import os
from tkinter import *

# import main
# import computer_main

# computer_code = computer_main()
# player_code = main()


root = Tk()
root.geometry("562x533")
title = root.title("PONG GAME")

BackgroundImage = PhotoImage(file="Background_image_new.png")
# root.config(background=BackgroundImage)
label = Label(image=BackgroundImage)
label.place(x=0, y=0)


def PVP_game():
    root.iconify()
    os.system('main.py')


def PVC_game():
    root.iconify()
    os.system('computer_main.py')


PVP = PhotoImage(file="Player_vs_Player.png")
PVC = PhotoImage(file="Player_vs_computer.png")

PLayer_button = Button(root, image=PVP, command=PVP_game)
# PLayer_button.place(x=180,y=80)
PLayer_button.pack(pady=40)

Computer_button = Button(root, image=PVC, command=PVC_game)
# Computer_button.place(x=180,y=310)
Computer_button.pack(pady=40)

root.mainloop()
