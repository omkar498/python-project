
from signal import pause
from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog


current_volume= float(0.5)


def play_song():
    filename = filedialog.askopenfilename(initialdir="c:/",title="select file")
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green",text="now playing: "+ str(song_title))
        volume_label.config(fg="green",text="volume: "+str(current_volume))

    except Exception as e:
        print(e)
        song_title.config(fg="red", text="error playing tyrack")   

def reduce_volume():
    try:
        global current_volume
        if current_volume <=0:
            volume_label.config(fg="red",text="volume: muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text="volume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="track hasnt been selected")        

def increase_volume():
    try:
        global current_volume
        if current_volume >=1:
            volume_label.config(fg="green",text="volume: max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green",text="volume:"+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="song is not selected")        

def pause():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="song is not selected")    

def resume():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="song is not selected")    

master = Tk()
master.title("music")

Label(master,text=" music player",font=("caliber",15),fg="red").grid(sticky="n",row=0,padx=120)
Label(master,text="select music  to play",font=("caliber",12),fg="blue").grid(sticky="n",row=1)
Label(master,text="volume",font=("caliber",12),fg="red").grid(sticky="n",row=4)
song_title_label = Label(master,font=("caliber",12))
song_title_label.grid(stick = "n",row=3)
volume_label = Label(master,font=("caliber",12))
volume_label.grid(sticky= "n",row=5)


Button(master, text="select song",font=("caliber",12),command=play_song).grid(row=2,sticky="n")
Button(master, text="pause",font=("caliber",12),command=pause).grid(row=5,sticky="e")
Button(master, text="resume",font=("caliber",12),command=resume).grid(row=5,sticky="w")
Button(master, text="-",font=("caliber",12),width=5,command=reduce_volume).grid(row=3,sticky="w")
Button(master, text="+",font=("caliber",12),width=5,command=increase_volume).grid(row=3,sticky="e")
master.mainloop() 
