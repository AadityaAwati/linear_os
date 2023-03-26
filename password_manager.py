from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

#---------------------------------------FIND PASSWORD---------------------------------------------#


def find_password():
    website = website_input.get()
    try:
       with open("data.json") as data_file:
          data = json.load(data_file)
    except FileNotFoundError:
          data_json = open("data.json","w")
          data_json.close()
          messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
      try:
        if len(website) != 0:
            info = data[website]
            password = info["password"]
            email = info["email"]
            messagebox.showinfo(title=f"{website}", message=f"Your email is {email}.\nYour password is {password}.")
            pyperclip.copy(password)
      except KeyError:
             messagebox.showwarning(title="Error", message=" No Details for the website exists!")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    user_data = []
    user_data.append(website_input.get())
    user_data.append(email_input.get())
    user_data.append(password_input.get())
    new_data = {
        user_data[0]:{
            "email": user_data[1],
            "password": user_data[2]
        }
    }

    if len(user_data[0]) == 0 or len(user_data[2]) == 0:
        messagebox.showinfo(title="OOPS", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                 data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                 json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                 json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Inputs

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "aaditya.awati@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

# Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()