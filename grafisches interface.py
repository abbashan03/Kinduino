# import um fenster zu erstellen
from tkinter import *
from tkinter import messagebox

# folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def Start_action():
    Ergebnis_label.config(text="Fertig")
    
def controlle_action():
    coreckt_label.config(text="coreckt")

# fenster wierd erstelt 
fenster = Tk()
fenster.title("Kinduino")

# Label und Buttons erstellen.
Start_button = Button(fenster, text="Start", command=Start_action)
controlle_button = Button(fenster, text="kontrollieren", command=controlle_action)
Ergebnis_label = Label(fenster, text="")
coreckt_label = Label(fenster, text="")


# Eingabe
eingabefeld = Entry(fenster, bd=5, width=70)


# definieren der Grösse des Fensters
fenster.geometry("450x400")
# absoluten Koordinaten um die Komponenten zu
# setzen und die Grösse definieren
Ergebnis_label.place(x = 350, y = 300, width=50, height=50)
Start_button.place(x = 10, y = 0, width=50, height=50)
coreckt_label.place(x = 350, y = 260, width=50, height=50)
controlle_button.place(x = 60, y = 0, width=80, height=50)
eingabefeld.place(x = 3, y = 60)

# wartet auf eingabe
fenster.mainloop()

#https://pythonbuch.com/gui.html


































#Quelle
#https://pythonbuch.com/gui.html
