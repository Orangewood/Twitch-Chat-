""""
Attempting to make a twitch bot that connects through IRC.
User will be able to input a message that they wish to have
fragmented with random or desired twitch emotes, that will post at
allowed intervals, according to Twitch message rates.


                                        -Orangewood 2019
"""





import random
import socket
import threading
import time
from tkinter import *
from PIL import Image, ImageTk








#--------------------------Omegalul-----------------------------

HOST = "irc.chat.twitch.tv"

PORT = 6667

NICK = #Users twitch password

PASS = #recieve pass from link

CHAN = #URL of the chat irc

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


#class Container():

    #def __init__(self):
       # pass

    #def Box(self, Text):


b = Omegalul()

b.Test()

while True:
    b.Repeat()
    time.sleep(3.0)




