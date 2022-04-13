"""
it is the music player app
"""
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from pygame import mixer


CURRENT_VOLUME = float(0.5)


def play_song():
    """ this function is used to play  new song"""
    filename = filedialog.askopenfilename(initialdir="c:/", title="select file")
    song_title = filename.split("/")
    song_title = song_title[-1]
    try:
        mixer.init()
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        SONG_TITLE_LABEL.config(fg="green", text="now playing: "+ str(song_title))
        VOLUME_LABEL.config(fg="green", text="volume: "+str(current_volume))
    except Exception as e_r:
        print(e_r)
        song_title.config(fg="red", text="error playing tyrack")


def reduce_volume():
    """this function is used to reduce volume of the current song"""
    try:
        global current_volume
        if current_volume <= 0:
            VOLUME_LABEL.config(fg="red", text="volume: muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        VOLUME_LABEL.config(fg="green", text="volume:"+str(current_volume))
    except Exception as e_r:
        print(e_r)
        SONG_TITLE_LABEL.config(fg="red", text="track hasnt been selected")


def increase_volume():
    """function to increase the volume"""
    try:
        global current_volume
        if current_volume >= 1:
            VOLUME_LABEL.config(fg="green", text="volume: max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        VOLUME_LABEL.config(fg="green", text="volume:"+ str(current_volume))
    except Exception as e_r:
        print(e_r)
        SONG_TITLE_LABEL.config(fg="red", text="song is not selected")


def pause():
    """this function to use to pause the song"""
    try:
        mixer.music.unpause()
    except Exception as e_r:
        print(e_r)
        SONG_TITLE_LABEL.config(fg="red", text="song is not selected")


def resume():
    """to resume the song"""
    try:
        mixer.music.pause()
    except Exception as e_r:
        print(e_r)
        SONG_TITLE_LABEL.config(fg="red", text="song is not selected")

MASTER = Tk()
MASTER.title("music")
Label(MASTER, text=" music player", font=("caliber", 15),
      fg="red").grid(sticky="N", row=0, padx=120)
Label(MASTER, text="select music  to play", font=("caliber", 12),
      fg="blue").grid(sticky="N", row=1)
Label(MASTER, text="volume", font=("caliber", 12),
      fg="red").grid(sticky="N", row=4)
SONG_TITLE_LABEL = Label(MASTER, font=("caliber", 12))
SONG_TITLE_LABEL.grid(sticky="N", row=3)
VOLUME_LABEL = Label(MASTER, font=("caliber", 12))
VOLUME_LABEL.grid(sticky="N", row=5)
Button(MASTER, text="select song", font=("caliber", 12),
       command=play_song).grid(row=2, sticky="N")
Button(MASTER, text="pause", font=("caliber", 12),
       command=pause).grid(row=5, sticky="E")
Button(MASTER, text="resume", font=("caliber", 12),
       command=resume).grid(row=5, sticky="W")
Button(MASTER, text="-", font=("caliber", 12), width=5,
       command=reduce_volume).grid(row=3, sticky="W")
Button(MASTER, text="+", font=("caliber", 12), width=5,
       command=increase_volume).grid(row=3, sticky="E")
MASTER.mainloop()
