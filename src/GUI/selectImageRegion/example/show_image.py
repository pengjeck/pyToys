import tkinter as tk
from PIL import ImageTk, Image

# This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("1300x700")
window.configure(background='grey')

path = "/home/pj/pro/android/inBack/src/res/metaMaterial/_1/1_element.png"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image=img)

# The Pack geometry manager packs widgets in rows or columns.
panel.pack(side="bottom", fill="both", expand="yes")

# Start the GUI
window.mainloop()
