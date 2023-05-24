from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Text
text = Text(width=30, height=5)
text.focus()  # Puts cursor in the textbox
text.insert(END, 'Example of multi-line string entry')
print(text.get('1.0', END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):  # Called with current scale value
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())  # Prints 1 if On button checked, otherwise 0.


checked_state = IntVar()  # variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()  # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))  # Gets current selection from listbox


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Canvas
canvas = Canvas(width=200, height=224)  # Inserts a layout one over another. Example: text over an image
tomato = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato)
canvas.create_text(102, 130, text="00:00", fill='white', font=('Ariel', 25, 'bold'))  # Inserts this text over the image
canvas.pack()

window.mainloop()
