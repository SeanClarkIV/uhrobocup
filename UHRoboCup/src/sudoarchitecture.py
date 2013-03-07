import config
import threading
#over is the variable that makes it keep playing the game until it is told games over
over =0;
statein = 0;
stopinitial=threading.Event()
def clear():
    stopready.clear()
    stopset.clear()
    stopplaying.clear()
    stoppenalized.clear()
    stopfinished.clear()
def stop(state):
    if state == "ready":
        stopready.set()
    elif state == "set":
        stopset.set()
    elif state == "playing":
        stopplaying.set()
    elif state == "penalized":
        stoppenalized.set()
    elif state == "finished":
        stopfinished.set()
class inizialize(threading.Thread):
    def run(self):

class penalized(threading.Thread):
    def run(self):
        while (not penalized.is_set()):
            if ready.is_alive():
                stop("ready")
            elif set.is_alive():
                stop("set")
            elif playing.is_alive():
                stop("playing")
            config.stiffness_off("Head")
        clear()
while over == 0:
    if statein == 0:
        state.initial()
