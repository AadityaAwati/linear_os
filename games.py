from tkinter import *
import os

app = Tk()
app.title("Games")
app.iconbitmap("games_logo.ico")
app.geometry("600x600")
app.config(background="white")

main_label = Label(app, text="Games & Entertainers", font=("Calibri", 30, "bold"), background="white")
main_label.pack(anchor=CENTER, pady=40)

hand_distance_game_button = Button(app, text="Catch the ball Game", font=("Helvetica", 15, "bold"), borderwidth=0, foreground="blue", background="white",  command=lambda: os.system("python hand_distance_game.py"))
hand_distance_game_button.pack(anchor=CENTER, pady=20, padx=20)

pong_game_button = Button(app, text="Pong Game", font=("Helvetica", 15, "bold"), borderwidth=0, foreground="red", background="white",  command=lambda: os.system("python pong_game/main.py"))
pong_game_button.pack(anchor=CENTER, pady=20, padx=20)

million_dollar_art_piece_generator_button = Button(app, text="Colour Points", font=("Helvetica", 15, "bold"), borderwidth=0, foreground="yellow", background="white", command=lambda: os.system("python million_dollar_art_piece_generator.py"))
million_dollar_art_piece_generator_button.pack(anchor=CENTER, pady=20, padx=20)

quizler_button = Button(app, text="Quizler", font=("Helvetica", 15, "bold"), borderwidth=0, foreground="orange", background="white", command=lambda: os.system("python quizler/main.py"))
quizler_button.pack(anchor=CENTER, pady=20, padx=20)

turtle_road_crossing_game_button = Button(app, text="Turtle Road Crossing Game", font=("Helvetica", 15, "bold"), borderwidth=0, foreground="green", background="white",  command=lambda: os.system("python turtle_escape_game/main.py"))
turtle_road_crossing_game_button.pack(anchor=CENTER, pady=20, padx=20)


app.mainloop()
