import config
import threading
#over is the variable that makes it keep playing the game until it is told games over
over =0;
statein = 0;
stopinitial=threading.Event()
stopready=threading.Event()
stopset=threading.Event()
stopplaying=threading.Event()
stopfinished=threading.Event()
initialon = threading.Event()
readyon = threading.Event()
seton= threading.Event()
playingon = threading.Event()
def choice():   #this is to
    print "1.) initialize 2.) ready       3.) set "
    print "4.) playing    5.) penalized   6.) finished"
    return input ("\nChoose your option(s) as list: ")
def clear():
    stopready.clear()
    stopset.clear()
    stopplaying.clear()
    stoppenalized.clear()
    stopfinished.clear()

class initial(threading.Thread):
    def run(self):
        initialon.set()
        print "running start"
        while (not stopinitial.is_set()):
            pass
        stopinitial.clear()
        initialon.clear()
        print "out of initial"
class ready(threading.Thread):
    def run(self):
        print "running ready"
        readyon.set()
        while (not stopready.is_set()):
            pass
        print "out of ready"
        readyon.clear()
class set(threading.Thread):
    def run(self):
        seton.set()
        while(not stopset.is_set()):
            pass
        print "running set"
        seton.clear()
class playing(threading.Thread):
    def run(self):
        playingon.set()
        while(not stopplaying.is_set()):
            pass
        playingon.clear()
        stopplaying.clear()
        print "running playing"
class finished(threading.Thread):
    def run(self):
        print "running finished"
class penalized(threading.Thread):
    def run(self):
        penalizedon.set()
        while (not stoppenalized.is_set()):
            if readyon.is_set():
                stop("ready")
            elif set.isAlive():
                stop("set")
            elif playing.isAlive():
                stop("playing")
            config.stiffnessOff("Head")
        penalizedon.clear()
def stop(state):
    if initialon.is_set():
        print "stopping initial"
        stopinitial.set()
    elif readyon.is_set():
        print "stopping ready"
        stopready.set()
    elif seton.is_set():
        stopset.set()
    elif playingonis_set():
        stopplaying.set()
    elif penalizedon.is_set():
        stoppenalized.set()
def sudo():
    over =0
    while over == 0:
        statein = choice()
        if statein[0] == 1:
            initial().start()
        elif statein[0] == 2:
            ready().start()
        elif statein[0] == 3:
            print "set"
        elif statein[0] == 4:
            print "playing"
        elif statein[0] == 5:
            print "penalized"
        elif statein[0] == 6:
            stop("all")
            print "finished, hopefully we won"
            #over = 1
