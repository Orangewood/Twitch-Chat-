import tkinter as tk
from PIL import Image, ImageTk

class TwitchBot(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = 'top', fill = 'both', expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Ditionary for the frames to be called from
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row = 0, column = 0, sticky ='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):


        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'testing123')
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img = tk.Button(self, image=render, text="When finished, click me to begin!", compound="top", bd=0, cursor="hand2")
        img.image = render
        img.pack(side="top", fill='both')
        #root.resizable(width=False, height=False)
        label.pack()



app = TwitchBot()
app.mainloop()
