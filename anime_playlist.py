import tkinter as tk
import pygame,os
from pydub import AudioSegment
from tkinter import filedialog,messagebox

class AnimePlayer:

    def __init__(self,root):
        self._root = root
        self.status = tk.StringVar()
        self.track = tk.StringVar()

    def playsong(self):
        #change mp3 to ogg
        #get the active song from the ListBox
        self.track.set(self.animelist.get("active"))
        self.status.set(" |> Playing...")
        AudioSegment.from_mp3(self.animelist.get("active")).export("play.ogg", format='ogg')
        pygame.mixer.music.load("play.ogg")
        pygame.mixer.music.play(loops=0)

    def stopsong(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set(" --Playing Over")
        pygame.mixer.music.unpause()

    def main(self):
        self._root.geometry("400x460+465+115")
        self._root.resizable(False,False)
        canva = tk.Canvas(self._root,bg="black").place(x=-10,y=-10,width=450,height=450)
        box = tk.Listbox(self._root,bg="grey",bd=5).place(x=0,y=368,width=400,height=90)

        #control buttons and images
        play_img = tk.PhotoImage(file="play.png")
        pause_img = tk.PhotoImage(file="pause.png")
        stop_img = tk.PhotoImage(file="stop.png")
        unpause_img = tk.PhotoImage(file="unpause.png")

        #use playsong, pausesong as the trigger functions for the active songs
        play_button = tk.Button(box,image=play_img,command=self.playsong,bd=5,bg="blue")
        play_button.place(x=110,y=375,width=80,height=75)
        pause_button = tk.Button(box,image=pause_img,command=self.pausesong,bd=5,bg="blue")
        pause_button.place(x=10,y=375,width=80,height=75)
        stop_button = tk.Button(box,image=stop_img,command=self.stopsong,bd=5,bg="blue")
        stop_button.place(x=210,y=375,width=80,height=75)
        unpause_button = tk.Button(box,image=unpause_img,command=self.unpausesong,bg="blue",bd=5)
        unpause_button.place(x=310,y=375,width=80,height=75)
        #controls config ends here

        #the main frame where all the song will be displayer
        anime_frame = tk.LabelFrame(self._root,text="Anime Playlist",font=("arial",15,"bold"),bg="black",fg="blue",bd=5)
        anime_frame.place(x=0,y=20,width=400,height=250)

        #this is used to display the status while song is active, active: when user clicks on any song
        statusframe = tk.LabelFrame(self._root,text="Now Playing",font=("arial",15,"bold"),bg="black",fg="blue",bd=5)
        statusframe.place(x=0,y=270,width=400,height=95)

        song = tk.Label(statusframe,textvariable=self.track,font=("arial",14,"bold"),bg="black",fg="blue")
        song.pack()

        status = tk.Label(statusframe,textvariable=self.status,font=("arial", 15,"bold"),bg="black",fg="blue")
        status.pack()

        #configure the scroll-bar which becomes easy to choose a song
        scroll_bar = tk.Scrollbar(anime_frame,orient="vertical")
        self.animelist = tk.Listbox(anime_frame,yscrollcommand=scroll_bar.set,selectbackground="white",font=("arial",12,"bold"),bg="grey",fg="navyblue",bd=5)
        scroll_bar.pack(side="right",fill="y")
        scroll_bar.config(command=self.animelist.yview)
        self.animelist.pack(fill="both")

        #change the directory where all the openings are saved
        os.chdir("AnimeTrack")
        anime_songs = os.listdir() #store all songs in a list
        anime_songs.sort()
        for songs in anime_songs[:-1]:
            #add all songs in the ListBox
            self.animelist.insert(tk.END,songs)
        self._root.mainloop()

if __name__ == '__main__':
    #create a root window and initialize pygame mixer
    root = tk.Tk()
    root.title("Anime Player")
    pygame.init()
    pygame.mixer.init()
    anime = AnimePlayer(root)
    FPS=30
    fpsClock = pygame.time.Clock()
    anime.main()
    fpsClock.tick(FPS)
