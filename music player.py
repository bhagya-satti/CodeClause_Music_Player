import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import pygame 
from pygame import mixer

class MusicPlayer:
    def __init__(self,root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("700x400")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root,text="Song Track",font=("Doctrine",15,"bold"),bg="black",fg="White")
        trackframe.place(x=0,y=0,width=500,height=400)

        songtrack = Label(trackframe,textvariable=self.track,width=19,font=("Doctrine",24,"bold"),bg="#2c2d32",fg="white").grid(row=0,column=0,padx=85,pady=10)
        
        buttonframe = LabelFrame(self.root,text="Control Panel",font=("Doctrine",15,"bold"),bg="#2c2d32",fg="white")
        buttonframe.place(x=70,y=100,width=400,height=280)

        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=8,height=1,font=("Doctrine",16,"bold"),fg="white",bg="#fe2c42").grid(row=0,column=0,padx=20,pady=5)

        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("Doctrine",16,"bold"),fg="white",bg="#fe2c42").grid(row=0,column=2,padx=50,pady=50)

        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=8,height=1,font=("Doctrine",16,"bold"),fg="white",bg="#fe2c42").grid(row=3,column=0,padx=40,pady=5)

        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=8,height=1,font=("Doctrine",16,"bold"),fg="white",bg="#fe2c42").grid(row=3,column=2,padx=20,pady=5)

        songsframe = LabelFrame(self.root,text="Playlist",font=("Doctrine",15,"bold"),bg="#2c2d32",fg="white")
        songsframe.place(x=500,y=0,width=400,height=700)
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#fe2c42",selectmode=SINGLE,font=("Doctrine",14,"bold"),bg="#2c2d32",fg="white")
        scrol_y.pack(side=RIGHT)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        os.chdir(r"C:\Users\bhagy\music player\Music")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END,track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set(".........")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("|>")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("||>")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set("........")
        pygame.mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()