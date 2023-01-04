import time
from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title('Hw5')
root.geometry('500x500')

l = Label(root, bg='blue',text=' Welcome to drunk game ',font= ("Arial",25)).grid(column=0,row=0,padx=60)
l1 = Label(root, bg='yellow',text='Rules:\nPress button when you see RED Colour',font= ("Arial",16)).grid(column=0,row=1,padx=60)


timer: float = 0.0
counter: int = 0


def btn_game_press():
    change()
    count()


def change():
    global timer
    end_time = time.time()
    if l2.cget("bg") == 'red':
        l4.config(text=f"Time of your reaction was: {round(end_time-timer,3)} seconds")


def count():
    if l2.cget("bg") != 'red':
        global counter
        counter += 1
        l5.config(text=f'Count of missclicks: {counter}')


def random_colour():
    import random
    var = random.choice(['blue', 'yellow', 'green', 'red', 'white', 'black', 'violet'])
    return var


def change_colour():
    global timer
    val = random_colour()
    l2.config(bg=val)
    if l2.cget("bg") != 'red':
        l2.after(2000, change_colour)
    elif l2.cget("bg") == 'red':
        start_time = time.time()
        timer = float(start_time)


l2 = Label(root, bg='black', width = 30, height = 10)
# l3 = Label(root, bg='purple', text='number of unsuccessful clicks:')
btn_game = Button(root, text='PRESS ME ON RED', command=btn_game_press)
l4 = Label(root, bg='grey', text=f'You will see your reaction time here')
btn_start_game = Button(text='Start Game', command=change_colour)
l5 = Label(root,bg='grey', text=f'Count of missclicks: ')

l2.grid(column=0, row=3, padx=60)
# l3.grid(column=0, row=4, pady=5)
btn_game.grid(column=0, row=5, padx=60,pady=5)
l4.grid(column=0, row=9, pady=5)
btn_start_game.grid(column=0, row=2, pady=10)
l5.grid(column=0, row=10, pady=5)


root.mainloop()
