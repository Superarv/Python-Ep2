from tkinter import *
import os

root = Tk()
root.geometry('800x600')
root.title('tkinter tutorial')
root.resizable(False, False)
root.iconbitmap(os.path.join('Tuts', 'Assets2', 'calcicon.ico'))

def click():
    label =  Label(root, bg = 'Light Grey', fg = 'black', text = 'You clicked it!')
    label.grid(row = 1, column = 0)
    input = entry.get()
    print(input)
    if input == ('Bob', 'bob'):
        top = Tk()
        top.geometry('400x400')
        top.title('Authentication')
        top.resizable(False, False)


button = Button(root, bg = 'green', fg = 'white', text = 'Click me', font = ('Helvetica', 24), command = click)       # fg & bg
button.grid(row = 0, column = 0, columnspan = 1)

text = Text(root, height = 3, width = 20, bg = 'navy blue', fg = 'white', font = ('Courrier'))
text.grid(row = 0, column = 1,)

entry = Entry(root, text = 'Enter the passcode', width = 50)
entry.grid(row=0, column=2)





root.mainloop()




