import config
import motion
from naoqi import ALProxy

proxy = config.loadProxy("ALMotion")
pNames = "Body"

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
    RightArm = [ + 135, - 00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, -00, -10, + 00, + 00, +8]
    RightLeg = [ + 00, -00, -10, + 00, + 00, +8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 80, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 04, -10, + 00, -00, +8]
    RightLeg = [ + 00, +04, -10, + 00, - 10, +8]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 80, + 00, + 00, + 00, + 00]
    RightArm = [ + 180, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 04, -15, + 00, -00, + 10]
    RightLeg = [ + 00, +00, -10, + 60, -30, + 00]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 50, + 00, + 00, + 00, + 00]
    RightArm = [ + 180, -00, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 04, -12, + 00, + 00, + 9]
    RightLeg = [ + 00, +00, -40, + 00, + 10, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step5():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 135, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 135, - 90, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, -00, -10, + 00, + 00, -8]
    RightLeg = [ + 00, -00, -10, + 00, + 00, -8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step6():
    Head     = [ + 00, + 00]

    LeftArm  = [ + 90, + 00, + 00, + 00, + 00, + 00]
    RightArm = [ + 90, -80, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, - 04, -10, + 00, -10, -8]
    RightLeg = [ + 00, -04, -10, + 00, + 00, -8]
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
    RightArm = [ + 90, -50, -00, -00, + 00, + 00]

    LeftLeg  = [ + 00, + 00, -40, + 00, + 10, + 0]
    RightLeg = [ + 00, -04, -12, + 00, + 00, -9]
    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

#This function kicks the ball, y being an input of what to say right before he
#kicks the ball.

#rightkick kicks with right foot
def kickRightFoot():
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.17)
    proxy.angleInterpolationWithSpeed(pNames, step2(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step3(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 0.2)

#leftkick kicks with left foot
def kickLeftFoot():
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 0.17)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 0.5)
    proxy.angleInterpolationWithSpeed(pNames, step7(), 0.4)
    proxy.angleInterpolationWithSpeed(pNames, step8(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 0.2)