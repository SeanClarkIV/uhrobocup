import time

import camera
import config

motionProxy = config.loadProxy("ALMotion")
redballtrackerProxy = config.loadProxy("ALRedBallTracker")

def findRedBall():
    # Set stiffnes ON.
    config.StiffnessOn(motionProxy)

    # Make sure top camera is active.
    camera.topCamera()

    # Start looking for red ball to track.
    redballtrackerProxy.startTracker()
    redballtrackerProxy.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable.
    initialredballposition = redballtrackerProxy.getPosition()
    print "Initial Position: ", initialredballposition

    count = 0
    while redballtrackerProxy.isActive():
        while redballtrackerProxy.getPosition() == initialredballposition:  # Ball lost.
            if redballtrackerProxy.isNewData() == False and count == 0: # Ball still lost.
                # Pan head side to side to search for ball.
                print "Looking for red ball"
                camera.topCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [1.0, 1.4318], 0.2)
                time.sleep(2)
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-1.0, 1.4318], 0.2)
                count = 1
            elif redballtrackerProxy.isNewData() == False and count == 1:
                camera.bottomCamera()
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [1.0, 1.4318], 0.2)
                time.sleep(2)
                count = 0
            else: # Ball found.
                # Store found red ball positon to variable.
                foundredballposition = redballtrackerProxy.getPosition()
                if foundredballposition != initialredballposition:
                    print "Found red ball position: ", foundredballposition
                    return foundredballposition
                else:
                    print "Ball not found"
                    exit