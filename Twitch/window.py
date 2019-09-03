import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser







class TwitchBot(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img = tk.Button(self, image=render, text="When finished, click me to begin!", compound="top", bd=0,
                        cursor="hand2")
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

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


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



class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)


        message_area = tk.Text(self, width = 10,  height = 10, highlightthickness = 1, fg = 'grey')
        message_area.pack(side='top', fill = 'both', expand = 'yes')
        message_area.insert('0.0', 'Insert message here, 500 characters max...')

        #make text entry box delete on command and change from grey to black
        message_area.bind('<FocusIn>', lambda x: message_area.delete('0.0', tk.END))

        back_button = tk.Button(self, text = 'Back', command = lambda: controller.show_frame(StartPage), cursor="hand2")
        back_button.pack(side='left', fill = 'x', expand = True)

        button = tk.Button(self, text='Next', command=lambda: controller.show_frame(PageTwo), cursor="hand2")
        button.pack(side = 'right', fill = 'x', expand = True)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

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


app = TwitchBot()
app.geometry('400x560')
app.resizable(height = False, width = False)
app.mainloop()
