import time
import kick
import camera
import config
import walk
import threading
motionProxy = config.load_proxy("ALMotion")

redballtracker = config.load_proxy("ALRedBallTracker")
def find_red_ball(trackstop=threading.Event()): #added the trackstop so that if you want to use this
                                                #in a thread you can stop it. 
    #This code finds the red ball.
    # Set stiffnes ON
    config.stiffness_on()

    #Make sure top camera is active
    camera.top_camera()
    # Start looking for red ball to track.
    redballtracker.stopTracker()
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition
    count = 0
    times = 0
    headpitchangle = 1.433
    while redballtracker.getPosition() == initialredballposition:  # Ball lost.
        if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
            print "Looking for red ball"
            motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
            time.sleep(3)
            count = 1
            times += 1
        elif redballtracker.isNewData() == False and count == 1:
            motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
            time.sleep(3)
            count = 0
            times += 1
        # the next if condition is to look up slightly if he can't find the ball and then when it looks up 3 times
        # it decides turns left and starts all over again.
        if times > 1:
            number = float(times)
            if number % 2 == 1:
                if headpitchangle < 0:
                    headpitchangle = 1.433
                    walk.ultimate_walk_to(0, 0, 2)
                elif headpitchangle > .5:
                    headpitchangle = .2
                else:
                    headpitchangle = headpitchangle - 0.2
                print headpitchangle
            else:
                pass
        if trackstop.is_set():
            initialredballposition=[-1000,-1000,-1000]
            print "stopped at tracking"
    print "found red ball"
    redballposition=redballtracker.getPosition()
    redballtracker.stopTracker()
    return redballposition
def find_red_ball_and_kick(option):
    # Set stiffnes ON
    config.stiffness_on()

    #Make sure top camera is active
    camera.top_camera()

    # Start looking for red ball to track.
    redballtracker.startTracker()
    redballtracker.setWholeBodyOn(True)
    print "Tracking red ball"

    #Store initial red ball positon to variable
    initialredballposition = redballtracker.getPosition()
    print "Initial Position: ", initialredballposition
    cameras = 0 #Top camera
    count = 0
    counter = 0 #Used for Redballposition
    times = 0
    headpitchangle = 1.433
    while redballtracker.isActive(): # runs while loop as long as redballtracker is active
        while redballtracker.getPosition() == initialredballposition:  # Ball lost.
            if redballtracker.isNewData() == False and count == 0: # Ball still lost.true if a new Red Ball was detected since the last getPosition().
                print "Looking for red ball"
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [-0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 1
                cameras = 0 # top camera
                times += 1
            elif redballtracker.isNewData() == False and count == 1:
                motionProxy.setAngles(['HeadYaw', 'HeadPitch'], [0.5, headpitchangle], 0.07)
                time.sleep(3)
                count = 0
                cameras = 1 # bottom camera
                times += 1
            # the next if condition is to look up slightly if he can't find the ball and then when it looks up 3 times
            # it decides turns left and starts all over again.
            if times > 1:
                number = float(times)
                if number % 2 == 1:
                    if headpitchangle < 0:
                        headpitchangle = 1.433
                        walk.ultimate_walk_to(0, 0, 2)
                    elif headpitchangle > .5:
                        headpitchangle = .2
                    else:
                        headpitchangle = headpitchangle - 0.2
                    print headpitchangle
                else:
                    pass
        # Ball found.
        # Store found red ball positon to variable.
        #foundredballposition and foundredballposition 2 are to make sure there are no
        #random jumps so the robot doesn't randomly pick a different thing to go to.
        if counter == 0:
            foundredballposition2 = redballtracker.getPosition()
        walk.ewalk()
        foundredballposition = foundredballposition2
        foundredballposition2 = redballtracker.getPosition()
        print "Found red ball position: ", foundredballposition2
        counter = 1
        if redballtracker.isNewData() == False and count > 1000 or foundredballposition[0]/foundredballposition2[0] > 2: #means it lost the ball
            walk.stop()                                                                                                  #start fresh
            initialredballposition = redballtracker.getPosition()
            count = 0
            counter = 0
        elif cameras == 0 and foundredballposition2[0] < .57 and foundredballposition[0]/foundredballposition2[0] <= 2:
            walk.stop()
            print "I made it"
            walk.ultimate_walk_to(0.28, foundredballposition2[1]/1.5, foundredballposition2[2]/2.1)
            redballtracker.stopTracker()
            print "I made it"
            if option == 1:
                walk.ultimate_walk_to(0, -.01, 0)
                kick.kick_left_foot()
            elif option == 2:
                walk.ultimate_walk_to(0, -.075, 0)
                kick.kick_left_foot()
            elif option == 3:
                walk.ultimate_walk_to(0, -.14, 0)
                kick.kick_left_foot()
            if option == 4:
                walk.ultimate_walk_to(0, .01, 0)
                kick.kick_right_foot()
            elif option == 5:
                walk.ultimate_walk_to(0, .075, 0)
                kick.kick_right_foot()
            elif option == 6:
                walk.ultimate_walk_to(0, .14, 0)
                kick.kick_right_foot()
            config.pose_init()
        elif cameras == 1 and foundredballposition2[0] < .4 and foundredballposition[0]/foundredballposition2[0] <= 2:
            walk.stop()
            print "I made it, bottom camera"
            kick.kick_right_foot()
            redballtracker.stopTracker()
            config.pose_init()
        elif redballtracker.isNewData() == True and foundredballposition2[0] >= .4:
            count = 2

        elif redballtracker.isNewData() == False and count <= 1000:
            count += 1
            print count

def stop_tracker():
    redballtracker.stopTracker()