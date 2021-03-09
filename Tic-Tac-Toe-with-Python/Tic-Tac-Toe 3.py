from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

ActivePlayer = 1  # set active player
p1 = []  # What player 1 selected
p2 = []  # What player 2 selected
root = Tk()
root.title('Tic Tac Toy : Player 1')
style = ttk.Style()
style.theme_use('classic')
b1 = ttk.Button(root, text=' ')  # button1
b1.grid(row=0, column=0, sticky='wsen', ipadx=40, ipady=40)
b1.config(command=lambda: bu_click(1))

b2 = ttk.Button(root, text=' ')  # 2 
b2.grid(row=0, column=1, sticky='wsen', ipadx=40, ipady=40)
b2.config(command=lambda: bu_click(2))

b3 = ttk.Button(root, text=' ')  # 3
b3.grid(row=0, column=2, sticky='wsen', ipadx=40, ipady=40)
b3.config(command=lambda: bu_click(3))

b4 = ttk.Button(root, text=' ')  # 4
b4.grid(row=1, column=0, sticky='wsen', ipadx=40, ipady=40)
b4.config(command=lambda: bu_click(4))

b5 = ttk.Button(root, text=' ')  # 5
b5.grid(row=1, column=1, sticky='wsen', ipadx=40, ipady=40)
b5.config(command=lambda: bu_click(5))

b6 = ttk.Button(root, text=' ')  # 6
b6.grid(row=1, column=2, sticky='wsen', ipadx=40, ipady=40)
b6.config(command=lambda: bu_click(6))

b7 = ttk.Button(root, text=' ')  # 7
b7.grid(row=2, column=0, sticky='wsen', ipadx=40, ipady=40)
b7.config(command=lambda: bu_click(7))

b8 = ttk.Button(root, text=' ')  # 8
b8.grid(row=2, column=1, sticky='wsen', ipadx=40, ipady=40)
b8.config(command=lambda: bu_click(8))

b9 = ttk.Button(root, text=' ')  # 9
b9.grid(row=2, column=2, sticky='wsen', ipadx=40, ipady=40)
b9.config(command=lambda: bu_click(9))

userInput = int(input('For 2 player enter [1] For Vs PC enter[2]: '))


def bu_click(x):
    global ActivePlayer
    global p1
    global p2
    if userInput == 1:
        if ActivePlayer == 1:
            set_layout(x, 'X')
            p1.append(x)
            root.title('Tic Tac Toy : Player 2')
            ActivePlayer = 2
            print('P1:{}'.format(p1))
        elif ActivePlayer == 2:
            set_layout(x, 'O')
            p2.append(x)
            root.title('Tic Tac Toy : Player 1')
            ActivePlayer = 1
            print('P2:{}'.format(p2))
        check_winner()
    if userInput == 2:
        if ActivePlayer == 1:
            set_layout(x, 'X')
            p1.append(x)
            root.title('Tic Tac Toy : Player 2')
            ActivePlayer = 2
            print('P1:{}'.format(p1))
            auto_play()
        elif ActivePlayer == 2:
            set_layout(x, 'O')
            p2.append(x)
            root.title('Tic Tac Toy : Player 1')
            ActivePlayer = 1
            print('P2:{}'.format(p2))
        check_winner()


def set_layout(x, text):
    if x == 1:  
        b1.config(text=text)
        b1.state(['disabled'])
    elif x == 2:
        b2.config(text=text)
        b2.state(['disabled'])
    elif x == 3:
        b3.config(text=text)
        b3.state(['disabled'])
    elif x == 4:
        b4.config(text=text)
        b4.state(['disabled'])
    elif x == 5:
        b5.config(text=text)
        b5.state(['disabled'])
    elif x == 6:
        b6.config(text=text)
        b6.state(['disabled'])
    elif x == 7:
        b7.config(text=text)
        b7.state(['disabled'])
    elif x == 8:
        b8.config(text=text)
        b8.state(['disabled'])
    elif x == 9:
        b9.config(text=text)
        b9.state(['disabled'])


def check_winner():
    winner = -1
    if 1 in p1 and 2 in p1 and 3 in p1:
        winner = 1
    elif 1 in p2 and 2 in p2 and 3 in p2:
        winner = 2
    if 4 in p1 and 5 in p1 and 6 in p1:
        winner = 1
    elif 4 in p2 and 5 in p2 and 6 in p2:
        winner = 2

    if 7 in p1 and 8 in p1 and 9 in p1:
        winner = 1
    elif 7 in p2 and 8 in p2 and 9 in p2:
        winner = 2

    if 1 in p1 and 4 in p1 and 7 in p1:
        winner = 1
    elif 1 in p2 and 4 in p2 and 7 in p2:
        winner = 2

    if 2 in p1 and 5 in p1 and 8 in p1:
        winner = 1
    elif 2 in p2 and 5 in p2 and 8 in p2:
        winner = 2

    if 3 in p1 and 6 in p1 and 9 in p1:
        winner = 1
    elif 3 in p2 and 6 in p2 and 9 in p2:
        winner = 2

    if winner == 1:
        messagebox.showinfo(title='Cong.', message='Player 1 is winner')
    if winner == 2:
        messagebox.showinfo(title='Cong.', message='Player 2 is winner')


def auto_play():
    global p1
    global p2
    empty_cell = []
    for cell in range(9):
        if not (cell + 1 in p1 or cell + 1 in p2):
            empty_cell.append(cell + 1)
    rand_index = randint(0, len(empty_cell) - 1)
    bu_click(empty_cell[rand_index])


root.mainloop()