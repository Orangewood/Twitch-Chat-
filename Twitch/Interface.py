import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser


class Window(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.master = master
        self.pack(side="right", fill=BOTH, expand="yes")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img = Button(self, image = render, text = "Click me to start!", compound = TOP, bd = 0, cursor="hand2")
        img.image = render
        img.pack(side = TOP, fill = BOTH)
        root.resizable(width=False, height=False)



        #Label frame for information
        self.labelFrame = ttk.LabelFrame(self, text = 'Welcome to my bot!')
        self.labelFrame.pack(side = 'bottom', fill = BOTH, expand = 'yes')
        self.User()
        self.Password()
        self.Channel()




    def User (self):

        username= tk.Label(self.labelFrame, text = "Twitch username: ", anchor = "w")
        username.pack(side = 'top', fill = X, expand = 'yes')
        entry_username = Entry(self.labelFrame, bd = 3)
        entry_username.pack(side ='top', fill = X, expand = 'yes')

    def Password(self):

        def Callback(event):
            webbrowser.open_new(("https://twitchapps.com/tmi/"))


        pass_ouath = tk.Label(self.labelFrame, text = "Authorization password: ",  fg="blue", cursor="hand2", anchor = "w")
        pass_ouath.pack(side = "top", fill = X, expand ="yes")
        pass_ouath.bind("<Button-1>", Callback)
        entry_pass_ouath = Entry(self.labelFrame, bd=3)
        entry_pass_ouath.pack( side = 'top' , fill=X, expand='yes')


    def Channel (self):

        channel_interval = tk.Label(self.labelFrame, text = "Twitch URL Channel: ", anchor = "w")
        channel_interval.pack(side = 'top', fill = X, expand = 'no')
        entry_channel_interval = Entry(self.labelFrame, bd=3)
        entry_channel_interval.pack(side='bottom', fill=X, expand='yes')
        entry_channel_interval.insert(0, "Example: https://www.twitch.tv/example")



#class BottomWindow(Botframe):

    #def __init__(self):


root = Tk()
app = Window(root)
root.wm_title("Twitch Chat Bot")
root.geometry('500x600')
root.mainloop()

