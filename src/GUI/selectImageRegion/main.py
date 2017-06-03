from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import Image

root = Tk()
topFrame = Frame(root)
topFrame.pack()


def choose_file():
    filename = askopenfilename(
        initialdir="/home/pj/pro/android/inBack/src/res/",
        title="Select file",
        filetypes=(("image file", "*.png"), ("All Files", "*.*")),
    )
    if not filename:
        print('do not select image')
        return
    im = PhotoImage(file=filename)
    container = Label(label, image=im)
    container.pack(side=TOP)
    # label.image = im
    # c.create_image(0, 0, image=im)


bChooseFile = Button(topFrame,
                     text='choose file',
                     fg='black',
                     command=choose_file)

bChooseFile.pack(side=TOP)
# canvasFrame = Frame(root)
# canvasFrame.pack(side=BOTTOM)
label = Label(root, text="empty")
label.pack(side=BOTTOM)

# Code to add widgets will go here...
root.mainloop()

# IMPORT: the tkinter do not support png(portable network graphics)
# this script was be drop off
