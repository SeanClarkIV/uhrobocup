import config
import motion
from naoqi import ALProxy
proxy = config.loadProxy("ALMotion")
tts = ALProxy("ALTextToSpeech", config.IP, 9559)
pNames = "Body"
def stand():
    Head     = [+0, +0]

    LeftArm  = [+40, +0, +40, +0, +0, +0]
    RightArm = [+40, +0, -40, +0, +0, +0]

    LeftLeg  = [+0, +00, +0, +0, +0, +0]
    RightLeg = [+0, -00, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step():
    Head     = [+0, +0]

    LeftArm  = [+110, +40, +20, -90, +0, +0]
    RightArm = [+110, -40, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step1():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step2():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -40, +00, +0, +0]
    RightLeg = [+0, -0, -40, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step3():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -70, +0, +0]
    RightArm = [+110, -20, -10, +70, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, -0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step4():
    Head     = [+0, +0]

    LeftArm  = [+110, -60, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, +20, -90, +70, +50, +0]
    RightLeg = [-90, -20, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step5():
    Head     = [+0, +0]

    LeftArm  = [+119, -3.7, -14.2, -04.5, -11.3, +0]
    RightArm = [+63.5, -69.8, -33, +2.2, +104.5, +0]

    LeftLeg  = [-65.6, +45.3, -91.8, +93.4, +41.1, -3.9]
    RightLeg = [-65.6, -42.3, -91.2, +121, +20.3, +8.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step6():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -02, +11.8, +0]
    RightArm = [+17.9, -18.3, -33.5, +02.4, +104.5, +0]

    LeftLeg  = [-60.8, +45.3, -92.4, +80.9, +35.4, -3.2]
    RightLeg = [-60.8, -42.3, -12.6, +121, -41.1, +19.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step7():
    Head     = [+0, +0]

    LeftArm  = [+91, +31.6, +24.7, -05.3, +11.9, +0]
    RightArm = [+31.9, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.6, +30.1, -18.6, +25.5, +44.3, -6]
    RightLeg = [-65.6, -19, -18.5, +121, -67.9, -4.3]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step8():
    Head     = [+0, -90]

    LeftArm  = [-90, -90, -90, -90, +0, +0]
    RightArm = [-90, +90, +90, +90, +0, +0]

    LeftLeg  = [-90, +90, -40, +00, -10, -00]
    RightLeg = [-90, -90, -40, +00, -10, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step9():
    Head     = [+0, -90]

    LeftArm  = [+40, -20, -00, -00, +00, +0]
    RightArm = [+40, +20, +00, +00, +00, +0]

    LeftLeg  = [-90, +90, -180, +00, +90, -10]
    RightLeg = [-90, -90, -180, +00, +90, +10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step10():
    Head     = [+0, -90]

    LeftArm  = [+00, +90, -00, -0, +0, +0]
    RightArm = [+00, -90, +00, +0, +0, +0]

    LeftLeg  = [-90, +90, -100, +0, +90, -10]
    RightLeg = [-90, -90, -100, +0, +90, +10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step11():
    Head     = [+0, -90]

    LeftArm  = [+40, +90, +0, -00, +0, +0]
    RightArm = [+40, -90, -0, +00, +0, +0]

    LeftLeg  = [-90, +90, -100, +20, +90, -10]
    RightLeg = [-90, -90, -100, +20, +90, +10]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step12():
    Head     = [+0, -90]

    LeftArm  = [-45, +0, +0, -00, +0, +0]
    RightArm = [-45, -0, -0, +00, +0, +0]

    LeftLeg  = [-0, +0, -100, +0, +0, -00]
    RightLeg = [-0, -0, -100, +0, +0, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step13():
    Head     = [+0, -90]

    LeftArm  = [-90, +00, +0, -00, +0, +0]
    RightArm = [-90, +00, -0, +00, +0, +0]

    LeftLeg  = [-0, +0, -00, +0, -0, -00]
    RightLeg = [-0, -0, -00, +0, -0, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step14():
    Head     = [+0, +0]

    LeftArm  = [+0, +00, +00, -0, +00, +0]
    RightArm = [+0, -00, +00, +00, +00, +0]

    LeftLeg  = [-04, +1.1, -49, +115, -58.7, -10]
    RightLeg = [-04, -0.4, -45.1, +115, -64, -1.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def step15():
    Head     = [+0, +38]

    LeftArm  = [-0, +00, +0, -00, +0, +0]
    RightArm = [-0, +00, -0, +00, +0, +0]

    LeftLeg  = [-0, +0, -60, +0, +90, -00]
    RightLeg = [-0, -0, -60, +0, +90, +00]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def standuponback():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step1(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step3(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step5(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step6(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step7(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, step14(), 0.75)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 1.0)
def standuponfront():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, step14(), .1)
    tts.say("initial")
    proxy.angleInterpolationWithSpeed(pNames, step15(), 1)