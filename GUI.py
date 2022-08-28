import os
from tkinter import *
# import main
# import computer_main

# computer_code = computer_main()
# player_code = main()

root = Tk()
root.geometry("700x700")
title = root.title("PONG GAME")

def PVP_game():
    os.system('main.py')
    root.iconify()

def PVC_game():
    os.system('computer_main.py')
    root.iconify()

PVP = PhotoImage(file="Player_vs_Player.png")
PVC = PhotoImage(file="Player_vs_computer.png")

PLayer_button = Button(root,image=PVP,command=PVP_game)
PLayer_button.pack(padx=50,pady=80)

Computer_button = Button(root,image=PVC,command=PVC_game)
Computer_button.pack(padx=50,pady=80)





root.mainloop()