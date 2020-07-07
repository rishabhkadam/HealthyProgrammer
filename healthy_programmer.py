from datetime import datetime
from time import time
from pygame import mixer

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        sm = input()
        if sm == stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("my rutine.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exe = time()

    waterseecs = 40*60
    eyessecs = 30*60
    exesecs = 45*60

    while True:
        if time() - init_water > waterseecs:
            print("this is a remainder of drinking water.\n To stop the music Enter 'drank' :")
            musiconloop("Closer.mp3","drank")
            init_water = time()
            log("water log : ")

        if time() - init_eyes > eyessecs:
            print("this is a remainder of eyes exercise time .\n To stop the music Enter 'doneeyes' :")
            musiconloop("Harleys-In-Hawaii.mp3","doneeyes")
            init_eyes = time()
            log("Eyes log : ")

        if time() - init_exe > exesecs:
            print("this is a remainder of Physical Exercise time.\n To stop the music Enter 'doneexe' :")
            musiconloop("Harry Potter - The Ultimate Indian Theme.mp3","doneexe")
            init_exe = time()
            log("Exercise log : ")



