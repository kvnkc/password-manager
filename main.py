import tkinter

# Password Manager UI
window = tkinter.Tk()
window.title('Password Manager')
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
lock = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock, anchor=tkinter.CENTER)


window.mainloop()
