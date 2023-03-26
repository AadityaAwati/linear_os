from tkinter import *
from datetime import datetime
import os


def open_calculator():
    exec(open("calculator.py").read())


def open_camera():
    exec(open("camera.py").read())


def open_browser():
    os.system("python browser.py")


def open_ide():
    os.system("python ide.py")


def open_text_editor():
    os.system("python text_editor.py")


def open_games_app():
    os.system("python games.py")


def open_password_manager():
    os.system("python password_manager.py")


def open_translator():
    os.system("python translator.py")


def update():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_time_label["text"] = current_time
    main_window.after(1000, update)


main_window = Tk()
main_window.title("Linear")
main_window.geometry("1800x825")

bg_img = PhotoImage(file="background.png")
bg_img_label = Label(main_window, image=bg_img)
bg_img_label.place(x=0, y=0, relwidth=1, relheight=1)

current_time_label = Label(main_window, text="", font=("Helvetica", 20, "bold"), background="white")
current_time_label.pack(anchor=NE, padx=25, pady=25)

update()

calculator_logo = PhotoImage(file="calculator_logo.png")
calculator_button = Button(main_window, image=calculator_logo, command=open_calculator, borderwidth=0, background="white")
calculator_button.pack(anchor=NW, pady=20)

camera_logo = PhotoImage(file="camera_logo.png")
camera_button = Button(main_window, image=camera_logo, command=open_camera, borderwidth=0, background="white")
camera_button.pack(anchor=NW, pady=20)

browser_logo = PhotoImage(file="ocean_browser_logo.png")
browser_button = Button(main_window, image=browser_logo, command=open_browser, borderwidth=0, background="white")
browser_button.pack(anchor=NW, pady=20)

ide_logo = PhotoImage(file="ide_icon.png")
ide_button = Button(main_window, image=ide_logo, command=open_ide, borderwidth=0, background="white")
ide_button.pack(anchor=NW, pady=20)

text_editor_logo = PhotoImage(file="text_editor_logo.png")
text_editor_button = Button(main_window, image=text_editor_logo, command=open_text_editor, borderwidth=0, background="white")
text_editor_button.pack(anchor=NW, pady=20)

games_logo = PhotoImage(file="games_logo.png")
games_button = Button(main_window, image=games_logo, command=open_games_app, borderwidth=0, background="white")
games_button.pack(anchor=NW, pady=20)

password_manager_logo = PhotoImage(file="password_manager_logo.png")
password_manager_button = Button(main_window, image=password_manager_logo, command=open_password_manager, borderwidth=0, background="white")
password_manager_button.pack(anchor=NW, pady=20)

translator_logo = PhotoImage(file="translator_logo.png")
translator_button = Button(main_window, image=translator_logo, command=open_translator, borderwidth=0, background="white")
translator_button.pack(anchor=NW)

main_window.mainloop()
