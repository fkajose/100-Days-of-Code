from tkinter import *
from tkinter import messagebox
import password_generator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = password_generator.password
    password_bar.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_bar.get().title()
    email = email_bar.get()
    password = password_bar.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        },
    }

    if website == '' or password == '' or email == '':
        messagebox.showinfo(title='Oops!', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except json.decoder.JSONDecodeError or FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating JSON file with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_bar.delete(0, END)
            password_bar.delete(0, END)


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            website = website_bar.get().title()
            if website in data.keys():
                messagebox.showinfo(website, f"Email/Username: {data[website]['email']}\nPassword: {data[website]['password']}")
            else:
                messagebox.showinfo(website, "No details exist for this website")
    except json.decoder.JSONDecodeError or FileNotFoundError:
        messagebox.showinfo('Oops!', "No data file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text='Website:')
website_text.grid(row=1, column=0)
email_text = Label(text='Email/Username:')
email_text.grid(row=2, column=0)
password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

# Entries
website_bar = Entry(width=35)
website_bar.grid(row=1, column=1, columnspan=1)
website_bar.focus()
email_bar = Entry(width=53)
email_bar.insert(0, 'harkhorlade@gmail.com')
email_bar.grid(row=2, column=1, columnspan=2)
password_bar = Entry(width=35, show="●")
password_bar.grid(row=3, column=1, columnspan=1)

# Buttons
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(row=1, column=2, columnspan=1)
generate_button = Button(text='Generate Password', width=14, command=generate_password)
generate_button.grid(row=3, column=2, columnspan=1)
add_button = Button(text='Add', width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
