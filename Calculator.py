from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7',  '8',  '9',  '/',  'C',
'4',  '5',  '6',  '*',  '<-',
'1',  '2',  '3',  '-',  ' ',
'0',  '.',  '=',  '+',  ' ' ]

def click(key):
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.insert(END, "=" + s)
    elif key=="C":
        display.delete(0,END)
    elif key=="<-":
        s=len(display.get())
        display.delete(s - 1,END)
    else:
        if "=" in str(display.get()):
            display.delete(0,END)
        print(display.get())
        display.insert(END, key)

def display_del():
    s=len(display.get())
    display.delete(s - 1,END)

def keyinput(event):
    print(event)
    if event.keysym>='0' and event.keysym<='9':
        display_del()
        click(event.keysym)
    elif event.keysym=="asterisk":
        display_del()
        display.insert(END, "*")
    elif event.keysym=="minus":
        display_del()
        display.insert(END, "-")
    elif event.keysym=="plus":
        display_del()
        display.insert(END, "+")
    elif event.keysym=="slash":
        display_del()
        display.insert(END, "/")
    elif event.keysym=="Return":
        click("=")
    elif event.keysym=="Escape":
        click("C")

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window, text=button_text, width=5,
		command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
display.focus_set()
window.bind_all('<KeyPress>', keyinput)
