from tkinter import *
from tkinter import messagebox
import random
from characters import letters, numbers, symbols


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
    """Saves the entered information into a file and reset the entry boxes"""
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Some fields are empty!")
    else:
        ok_or_cancel =messagebox.askokcancel(title=website_entry.get(), message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\n"
                                                                  f"It is ok to save?")

        if ok_or_cancel:
            with open("passwords.txt", "a") as passwords_file:
                passwords_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

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
website_entry.grid(row=2, column=2, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2, sticky="EW")
email_entry.insert(0, default_email)
password_entry = Entry(width=21)
password_entry.grid(row=4, column=2, sticky="EW")

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=3, sticky="EW")
add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(row=5, column=2, columnspan=2, sticky="EW")

window.mainloop()