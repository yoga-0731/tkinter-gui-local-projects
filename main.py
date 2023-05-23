from tkinter import *


def button_click():
    my_label['text'] = entry.get()  # gets entry input


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adding padding to the entire screen

# Label component
my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
# Pack, Place and Grid examples - Layouts
# Note: We can't mix up pack(). place() and grid() for different components
# my_label.pack(side='left')
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)  # Grid is highly used for layouts
my_label.config(padx=50, pady=50)

# my_label['text'] = 'New Text 1'  # Changing the kwarg 'text'
# my_label.config(text='New Text 2')

# Button component
button_1 = Button(text='Click Me!', command=button_click)
# button.pack()
button_1.grid(column=1, row=1)

button_2 = Button(text='Click Me!', command=button_click)
# button.pack()
button_2.grid(column=2, row=0)

# Entry component - We can give our input in this box
entry = Entry(width=30)
entry.insert(END, string='Some text to begin with')  # Inserts a default text to the entry
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()
