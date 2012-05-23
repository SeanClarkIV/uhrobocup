import config
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

    LeftArm  = [ +90, +10, - 90, - 00, -90, + 05]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [ + 00, + 00]

    LeftArm  = [ +90, +10, - 90, - 00, -90, + 05]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step3():
    Head     = [ + 00, + 00]

    LeftArm  = [ +00, +10, - 90, - 00, -90, + 35]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step4():
    Head     = [ + 00, + 00]

    LeftArm  = [ +90, +10, - 90, - 00, -90, + 10]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step5():
    Head     = [ + 00, + 00]

    LeftArm  = [ +90, +90, - 90, - 00, -90, + 10]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
#This function kicks the ball, y being an input of what to say right before he
#kicks the ball.
def step6():
    Head     = [ + 00, + 00]

    LeftArm  = [ +00, +10, - 90, - 00, -90, + 05]
    RightArm = [ +120, +00, -00, +00, +90, + 00]

    LeftLeg  = [ + 00, + 00, -90, + 120, - 40, - 00]
    RightLeg = [ + 00, + 00, -90, + 120, - 40, - 00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

#rightkick kicks with right foot
def throwstrait():
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 0.1)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step2(), 0.05)
    proxy.angleInterpolationWithSpeed(pNames, step3(), 1.0)


#leftkick kicks with left foot
def throwright():
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 0.01)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 1.0)
