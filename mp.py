import tkinter
import pygame
import os
import sys
from tkinter import *
from pygame import mixer

def first():
    top=Tk()
    top.title("Musica")
    top.geometry("400x600")
    
    l1=Label(top,text="MUSICA",font=("arial",40,"bold"),bg="blue",fg="black")
    l1.pack(fill="both",expand="true")
    
    def ex():
        sys.exit()
    
    top.after(3000,second)

    top.mainloop()
   
def second():
    toop=Tk()
    toop.title("Musica")
    toop.geometry("400x600")
    
    mixer.init()
    songstatus=StringVar()
    songstatus.set("choosing")
    
    playlist=Listbox(toop,selectmode=SINGLE,bg="black",fg="blue",bd=2,font=("arial",15),width=15)
    playlist.pack(fill="both",expand="true")
    
    os.chdir(r'C:\Users\TOSIN\Music\audio')
    songs=os.listdir()
    for s in songs:
        playlist.insert(END,s)
        
    def playsong():
        currentsong=playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        songstatus.set("playing")
        mixer.music.play(currentsong)
        
    def pausesong():
        songstatus.set("pause")
        mixer.music.pause()
        
    def resumesong():
        songstatus.set("playing")
        mixer.music.unpause()
        
    def stopsong():
        songstatus.set("stopped")
        mixer.music.stop()
        
    playbtn=Button(toop,text="play",bg="blue",width=10,bd=0,fg="black",font=("arial",15),command=playsong)
    playbtn.place(x=0,y=560)
    
    pausebtn=Button(toop,text="pause",bg="blue",width=10,bd=0,fg="black",font=("arial",15),command=pausesong)
    pausebtn.place(x=100,y=560)
    
    resumebtn=Button(toop,text="resume",bg="blue",width=10,bd=0,fg="black",font=("arial",15),command=resumesong)
    resumebtn.place(x=200,y=560)
    
    stopbtn=Button(toop,text="stop",bg="blue",width=10,bd=0,fg="black",font=("arial",15),command=stopsong)
    stopbtn.place(x=300,y=560)
    toop.mainloop()

first()
#second()
