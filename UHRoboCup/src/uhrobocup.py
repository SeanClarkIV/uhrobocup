import config
import time
import kick
import walk

def main():
    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.1
    # Ask motion to do this with a blocking call

    #Kicking section

    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .6)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 1.0)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .1)
if __name__ == "__main__":
    main()