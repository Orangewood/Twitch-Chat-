import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
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
                        cursor="hand2", command = lambda: print(StartPage.login_list, PageOne.message_list, PageTwo.interval_list))
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





class StartPage(tk.Frame):

    login_list = []


    def __init__(self, parent, controller):

        self.counter = 0

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.username = tk.Label(self, text="Twitch username: ", anchor="w")
        self.username.pack(fill='x', expand='yes')
        self.entry_username = tk.Entry(self, bd=3)
        self.entry_username.pack(fill='x', expand='yes')








        def Callback(event):
            webbrowser.open_new(("https://twitchapps.com/tmi/"))

        self.pass_ouath = tk.Label(self, text="Generate authorization password: ", fg="blue", cursor="hand2", anchor="w")
        self.pass_ouath.pack(fill='x', expand="yes")
        self.pass_ouath.bind("<Button-1>", Callback)
        self.entry_pass_ouath = tk.Entry(self, bd=3)
        self.entry_pass_ouath.pack(fill='x', expand='yes')


        self.channel_interval = tk.Label(self, text="Twitch URL Channel: ", anchor="w")
        self.channel_interval.pack(fill='x', expand='no')
        self.entry_channel_interval = tk.Entry(self, bd=3)
        self.entry_channel_interval.pack(fill='x', expand='yes')
        self.entry_channel_interval.insert(0, "https://www.twitch.tv/example")




        self.button = tk.Button(self, text ='Next', command = lambda: [controller.show_frame(PageOne), self.get_function()], cursor="hand2")
        self.button.pack(side = 'bottom', fill = 'x', expand = True)

        self.button2 = tk.Button(self, text='test', command= lambda: self.get_function(), cursor="hand2")
        self.button2.pack(side='bottom', fill='x', expand=True)



    def get_function(self):



        one = self.entry_username.get()
        two =  self.entry_pass_ouath.get()
        three = self.entry_channel_interval.get()
        print(one, two, three)

        if self.counter == 0:

            for entry in (one, two, three):
                self.login_list.append(entry)
            self.counter +=1
        #print(self.counter)







class PageOne(tk.Frame):

    message_list = []


    def __init__(self, parent, controller):

        self.counter2 = 0

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.message_area = tk.Text(self, width = 10,  height = 10, highlightthickness = 1, fg = 'grey')
        self.message_area.pack(side='top', fill = 'both', expand = 'yes')
        self.message_area.insert('0.0', 'Insert message here, 500 characters max...')

        #make text entry box delete on command and change from grey to black
        self.message_area.bind('<FocusIn>', lambda x: self.message_area.delete('0.0', tk.END))

        self.back_button = tk.Button(self, text = 'Back', command = lambda: controller.show_frame(StartPage), cursor="hand2")
        self.back_button.pack(side='left', fill = 'x', expand = True)

        self.button = tk.Button(self, text='Next', command=lambda: [controller.show_frame(PageTwo), self.get_PageOne()], cursor="hand2")
        self.button.pack(side = 'right', fill = 'x', expand = True)



    def get_PageOne(self):

        content = self.message_area.get('1.0', tk.END)

        if self.counter2 == 0:

            self.message_list.append(content)
            self.counter2 += 1




class PageTwo(StartPage, tk.Frame):

    interval_list = []

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.interval = tk.Label(self, text = 'Alloted interval (seconds): ', anchor ='w')
        self.interval.pack(side = 'top')
        self.interval_menu = ttk.Combobox(self, values=[
                                    "3",
                                    "10",
                                    "30",
                                    "60"])
        self.interval_menu.pack(side = 'top')

        self.emote = tk.Label(self, text ='Enable random emotes?: ', anchor = 'w')
        self.emote.pack(side='top', pady = 10)
        self.yes_box = tk.Checkbutton(self, text ='Yes')
        self.yes_box.pack(fill = 'y', pady = 5 )
        self.no_box = tk.Checkbutton(self, text = "No")
        self.no_box.pack(fill = 'y')


        self.button = tk.Button(self, text='Back', command=lambda: controller.show_frame(PageOne), cursor="hand2")
        self.button.pack(side = 'bottom' , fill='x', expand=True)

    def get_PageTwo(self):

        interval_value = self.interval_menu.get()
        self.interval_list.append(interval_value)

        if self.yes_box is True:
            pass




#--------------------------Omegalul-----------------------------




class Omegalul(StartPage):

    HOST = "irc.chat.twitch.tv"

    PORT = 6667

    NICK = "{}".format(str(StartPage.login_list[0]))

    PASS = "oauth:fdgg9nwgxnaseqgnyxe8kjnefe0fmq"

    CHAN = "#druezy"

    s = socket.socket()

    s.connect((HOST, PORT))

    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))

    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))

    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

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
        a = self.s.send("PRIVMSG {} :{}\r\n".format(self.CHAN, self.Text()).encode("utf-8"))
        return a

    def Repeat(self):
        threading.Timer(3.0, b.Test, args=()).start()






app = TwitchBot()
app.geometry('400x560')
app.resizable(height = False, width = False)
app.mainloop()

y = StartPage(parent = None, controller = None)
y.get_function()
x = PageOne(parent = None, controller= None)
x.get_PageOne()

#b = Omegalul()


#b.Test()


#while True:
    #b.Repeat()
    #time.sleep(3.0)
