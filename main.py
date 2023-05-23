from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label component
my_label = Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.pack()
my_label['text'] = 'New Text 1'  # Changing the kwarg 'text'
my_label.config(text='New Text 2')


# Button
def button_click():
    my_label['text'] = 'Clicked!!'


button = Button(text='Click Me!', command=button_click)
button.pack()

window.mainloop()
