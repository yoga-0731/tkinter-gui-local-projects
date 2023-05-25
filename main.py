from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip  # Copy and paste clipboard functions

window = Tk()
window.title('Password Generator')
window.config(padx=40, pady=40)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(numbers) for _ in range(nr_symbols)]
    password_list += [choice(symbols) for _ in range(nr_numbers)]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    print(pyperclip.paste())
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    given_password = password_entry.get()
    if len(website) == 0 or len(given_password) == 0:
        messagebox.showwarning(title='Empty field', message="You hav empty field. Please do fill all the fields!")
    else:
        save_data = messagebox.askyesno(title=website, message=f"Verify if you want to proceed with these details:"
                                                               f"\nEmail: {email}\nPassword: {given_password}")
        if save_data:
            with open('data.txt', mode='a') as file:
                file.write(f"{website} | {email} | {given_password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'yoga@gmail.com')
password_entry = Entry(width=15)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text='Generate Password', width=16, command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

