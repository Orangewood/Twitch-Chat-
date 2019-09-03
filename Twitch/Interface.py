import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser


class Window(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.master = master
        self.pack(side="top", fill=BOTH, expand="yes")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img = Button(self, image=render, text="When finished, click me to begin!", compound=TOP, bd=0, cursor="hand2")
        img.image = render
        img.pack(side=TOP, fill=BOTH)
        root.resizable(width=False, height=False)
        self.labelFrame = ttk.LabelFrame(self, text='Welcome! ')
        self.labelFrame.pack(side="bottom", fill=BOTH, expand='yes')


        self.Bottom_Window.Buttons(self)
        self.Bottom_Window.User(self)
        self.Bottom_Window.Password(self)
        self.Bottom_Window.Channel(self)
        self.Bottom_Window(self)
        #self.Bottom_Window.Text_Area(self)


    class Bottom_Window(Frame):



        def __init__(self, Window):
            Frame.__init__(self)

            self.pack(side="bottom", fill = BOTH, expand = 'yes')
            #self.pack_forget()
            self.labelBottomFrame = ttk.LabelFrame(self, text = 'testing123')
            self.labelBottomFrame.pack (side = 'bottom', fill = BOTH, expand ='yes')

            #self.labelBottomFrame.pack_forget()






        def Buttons(self):


            def Back_Callback():
                self.labelFrame.pack(side="bottom", fill=BOTH, expand='yes')
                Message(self).pack_forget()


            back_button = Button(text="Back", command = Back_Callback)
            back_button.pack(side='left', fill=X, expand=True)


            def Next_Callback():
                self.labelFrame.pack_forget()
                Message(self)
                message_area.pack()
                message.pack(fill=X, expand='yes')


            next_button = Button(text="Next", command= Next_Callback)
            next_button.pack(side="right", fill=X, expand=True)



            def Message (self):

                message = tk.Label(self.labelFrame, text ="here goes text", anchor = "w")
                message.pack(fill = X, expand = 'yes')
                message_area = Text(height = 12)
                message_area.pack()










        def User (self):

            username= tk.Label(self.labelFrame, text = "Twitch username: ", anchor = "w")
            username.pack(fill = X, expand = 'yes')
            entry_username = Entry(self.labelFrame, bd = 3)
            entry_username.pack(fill = X, expand = 'yes')

        def Password(self):

            def Callback(event):
                webbrowser.open_new(("https://twitchapps.com/tmi/"))


            pass_ouath = tk.Label(self.labelFrame, text = "Authorization password: ",  fg="blue", cursor="hand2", anchor = "w")
            pass_ouath.pack(fill = X, expand ="yes")
            pass_ouath.bind("<Button-1>", Callback)
            entry_pass_ouath = Entry(self.labelFrame, bd=3)
            entry_pass_ouath.pack( fill=X, expand='yes')


        def Channel (self):

            channel_interval = tk.Label(self.labelFrame, text = "Twitch URL Channel: ", anchor = "w")
            channel_interval.pack(fill = X, expand = 'no')
            entry_channel_interval = Entry(self.labelFrame, bd=3)
            entry_channel_interval.pack( fill=X, expand='yes')
            entry_channel_interval.insert(0, "https://www.twitch.tv/example")

        class Second_Window():

            def __init__(self):

                pass

            def Text(self):
                pass



        #need to add functions to pack_forget() the widget containing the functions.







root = Tk()
app = Window(root)
root.wm_title("Twitch Chat Bot")
root.geometry('500x600')
root.mainloop()

