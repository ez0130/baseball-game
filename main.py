from tkinter import *
from tkinter import ttk, messagebox
from random import sample
import time


# generating random number
def new_game():
    global answer
    answer = sample([x for x in range(0,9)], k = 5,)
    check_first_digit = True
    while check_first_digit:
        if answer[0] != 0:
            check_first_digit = False
            break
        else:
            answer = sample([x for x in range(0,9)], k = 5)   
    print(answer)
    # remove guesses
global try_count
try_count = 0
# check the answer

def reset_game():
    global answer, try_count
    try_count = 0
    canvas1.itemconfig(L1, text="_ _ _ _ _")
    canvas1.itemconfig(L2, text="20")
    for widget in canvas3.winfo_children():
        widget.destroy()
    new_game()

def check_answer():
    global try_count
    
    try_count += 1
    check_number = True
    for _ in E0.get():
        if _ not in [str(x) for x in range(0, 10)]:
            messagebox.showwarning(title="Error", message="Not 5 digit numbers")
            raise ValueError("Not numbers")
    a = []
    for _ in E0.get():
        a.append(int(_))
    if len(a) != 5:
        messagebox.showwarning(title="Error", message="Not 5 digit numbers")
        raise ValueError("Not 5 digit numbers")
    if len(set(E0.get())) != 5:
        messagebox.showwarning(title="Error", message="Duplicate numbers")
        raise ValueError("Duplicate numbers")

    strike = 0
    for x in range(0,5):
        if answer[x] == a[x]:
            strike += 1
    ball = len(set(a)&set(answer)) - strike
    if strike == 5:
        canvas1.itemconfig(L1, text = answer)
        messagebox.showwarning(title="Won", message="Congratulations!")
        reset_game()
        
    guessed_list = E0.get() + '    '+ str(strike) +'S' + str(ball) + 'B'
    E0.delete(0, 5)

    Label(canvas3, text = guessed_list).pack(anchor = 'n')
    print(try_count)
    canvas1.itemconfig(L2, text= 20-try_count)
 
    if try_count == 20:
        canvas1.itemconfig(L1, text = answer)
        messagebox.showwarning(title="Lost", message="You lost")
        window.after(1000, window.destroy)


window = Tk()
window.title("Baseball Game")
window.geometry("300x600")
window.config(padx=10, pady=3)
canvas1 = Canvas(width=600, height=150)
canvas2 = Canvas(width=500, height=10)
canvas3 = Canvas(width=600, height=800)

canvas1.place(x=0, y=0)
canvas2.place(x=0, y=60)
canvas3.place(x=0, y=100)   

'''
def motion(event):
  print("%s, %s" % (event.x, event.y))
  return
window.bind('<Button-1>', motion)
'''

window.update()
L1 = canvas1.create_text(80, 30, font="Times 20 italic bold", text = "_ _ _ _ _ ")
L2 = canvas1.create_text(224, 34, text = "20", font=("Ariel", 40, "italic"))
E0 = Entry(canvas2, width =20, font = 'Arial 10')
E0.pack()
E0.insert(0, "12345")


B1 = Button(canvas2, text= "Submit", command = check_answer)
B1.pack()

new_game()


'''
#menu      
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Schedule" )
filemenu.add_command(label="Open Schedule" )#command= )
filemenu.add_command(label="Save Schedule" )#command= )
filemenu.add_command(label="Exit", command= window.quit)
menubar.add_cascade(label="New", menu=filemenu)
#filemenu.add_separator
window.config(menu=menubar)
'''



window.mainloop()
