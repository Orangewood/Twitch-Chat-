import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import random
import socket
import threading
import time
import re


# --------------------------Omegalul-----------------------------


class Omegalul:

    HOST = "irc.chat.twitch.tv"

    PORT = 6667

    NICK = ""

    PASS = ""

    CHAN = ""

    user_message = ""

    def __init__(self):
        pass

    def startup(self):
        s = socket.socket()

        s.connect((self.HOST, self.PORT))

        s.send("PASS {}\r\n".format(self.PASS).encode("utf-8"))

        s.send("NICK {}\r\n".format(self.NICK).encode("utf-8"))

        s.send("JOIN {}\r\n".format(self.CHAN).encode("utf-8"))

        a = s.send("PRIVMSG {} :{}\r\n".format(self.CHAN, self.text()).encode("utf-8"))

        # print(self.NICK, self.PASS, self.CHAN)

        return a

    def text(self):
        x = self.user_message

        list_x = x.split()

        # List of twitch emotes for testing:

        y = [" KappaPride", " LUL", " ResidentSleeper", " 4Head", " cmonBruh", " EleGiggle", " Jebaited", " Kreygasm",
             " NotLikeThis", " PJSalt", " PogChamp", " BigBrother"]

        msg = [i + random.choice(y) for i in list_x]

        # -------------------------------Make selection of emotes or no
        # emotes------------------------------------------------- return " ".join(msg)

        return x

    def test(self):
        pass

    def repeat(self):
        threading.Timer(3.0, b.test, args=()).start()


b = Omegalul()


# ---------------------------------------GUI-------------------------------------------#

class TwitchBot(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Button(self, image=render, text="When finished, click me to begin!", compound="top", bd=0,
                        cursor="hand2", command=lambda: b.startup())
        img.image = render
        img.pack(side="top", fill='both')

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Ditionary for the frames to be called from
        self.frames = {}

        for Page in (StartPage, PageOne, PageTwo):
            frame = Page(container, self)

            self.frames[Page] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.NICK = None
        self.PASS = None
        self.CHAN = None

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.username = tk.Label(self, text="Twitch username: ", anchor="w")
        self.username.pack(fill='x', expand='yes')
        self.entry_username = tk.Entry(self, bd=3)
        self.entry_username.pack(fill='x', expand='yes')
        self.entry_username.insert(0, "darksouls3twitch")

        def callback():
            webbrowser.open_new("https://twitchapps.com/tmi/")

        self.pass_ouath = tk.Label(self, text="Generate authorization password: ", fg="blue", cursor="hand2",
                                   anchor="w")
        self.pass_ouath.pack(fill='x', expand="yes")
        self.pass_ouath.bind("<Button-1>", callback)
        self.entry_pass_ouath = tk.Entry(self, bd=3)
        self.entry_pass_ouath.pack(fill='x', expand='yes')
        self.entry_pass_ouath.insert(0, "oauth:rq0qaf3knzhbvte39ducmzuiljnjyp")
        self.channel_interval = tk.Label(self, text="Twitch URL Channel: ", anchor="w")
        self.channel_interval.pack(fill='x', expand='no')
        self.entry_channel_interval = tk.Entry(self, bd=3)
        self.entry_channel_interval.pack(fill='x', expand='yes', pady = 10)
        self.entry_channel_interval.insert(0, "https://www.twitch.tv/druezy")
        self.button = tk.Button(self, text='Next', command=lambda: [controller.show_frame(PageOne),
                                                                    self.update_all()],
                                cursor="hand2")
        self.button.pack(side='bottom', fill='x', expand=True)

    def update_nick(self, text):
        self.NICK = str(text)

    def update_pass(self, text):
        self.PASS = str("oauth:" + re.sub("[^_]*:", "", text))

    def update_chan(self, text):
        self.CHAN = str('#' + re.sub("[^_]*/", "", text))

    def update_all(self):
        self.update_nick(self.entry_username.get())
        self.update_pass(self.entry_pass_ouath.get())
        self.update_chan(self.entry_channel_interval.get())
        Omegalul.NICK = self.NICK
        Omegalul.PASS = self.PASS
        Omegalul.CHAN = self.CHAN

        # print(self.CHAN, self.NICK, self.PASS)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.message_area = tk.Text(self, width=10, height=10, highlightthickness=1, fg='grey')
        self.message_area.pack(side='top', fill='both', expand='yes')
        self.message_area.insert('0.0', 'Insert message here, 500 characters max...')

        # make text entry box delete on command and change from grey to black
        self.message_area.bind('<FocusIn>', lambda x: self.message_area.delete('0.0', tk.END))

        self.back_button = tk.Button(self, text='Back', command=lambda: controller.show_frame(StartPage),
                                     cursor="hand2")
        self.back_button.pack(side='left', fill='x', expand=True)

        self.button = tk.Button(self, text='Next', command=lambda: [controller.show_frame(PageTwo), self.get_page_one()],
                                cursor="hand2")
        self.button.pack(side='right', fill='x', expand=True)

    def get_page_one(self):
        content = self.message_area.get('1.0', tk.END)
        message = re.sub("[$_]*/n", "", content)
        user_message = message
        Omegalul.user_message = user_message


class PageTwo(StartPage, tk.Frame):
    interval_list = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.interval = tk.Label(self, text='Alloted interval (seconds): ', anchor='w')
        self.interval.pack(side='top')
        self.interval_menu = ttk.Combobox(self, values=[
            "3",
            "10",
            "30",
            "60"])
        self.interval_menu.pack(side='top')

        self.emote = tk.Label(self, text='Enable random emotes?: ', anchor='w')
        self.emote.pack(side='top', pady=10)
        self.yes_box = tk.Checkbutton(self, text='Yes')
        self.yes_box.pack(fill='y', pady=5)
        self.no_box = tk.Checkbutton(self, text="No")
        self.no_box.pack(fill='y', pady = 10)

        self.button = tk.Button(self, text='Back', command=lambda: controller.show_frame(PageOne), cursor="hand2")
        self.button.pack(side='bottom', fill='both', expand=True)

    def get_page_two(self):
        interval_value = self.interval_menu.get()
        self.interval_list.append(interval_value)

        if self.yes_box is True:
            pass


app = TwitchBot()
app.geometry('400x560')
app.resizable(height=False, width=False)
app.mainloop()

# while True:
#     b.Repeat()
#     time.sleep(3.0)