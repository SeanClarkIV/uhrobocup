import time
import config
from naoqi import ALProxy

motion = ALProxy("ALMotion", config.IP, 9559)
redBallTracker = ALProxy("ALRedBallTracker", config.IP, 9559)

def trackRedBall():
    # Set Head Stiffness is ON and start red ball tracker
    motion.setStiffnesses("Head", 1.0)
    print "Head stiffness ON."
    redBallTracker.startTracker()
    print "Looking for red ball to track."

    # Track red ball for 60 seconds.
    time.sleep(60)
    print "Ball tracking will be stopped in 60 seconds...."

    # Stop tracker and remove head stiffness.
    redBallTracker.stopTracker()
    print "Red ball traking stoped."
    motion.setStiffnesses("Head", 0.0)
    print "Head stiffness OFF."