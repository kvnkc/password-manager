import tkinter

# Password Manager UI
window = tkinter.Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
lock = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, anchor='center', image=lock)
canvas.pack()


window.mainloop()
