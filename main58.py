#healthy programmer
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("fileio2.text","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musiconloop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_execrice=time()
    watersecs=5
    exsecs=10
    eyessecs=20
    while True:
        if time()-init_water>watersecs:
            print("water Drinking time. Enter 'drunk' to stop the alarm")
            musiconloop('water.mp3','drunk')
            init_water=time()
            log_now("drunk water at")
        if time()-init_eyes>eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm")
            musiconloop('eyes.mp3','drunk')
            init_eyes=time()
            log_now("drunk water at")
        if time()-init_execrice>exsecs:
            print("physical Activity time. Enter 'donephy' to stop the alarm")
            musiconloop('physical.mp3','drunk')
            init_execrice=time()
            log_now("physical exercise done at")
