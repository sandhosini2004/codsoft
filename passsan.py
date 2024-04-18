from tkinter import *
import random,string
root = Tk()
root.title("Password generator")
root.geometry("400x250")
user_input = Entry(root, width = 50)
user_input.pack()
def click():
    try:
        length = int(user_input.get())
        characters = string.ascii_letters + string.digits + string.punctuation

        if length <= 0:
            raise ValueError("Password length must be greater than 0")
        elif length > len(characters):
            raise ValueError(f"Password length is longer than characters {len(characters)}")

        password = "".join(random.sample(characters,length))
        label = Label(root, text = password)
        label.pack()

    except ValueError as e:
        label = Label(root, text = str(e), fg = "red")
        label.pack()
button = Button(root, padx = 50 , pady = 8, text="Generate Password", bg = "cornflowerblue", fg = "white", command = click)
button.pack()
root.mainloop()
