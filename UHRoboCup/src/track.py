import walk
import random
import time

import config
from naoqi import ALProxy

motion = ALProxy("ALMotion", config.IP, 9559)
redBallTracker = ALProxy("ALRedBallTracker", config.IP, 9559)

def trackRedBall():
    # Set Head Stiffness ON.
    motion.setStiffnesses("Head", 1.0)
    print "Head stiffness ON."

    # Start looking for red ball to track.
    redBallTracker.startTracker()
    if redBallTracker.isActive() == True:
        print "Looking for red ball to track."


    stop = 0
    while (stop == 0):
        count = 0
        print count, "  ", redBallTracker.getPosition()
        count = count + 1
        stop = input ("To stop press 1: ")

    print "done"

    # Track red ball for 60 seconds.
#    print "Ball tracking will be stopped in 60 seconds...."
#    time.sleep(60)

    # Stop tracker and remove head stiffness.
    redBallTracker.stopTracker()
    print "Red ball traking stoped."

    # Set Head Stiffness OFF.
    motion.setStiffnesses("Head", 0.0)
    print "Head stiffness OFF."

def findRedBall():
    # Set Head Stiffness ON.
    motion.setStiffnesses("Head", 1.0)
    print "Head stiffness ON."

    redBallTracker.startTracker()
    redballposition = redBallTracker.getPosition()

    count = 0
    while redballposition == [0,0,0]:
        # Move head to random position (Jerky Head).
        motion.setAngles("HeadYaw", random.uniform(-1.0, 1.0), 0.6)
        motion.setAngles("HeadPitch", random.uniform(-0.5, 0.5), 0.6)
        redballposition = redBallTracker.getPosition()
        print count, redballposition
        if count == 50:
            walk.turnleft()
            count = 0
        else:
            count = count + 1

    print "found it"
