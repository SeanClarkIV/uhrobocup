import config
import motion
from naoqi import ALProxy
proxy = config.loadProxy("ALMotion")
tts = ALProxy("ALTextToSpeech", config.IP, 9559)
pNames = "Body"
def poseint():
    Head     = [+0, +0]

    LeftArm  = [+40, +0, +40, +0, +0, +0]
    RightArm = [+40, +0, -40, +0, +0, +0]

    LeftLeg  = [+0, +00, +0, +0, +0, +0]
    RightLeg = [+0, -00, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand():
    Head     = [+0, +0]

    LeftArm  = [+110, +40, +20, -90, +0, +0]
    RightArm = [+110, -40, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def stand1():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +00, +0, +0]
    RightLeg = [+0, -0, -90, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def stand2():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -40, +00, +0, +0]
    RightLeg = [+0, -0, -40, +00, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def stand3():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -70, +0, +0]
    RightArm = [+110, -20, -10, +70, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, -0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand4():
    Head     = [+0, +0]

    LeftArm  = [+110, -60, +20, -00, +0, +0]
    RightArm = [+110, -20, -10, +00, +0, +0]

    LeftLeg  = [-90, +20, -90, +70, +50, +0]
    RightLeg = [-90, -20, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def stand5():
    Head     = [+0, +0]

    LeftArm  = [+119, -3.7, -14.2, -04.5, -11.3, +0]
    RightArm = [+63.5, -69.8, -33, +2.2, +104.5, +0]

    LeftLeg  = [-65.6, +45.3, -91.8, +93.4, +41.1, -3.9]
    RightLeg = [-65.6, -42.3, -91.2, +121, +20.3, +8.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand6():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -02, +11.8, +0]
    RightArm = [+17.9, -18.3, -33.5, +02.4, +70, +0]

    LeftLeg  = [-60.8, +45.3, -92.4, +80.9, +35.4, -3.2]
    RightLeg = [-60.8, -42.3, -12.6, +121, -41.1, +19.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def concrete1():
    Head     = [+0, +0]

    LeftArm  = [+91, +31.6, +24.7, -05.3, +11.9, +0]
    RightArm = [+31.9, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.6, +30.1, -18.6, +25.5, +44.3, -6]
    RightLeg = [-65.6, -19, -18.5, +121, -67.9, -4.3]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def concrete2():
    Head     = [+0, +0]

    LeftArm  = [+0, +00, +00, -0, +00, +0]
    RightArm = [+0, -00, +00, +00, +00, +0]

    LeftLeg  = [-04, +1.1, -49, +115, -58.7, -10]
    RightLeg = [-04, -0.4, -45.1, +115, -64, -1.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def concrete3():
    Head     = [+0, +0]

    LeftArm  = [+58.7, +16.3, -38, -87.4, +0, +0]
    RightArm = [+58.7, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, -0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def concrete4():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -2, +11.8, +0]
    RightArm = [+58.7, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-90, +20, -90, +70, +50, +0]
    RightLeg = [-90, -20, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def concrete5():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -02, +11.8, +0]
    RightArm = [+59.8, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-65.6, +45.3, -91.8, +93.4, +41.1, -3.9]
    RightLeg = [-65.6, -42.3, -91.2, +121, +20.3, +8.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def carpet1():
    Head     = [+0, -0]

    LeftArm  = [+91, +27, +24.7, -5.3, +0, +0]
    RightArm = [+31.9, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.6, +20.8, -15.6 , +25.5, +32.5, -14.1]
    RightLeg = [-65.6, -23.4, -19.5, +121, -68, -4.3]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def carpet2():
    Head     = [+0, -0]

    LeftArm  = [+91, +27, +24.7, -5.3, +0, +0]
    RightArm = [+115, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.3, +15.5, -19.5, +92.4, -16.3, -5.4]
    RightLeg = [-65.3, -32.8, -27.5, +121, -60, -1.4]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def carpet3():
    Head     = [+0, -0]

    LeftArm  = [+0, +00, +00, -00, +00, +0]
    RightArm = [+00, +00, +00, +00, -00, +0]

    LeftLeg  = [-4, +1.1, -45.1, +115, -64.7, -12]
    RightLeg = [-4, -1.1, -45.1, +115, -64.7, +12]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def standupbackconcrete():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand1(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand3(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand5(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand6(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, concrete1(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, concrete2(), 0.75)
    proxy.angleInterpolationWithSpeed(pNames, poseint(), 1.0)

def standupbackcarpet():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, stand(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand1(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand3(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand4(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand5(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, stand6(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, carpet1(), 0.95)
    proxy.angleInterpolationWithSpeed(pNames, carpet2(), 0.35)
    proxy.angleInterpolationWithSpeed(pNames, carpet3(), 0.35)
    proxy.angleInterpolationWithSpeed(pNames, poseint(), 0.95)

def sitdown():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, poseint(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, concrete2(), 1.0)
    proxy.angleInterpolationWithSpeed(pNames, concrete1(), 0.35)
    proxy.angleInterpolationWithSpeed(pNames, stand6(), 0.7)
    proxy.angleInterpolationWithSpeed(pNames, concrete5(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, concrete3(), 0.3)

def standfromsit():# Kick ball with right foot.
    #Turns the stiffness on.
    config.StiffnessOn(proxy)
    proxy.angleInterpolationWithSpeed(pNames, concrete3(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, concrete5(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, stand6(), 0.65)
    proxy.angleInterpolationWithSpeed(pNames, concrete1(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, concrete2(), 0.3)
    proxy.angleInterpolationWithSpeed(pNames, poseint(), 0.3)