from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip  # Copy and paste clipboard functions
import json

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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    given_password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": given_password
        }
    }

    if len(website) == 0 or len(given_password) == 0:
        messagebox.showwarning(title='Empty field', message="You hav empty field. Please do fill all the fields!")
    else:
        save_data = messagebox.askyesno(title=website, message=f"Verify if you want to proceed with these details:"
                                                               f"\nEmail: {email}\nPassword: {given_password}")
        if save_data:
            # with open('data.txt', mode='a') as file:
            #     file.write(f"{website} | {email} | {given_password}\n")

            # Exception handling
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)  # Reading a json file
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)  # Update a json data
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)  # Creating a json file, and dump data to it
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ------------------------------FIND PASSWORD ------------------------------------ #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title='Warning', message="No data file found")
    else:
        # try:
        #     website_name = data[website]
        # except KeyError as error_message:
        #     messagebox.showwarning(title='Warning', message=f"Website - {error_message} doesn't exist")
        # else:
        #     email = website_name['email']
        #     password = website_name['password']
        #     messagebox.showinfo(title=f"{website} - Email and Password", message=f"Email: {email}\nPassword: {password}")
        #     pyperclip.copy(password)  # The password will be copied to clipboard

        # If the above can be handled with if .. else, then go with if .. else
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website} - Email and Password", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title='Warning', message=f"Website - {website} doesn't exist")


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
search_button = Button(text='Search', width=16, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()

