#-*- coding: iso-8859-15 -*-

''' PoseInit: Small example to make Nao go to an initial position. '''

import config
import time
import kick

def main():
    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)

    # Get the Robot Configuration
    robotConfig = proxy.getRobotConfig()
    robotName = ""

    # Convert to radians
    

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.1
    pMaxSpeedFraction2 = 1.0
    # Ask motion to do this with a blocking call
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), pMaxSpeedFraction)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), .1)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), .05)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), pMaxSpeedFraction)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), pMaxSpeedFraction2)
    time.sleep(4)
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), pMaxSpeedFraction)


if __name__ == "__main__":
    main()