import goalie
import config
import dive
import math
import time
import camera
motionProxy = config.loadProxy("ALMotion")
pNames = "Body"
timeProxy = config.loadProxy("DCM")
redballtracker = config.loadProxy("ALRedBallTracker")
def goaliepose():
    config.StiffnessOn()
    motionProxy.angleInterpolationWithSpeed(pNames, dive.dive1(), .5)
def goalie():
    goaliepose()
    timer = timeProxy.getTime(0)
    print time
    initialredballposition = redballtracker.getPosition()
    camera.topCamera()
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    counter = 0
    count = 0
    while True:

        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
                if redballtracker.isNewData() == False and count == 0: # Ball still lost.
                    print "Looking for red ball"
                    camera.topCamera()
                    motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, 1.433], 0.07)
                    time.sleep(2)
                    count = 1
                elif redballtracker.isNewData() == False and count == 1: #Ball still lost.
                    camera.bottomCamera()
                    motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, 1.433], 0.07)
                    time.sleep(2)
                    count = 0
        if counter == 0:
            redballposition = redballtracker.getPosition()
            counter == 1
            timer = timeProxy.getTime(0)
        redballposition2 = redballposition
        print "redballposition2 :",   redballposition2, "timer:", timer
        while count < 100:
            redballtracker.startTracker()
            redballtracker.setWholeBodyOn(True)
            redballposition2 = redballposition
            redballposition = redballtracker.getPosition()
            print "redballposition:", redballposition
            timer = timeProxy.getTime(0)
            timer2 = timeProxy.getTime(0)
            distance = math.sqrt(math.pow(redballposition[0],2) + math.pow(redballposition[1],2) + math.pow(redballposition[2],2))
            print "distance:" , distance
            print "timer2:" , timer2, "timer:" , timer
            velocity = math.sqrt(math.pow((redballposition[0] - redballposition2[0]), 2) + math.pow((redballposition[1] - redballposition2[1]),2) + math.pow((redballposition[2] - redballposition2[2]),2))/ (timer2 - timer)
            print "velocity:" , velocity, "count" , count
            if velocity == 0:
                count += 1
            elif velocity >= .05 and redballposition[1] > .1 and redballposition[0] < 1:
                redballtracker.stopTracker()
                dive.dive()
                motionProxy.angleInterpolationWithSpeed(pNames, dive.dive1(), .3)
                redballtracker.startTracker()
                count = 100
            elif velocity >= .02 and redballposition[0] < .4 and redballposition[1] > .09:
                redballtracker.stopTracker()
                dive.dive()
                motionProxy.angleInterpolationWithSpeed(pNames, dive.dive1(), .3)
                redballtracker.startTracker()
                count = 100
            time.sleep(1)


        initialposition= redballtracker.getPosition()
        count = 0