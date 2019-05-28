# import um fenster zu erstellen
from tkinter import *


# folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def Start_action():
    f = open("test","w+")
    f.write()
    f.close
    
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
t = Text(fenster, bd=5, height=20, width=54)
t.pack()


# definieren der Grösse des Fensters
fenster.geometry("450x400")
# absoluten Koordinaten um die Komponenten zu
# setzen und die Grösse definieren
Ergebnis_label.place(x = 350, y = 300, width=50, height=50)
Start_button.place(x = 10, y = 0, width=50, height=50)
coreckt_label.place(x = 350, y = 260, width=50, height=50)
controlle_button.place(x = 60, y = 0, width=80, height=50)
t.place(x = 3, y = 60)

# wartet auf eingabe
fenster.mainloop()

#https://pythonbuch.com/gui.html
#https://www.devdungeon.com/content/gui-programming-python
#https://stackoverflow.com/questions/24501606/tkinter-python-entry-height
#https://www.guru99.com/reading-and-writing-files-in-python.html#1
#https://www.pythoncentral.io/reading-and-writing-to-files-in-python/



































