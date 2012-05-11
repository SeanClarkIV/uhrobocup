import config
import time
import kick
import motion
from naoqi import ALProxy

def main():
    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)
    #------------------------------ send the commands -----------------------------
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    # We set the fraction of max speed
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
    time.sleep(5.5)

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


    #Kicking section
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), 0.5)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 1.0)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("one!")

    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .1)

    X = 1.0
    Y = 0.0
    Theta = 0.0
    Frequency =1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(5.5)

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


    #Kicking section

    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), 0.5)
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)

    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 1.0)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("two!")

    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .1)

    X = 1.0
    Y = 0.0
    Theta = 0.0
    Frequency =1.0 # max speed
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
    time.sleep(5.5)

    #####################
    ## End Walk
    #####################
    #TARGET VELOCITY
    X = 0.0
    Y = 0.0
    Theta = 0.0
    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)


    #Kicking section
    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), 0.5)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.10)

    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)

    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 1.0)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("three!")

    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.55)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

    proxy.angleInterpolationWithSpeed(pNames, kick.stand(), .1)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("game over!")
if __name__ == "__main__":
    main()