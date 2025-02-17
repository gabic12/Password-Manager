from characters import letters, numbers, symbols
from tkinter import *
from tkinter import messagebox
import random
import json


def generate_password():
    """Generates a password with random characters and displays it into the password entry box"""
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password_string = "".join(password_list)
    password_entry.insert(0, password_string)


def save_to_file():
    """Saves the entered information into a JSON file and reset the entry boxes"""
    new_password = {website_entry.get():
                        {
                            "email": email_entry.get(),
                            "password": password_entry.get()
                        }}
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Some fields are empty!")
    else:
        try: #If the file is created
            with open("passwords.json", "r") as passwords_file:
                passwords = json.load(passwords_file)
                passwords.update(new_password)
            with open("passwords.json", "w") as passwords_file:
                json.dump(passwords, passwords_file, indent=4)
        except FileNotFoundError: #File will be created if it doesn't exist
            with open("passwords.json", "w") as passwords_file:
                json.dump(new_password, passwords_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

def search_password():
    """Searches the JSON file for the entered website's info"""
    website = website_entry.get()
    try: #Check for the existence of the file
        with open("passwords.json", "r") as passwords_file:
            file_data = json.load(passwords_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found!")
    else:
        if website in file_data:
            messagebox.showinfo(title=website, message=f"Email: {file_data[website]["email"]}\nPassword: {file_data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"No info for {website} exists")

#Tkinter UI setup
default_email = "default_email@gmail.com"

#Window and canvas
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=1, column=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2, sticky="EW")
email_entry.insert(0, default_email)
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2, sticky="EW")

#Buttons
search_button = Button(text="Search", command=search_password)
search_button.grid(row=2, column=3, sticky="EW")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=5, column=2, columnspan=2, sticky="EW")

window.mainloop()