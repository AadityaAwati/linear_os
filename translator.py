import googletrans
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyperclip
import speech_recognition as sr

window = Tk()
window.title('LangTrans')
window.iconbitmap("translator_icon.ico")
window.geometry("800x500")


def get_selected_language():
    return value_inside.get()


def get_translated_text():
    return text_entry.get()


def voice_translate_button_command():
    recogniser = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            voice = recogniser.listen(source)
            text = recogniser.recognize_google(voice)
            translator = googletrans.Translator()
            try:
                translated_text = translator.translate(text, dest=languages_short[languages.index(get_selected_language())]).text
            except ValueError:
                messagebox.showerror(title="LangTrans", message="Please fill out the language field")
            else:
                messagebox.showinfo(title="LangTrans", message=f"The translated text of {text} is {translated_text}.")
                pyperclip.copy(translated_text)
                # gtts.gTTS(translated_text)

    except:
        messagebox.showerror(title="LangTrans", message="Sorry We faced an error.\nPlease try speaking again.")


def translate_button_command():
    translator = googletrans.Translator()
    try:
        translated_text = translator.translate(get_translated_text(), dest=languages_short[languages.index(get_selected_language())]).text
    except ValueError:
        messagebox.showerror(title="LangTrans", message="Please fill out all the fields!")
    else:
        messagebox.showinfo(title="LangTrans", message=f"The translated text is {translated_text}")
        pyperclip.copy(translated_text)


img = ImageTk.PhotoImage(Image.open("translator_logo.png").resize((300, 300)))
img_label = Label(window, image=img)
img_label.grid(column=1)

label = Label(window, text="Enter your text here:", font=("", 20, ""), pady=20)
label.grid(column=0, row=1)

text_entry = Entry(window)
text_entry.grid(column=1, row=1)


languages = [googletrans.LANGUAGES[key] for key in googletrans.LANGUAGES]
languages_short = list(googletrans.LANGUAGES.keys())


value_inside = StringVar(window)
value_inside.set("Choose a language")

languages_menu = OptionMenu(window, value_inside, *languages)
languages_menu.grid(column=2, row=1)


voice_translate_button = Button(window, text=" Voice Translate", command=voice_translate_button_command, padx=10)
voice_translate_button.grid(column=0, row=2)

translate_button = Button(window, text=" Translate", command=translate_button_command, padx=10)
translate_button.grid(column=1, row=2)


window.mainloop()
