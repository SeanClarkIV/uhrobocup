import time

import camera
import config
import motion
from naoqi import ALProxy
import walk

proxy = config.loadProxy("ALMotion")

motion = ALProxy("ALMotion", config.IP, 9559)
memory = ALProxy("ALMemory", config.IP, 9559)
redballtracker = ALProxy("ALRedBallTracker", config.IP, 9559)

def findRedBall():
    # Set stiffnes ON
    config.StiffnessOn(proxy)

    #Make sure top camera is active
    camera.topCamera()

    # Start looking for red ball to track.
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition

    count = 0
    while redballtracker.isActive():
        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
            if redballtracker.isNewData() == False and count == 0: # Ball still lost.
                print "Looking for red ball"
                camera.topCamera()
                motion.setAngles(['HeadYaw', 'HeadPitch'], [1.0, 1.4318], 0.2)
                time.sleep(2)
                motion.setAngles(['HeadYaw', 'HeadPitch'], [-1.0, 1.4318], 0.2)
                count = 1
            elif redballtracker.isNewData() == False and count == 1:
                camera.bottomCamera()
                motion.setAngles(['HeadYaw', 'HeadPitch'], [1.0, 1.4318], 0.2)
                time.sleep(2)
                count = 0
            else: # Ball found.
                # Store found red ball positon to variable.
                foundredballposition = redballtracker.getPosition()
                if foundredballposition != initialredballposition:
                    print "Found red ball position: ", foundredballposition
                    return foundredballposition
                else:
                    print "Ball not found"
                    exit