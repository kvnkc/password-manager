import tkinter
import random
import pyperclip
from tkinter import END, messagebox

# Password Generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for char in range(nr_letters)]

    random_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    random_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(tkinter.END, password)
    pyperclip.copy(password)

# Save Password Function


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title='oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as passwords:
                passwords.write(
                    f'{email} | {website} | {password}\n')
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# Password Manager UI
window = tkinter.Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=40, pady=40)
canvas = tkinter.Canvas(width=200, height=200)
lock = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, anchor='center', image=lock)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # starts cursor at website entry

email_label = tkinter.Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_entry = tkinter.Entry(width=35)
email_entry.insert(tkinter.END, 'kekecheung@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)
password_button = tkinter.Button(
    text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
