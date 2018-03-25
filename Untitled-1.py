"""import PyQt5.QtWidgets as wi



app = wi.QApplication([])
sess = wi.QWidget()
sess.setWindowTitle("running")
sess.setGeometry(50,50,640,480)
sess.show()
print("done")
app.exec_()"""
"""import tkinter as tk

sess = tk.Frame()
sess.master.title("jeu")
sess.master.geometry("500x500+10+20")
button = tk.Button()
button['texte']
sess.mainloop()
print("2")"""

"""import tkinter as tk


    

fenetre = tk.Tk()
fenetre.title("right")


tk.Label(fenetre, text='Bienvenue ').grid(row=0, columnspan=2)

tk.Button(fenetre, text='jouer ').grid(row=1, column=0)
tk.Button(fenetre, text='quitter ').grid(row=1, column=1)


fenetre.mainloop()"""

import json
rar=12345
target = open('list_of_devices.json','r')
print(json.load(target))
target.close()

