import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

#import twtichbot as twitch



import random
import socket
import threading
import time




class TwitchBot(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)



        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img = tk.Button(self, image=render, text="When finished, click me to begin!", compound="top", bd=0,
                        cursor="hand2", command = lambda: print('test'))
        img.image = render
        img.pack(side="top", fill='both')

        container.pack(side = 'top', fill = 'both', expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #Ditionary for the frames to be called from
        self.frames = {}

        for Page in (StartPage, PageOne, PageTwo):

            frame = Page(container, self)

            self.frames[Page] = frame

            frame.grid(row = 0, column = 0, sticky ='nsew')



        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



    # Trying to create a method that will return the values in the different classes when called, to be returned when called later.

    def get_function(self):
        one = entry_username.get()
        two =  entry_pass_ouath.get()
        three = entry_channel_interval.get()
        print(one, two, three)


    #def fprint(self, name, password, channel):














class StartPage(tk.Frame):



    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        username = tk.Label(self, text="Twitch username: ", anchor="w")
        username.pack(fill='x', expand='yes')
        entry_username = tk.Entry(self, bd=3)
        entry_username.pack(fill='x', expand='yes')








        def Callback(event):
            webbrowser.open_new(("https://twitchapps.com/tmi/"))

        pass_ouath = tk.Label(self, text="Generate authorization password: ", fg="blue", cursor="hand2", anchor="w")
        pass_ouath.pack(fill='x', expand="yes")
        pass_ouath.bind("<Button-1>", Callback)
        entry_pass_ouath = tk.Entry(self, bd=3)
        entry_pass_ouath.pack(fill='x', expand='yes')


        channel_interval = tk.Label(self, text="Twitch URL Channel: ", anchor="w")
        channel_interval.pack(fill='x', expand='no')
        entry_channel_interval = tk.Entry(self, bd=3)
        entry_channel_interval.pack(fill='x', expand='yes')
        entry_channel_interval.insert(0, "https://www.twitch.tv/example")




        button = tk.Button(self, text ='Next', command = lambda: controller.show_frame(PageOne), cursor="hand2")
        button.pack(side = 'bottom', fill = 'x', expand = True)

        button2 = tk.Button(self, text='print', command = lambda: controller.fprint(entry_username.get()), cursor ='hand2')
        button2.pack(side ='right', fill= 'x', expand = True)

        def get_function():

            entry_username_get = entry_username.get()
            entry_pass_ouath_get = entry_pass_ouath.get()
            entry_channel_interval_get = entry_channel_interval.get()
            print(entry_username_get, entry_pass_ouath_get, entry_channel_interval_get)



class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        message_area = tk.Text(self, width = 10,  height = 10, highlightthickness = 1, fg = 'grey')
        message_area.pack(side='top', fill = 'both', expand = 'yes')
        message_area.insert('0.0', 'Insert message here, 500 characters max...')

        #make text entry box delete on command and change from grey to black
        message_area.bind('<FocusIn>', lambda x: message_area.delete('0.0', tk.END))

        back_button = tk.Button(self, text = 'Back', command = lambda: controller.show_frame(StartPage), cursor="hand2")
        back_button.pack(side='left', fill = 'x', expand = True)

        button = tk.Button(self, text='Next', command=lambda: controller.show_frame(PageTwo), cursor="hand2")
        button.pack(side = 'right', fill = 'x', expand = True)





class PageTwo(StartPage, tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        interval = tk.Label(self, text = 'Alloted interval (seconds): ', anchor ='w')
        interval.pack(side = 'top')
        interval_menu = ttk.Combobox(self, values=[
                                    "3",
                                    "10",
                                    "30",
                                    "60"])
        interval_menu.pack(side = 'top')

        emote = tk.Label(self, text ='Enable random emotes?: ', anchor = 'w')
        emote.pack(side='top', pady = 10)
        yes_box = tk.Checkbutton(self, text ='Yes')
        yes_box.pack(fill = 'y', pady = 5 )
        no_box = tk.Checkbutton(self, text = "No")
        no_box.pack(fill = 'y')


        button = tk.Button(self, text='Back', command=lambda: controller.show_frame(PageOne), cursor="hand2")
        button.pack(side = 'bottom' , fill='x', expand=True)





#--------------------------Omegalul-----------------------------

HOST = "irc.chat.twitch.tv"

PORT = 6667

NICK = "darksouls3twitch"

PASS = "oauth:fdgg9nwgxnaseqgnyxe8kjnefe0fmq"

CHAN = "#druezy"

s = socket.socket()

s.connect((HOST, PORT))

s.send("PASS {}\r\n".format(PASS).encode("utf-8"))

s.send("NICK {}\r\n".format(NICK).encode("utf-8"))

s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))


class Omegalul():

    def __init__(self):
        pass

    def Text(self):




        x = "Test message 1234"

        list_x = x.split()


        #List of twitch emotes for testing:

        y = [" KappaPride", " LUL", " ResidentSleeper", " 4Head", " cmonBruh", " EleGiggle", " Jebaited", " Kreygasm",
             " NotLikeThis", " PJSalt", " PogChamp", " BigBrother"]

        msg = [i + random.choice(y) for i in list_x]



#-------------------------------Make selection of emotes or no emotes-------------------------------------------------
        #return " ".join(msg)

        return x



    def Test(self):
        global a
        a = s.send("PRIVMSG {} :{}\r\n".format(CHAN, self.Text()).encode("utf-8"))
        return a

    def Repeat(self):
        threading.Timer(3.0, b.Test, args=()).start()






app = TwitchBot()
app.geometry('400x560')
app.resizable(height = False, width = False)
app.mainloop()
okay = TwitchBot()
okay.get_function()


b = Omegalul()

b.Test()


while True:
    b.Repeat()
    time.sleep(3.0)
