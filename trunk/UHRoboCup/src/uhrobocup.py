import config
import time
import kick
import motion

def main():
    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)

    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
    pMaxSpeedFraction = 0.1
    # Ask motion to do this with a blocking call
    # walking section
    motionProxy = config.loadProxy("ALMotion")
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

    #TARGET VELOCITY
    X = 1.0
    Y = 0.0
    Theta = 0.0
    Frequency =1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(4.0)

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


    #Kicking section

    
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.15)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 1.0)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .1)
if __name__ == "__main__":
    main()