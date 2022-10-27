import tkinter


# Save Password Function
def save():
    with open('data.txt', 'a') as passwords:
        passwords.write(
            f'{email_entry.get()} | {website_entry.get()} | {password_entry.get()}\n')
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
password_button = tkinter.Button(text='Generate Password')
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
