import config
import kick
import motion
from naoqi import ALProxy

proxy = config.loadProxy("ALMotion")
pNames = "Body"
tts = ALProxy("ALTextToSpeech", config.IP, 9559)

def stand():
    Head     = [ + 00, + 90]

    LeftArm  = [ + 90, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 00, -00, + 00, + 00, + 00]
    RightLeg = [ + 00, -00, -00, + 00, -00, + 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step1():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 135, + 90, + 00, + 00, + 00, + 00]
    RightArm = [ + 135, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 4, -10, + 00, + 00, + 10]
    RightLeg = [ + 00, + 4, -10, + 20, + 00, + 10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 80, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 4, -10, + 00, + 00, + 10]
    RightLeg = [ + 00, -00, -10, + 20, -30, + 00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 80, + 00, + 00, + 00, + 00]
    RightArm = [ + 180, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 4, -15, + 00, + 00, + 10]
    RightLeg = [ + 00, -00, -10, + 60, -40, + 00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 80, + 00, + 00, + 00, + 00]
    RightArm = [ + 180, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 4, -12, + 00, + 00, + 9]
    RightLeg = [ + 00, -00, -55, + 00, + 40, + 00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step5():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 135, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 135, - 90, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, -4, -10, + 20, + 00, -10]
    RightLeg = [ + 00, -4, -10, + 00, + 00, -10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step6():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -80, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 00, -10, + 20, -30, + 00]
    RightLeg = [ + 00, -04, -10, + 00, + 00, -10]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step7():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 180, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -80, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 0, -10, + 60, -30, + 00]
    RightLeg = [ + 00, -04, -15, + 00, -00, - 10]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step8():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 180, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -80, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 00, -55, + 00, + 30, + 0]
    RightLeg = [ + 00, -04, -12, + 00, + 00, -9]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

#This function kicks the ball, y being an input of what to say right before he
#kicks the ball.

#rightkick kicks with right foot
def kickRightFoot(textToSpeech):
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 0.9)
    tts.say(textToSpeech)
    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

#leftkick kicks with left foot
def kickLeftFoot(textToSpeech):
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, kick.step5(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, kick.step6(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, kick.step7(), 0.9)
    tts.say(textToSpeech)
    proxy.angleInterpolationWithSpeed(pNames, kick.step8(), 0.6)
    proxy.angleInterpolationWithSpeed(pNames, kick.step5(), 0.1)