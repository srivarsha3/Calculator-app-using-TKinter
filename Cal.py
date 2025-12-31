import tkinter as tk
def press(v):
    entry.insert(tk.END,v)
'''called when a number or operator button is clicked
Inserts the pressed value at the end of Entry widget'''
def clear():
    entry.delete(0,tk.END)
'''called when the clear button is clicked
Deletes all content from Entry widget from index 0 to end'''

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)
    #entry.delete(0, tk.END)
    #entry.insert(0, current[:-1])
'''called when the backspace button is clicked
Removes the last character from the Entry widget'''

def calc():
    try:
        result=eval(entry.get())
        '''entry.get() retreives the expression (e.g. 5+3)
        eval() evaluates the string as a python expression'''
        entry.delete(0,tk.END)
        '''Deletes all content from Entry widget from index 0 to end'''
        entry.insert(0,result)
        '''Inserts the result at index 0 of Entry widget'''

    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error occured")
        '''If an error occurs during evaluation,(5++)
        display appropriate message instead of crashing'''

#main window creation
root=tk.Tk()#creates the main application window
root.title("CALCULATOR")#sets the title of the window

root.configure(bg="#1e1e1e")#sets background color
root.resizable(False,False)#prevents resizing of the window

#entry window(display screen)
entry=tk.Entry(
root,font=('Arial',24),bd=0,justify="right",bg="#3e3e3e",fg="white")
'''Text input field where expressions and results are displayed
right alined for better calculator look'''
entry.grid(row=0,column=0,columnspan=4,pady=10,padx=10,ipady=10)
#places the Entry widget in the grid layout at row 0, column 0
#spanning 4 columns with padding
#button labels
buttons=[
'7','8','9','/',
'4','5','6','*',
'1','2','3','-',
'0','.','=','+'
]
'''Represent calculator buttons stored in a list to reduce repetitive code'''
#Dynamic button creation
r=1
c=0
for b in buttons:
    cmd=calc if b=='=' else lambda x=b: press(x)
    '''If button is '=', assign calc function to cmd
    otherwise,call press() with the button value
    lambda x=b prevents late binding issue in loops'''
    button=tk.Button(
    root,
    text=b,
    command=cmd,#tthese three lines creates a button widget
    width=5,
    height=2,
    font=('Arial',18),
    bd=0,
    bg="#ff9500" if b in "+-*/" else "#3a3a3a",
    fg="white"
    
    ).grid(row=r,column=c,pady=5,padx=5)
    #places the button in the grid layout at specified row and column
    
    c+=1
    if c==4:
        c=0
        r+=1
    '''moves to next row after every 4 buttons'''
#clear button
clear_button=tk.Button(
root,
text="C",
command=clear,
width=5,
height=2,
font=('Arial',18),
bd=0,
bg="#3a3a3a",
fg="white"
).grid(row=r,column=c,columnspan=2,pady=5,padx=5)

tk.Button(
    root,
    text="⌫",
    command=backspace,
    width=5,
    height=2,
    font=('Arial', 18),
    bd=0,
    bg="#3a3a3a",
    fg="white"
).grid(row=r, column=2,columnspan=2, pady=5, padx=5)

#starts the main event loop
root.mainloop()
