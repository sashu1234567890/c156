
from tkinter import*
import random

root = Tk()
root.geometry("500x500")
root.title("Random colors")

dictionary = {"colour" : ["red","green","blue","yellow","cyan","brown","pink","purple","magenta","black"]}

def bgchange():
    random_number = random.randint(0, 9)
    print(dictionary["colour"][random_number])
    root.configure(background=dictionary["colour"][random_number])

btn = Button(root , text="CLICK ME" , command=bgchange)
btn.place(relx=0.5 , rely=0.5 , anchor=CENTER)

root.mainloop()