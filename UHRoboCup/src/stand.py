import config
import motion
import stand
import fallcheck

motionProxy = config.load_proxy("ALMotion")

def pose_int():
    Head     = [+0, +0]

    LeftArm  = [+40, +0, +40, +0, +0, +0]
    RightArm = [+40, +0, -40, +0, +0, +0]

    LeftLeg  = [+0, +0, +0, +0, +0, +0]
    RightLeg = [+0, +0, +0, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def sit_1():
    Head     = [+0, +0]

    LeftArm  = [+91, +31.6, +24.7, -05.3, +11.9, +0]
    RightArm = [+31.9, +15.2, -74.6, -68, +0, +0]

    LeftLeg  = [-65.6, +30.1, -18.6, +25.5, +44.3, -6]
    RightLeg = [-65.6, -19, -18.5, +121, -67.9, -4.3]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def sit_2():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +0, +0, +0, +0]
    RightArm = [+0, +0, +0, +0, +0, +0]

    LeftLeg  = [-04, +1.1, -49, +115, -58.7, -10]
    RightLeg = [-04, +0.4, -45.1, +115, -64, -1.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def sit_3():
    Head     = [+0, +0]

    LeftArm  = [+58.7, +16.3, -38, -87.4, +0, +0]
    RightArm = [+58.7, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, +0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def sit_4():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -2, +11.8, +0]
    RightArm = [+59.8, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-65.6, +45.3, -91.8, +93.4, +41.1, -3.9]
    RightLeg = [-65.6, -45.3, -91.8, +121, +20.3, +8.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def sit_5():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -2, +11.8, +0]
    RightArm = [+59.8, -16.3, +38, +87.4, +0, +0]

    LeftLeg  = [-20, +45.3, -91.8, +0, -30, +0]
    RightLeg = [-20, -45.3, -91.8, +0, -30, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand():
    Head     = [+0, +0]

    LeftArm  = [+110, +40, +20, -90, +0, +0]
    RightArm = [+110, -40, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +0, +0, +0]
    RightLeg = [+0, +0, -90, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_1():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -90, +0, +0, +0]
    RightLeg = [+0, +0, -90, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_2():
    Head     = [+0, +0]

    LeftArm  = [+120, +30, +20, -90, +0, +0]
    RightArm = [+120, -30, -20, +90, +0, +0]

    LeftLeg  = [+0, +0, -40, +0, +0, +0]
    RightLeg = [+0, +0, -40, +0, +0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_3():
    Head     = [+0, +0]

    LeftArm  = [+110, +20, +20, -70, +0, +0]
    RightArm = [+110, -20, -10, +70, +0, +0]

    LeftLeg  = [-50, +0, -90, +70, +80, +0]
    RightLeg = [-50, +0, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_4():
    Head     = [+0, +0]

    LeftArm  = [+110, -60, +20, +0, +0, +0]
    RightArm = [+110, -20, -10, +0, +0, +0]

    LeftLeg  = [-90, +20, -90, +70, +50, +0]
    RightLeg = [-90, -20, -90, +70, +80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_5():
    Head     = [+0, +0]

    LeftArm  = [+119, -3.7, -14.2, -4.5, -11.3, +0]
    RightArm = [+63.5, -69.8, -33, +2.2, +104.5, +0]

    LeftLeg  = [-65.6, +45.3, -91.8, +93.4, +41.1, -3.9]
    RightLeg = [-65.6, -42.3, -91.2, +121, +20.3, +8.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_6():
    Head     = [+0, +0]

    LeftArm  = [+119.5, +30.3, -5.6, -2, +11.8, +0]
    RightArm = [+17.9, -18.3, -33.5, +2.4, +0, +0]

    LeftLeg  = [-60.8, +45.3, -92.4, +80.9, +35.4, -3.2]
    RightLeg = [-60.8, -42.3, -12.6, +121, -41.1, +19.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_7():
    Head     = [+0, +0]

    LeftArm  = [+91, +27, +24.7, -5.3, +0, +0]
    RightArm = [+31.9, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.6, +20.8, -15.6 , +25.5, +32.5, -14.1]
    RightLeg = [-65.6, -23.4, -19.5, +121, -68, -4.3]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_8():
    Head     = [+0, +0]

    LeftArm  = [+91, +27, +24.7, -5.3, +0, +0]
    RightArm = [+115, +15.2, -74.6, -68, -89.7, +0]

    LeftLeg  = [-65.3, +15.5, -19.5, +92.4, -16.3, -5.4]
    RightLeg = [-65.3, -32.8, -27.5, +121, -60, -1.4]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_9():
    Head     = [+0, +0]

    LeftArm  = [+0, +0, +0, +0, +0, +0]
    RightArm = [+0, +0, +0, +0, +0, +0]

    LeftLeg  = [-4, +1.1, -38.1, +115, -64.5, -12]
    RightLeg = [-4, -1.1, -38.1, +115, -64.5, +12]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front():
    Head     = [+2.2, +25]

    LeftArm  = [+0, +90, +0, +0, +0, +0]
    RightArm = [+0, -90, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, +10, +10, -80, +0]
    RightLeg = [+0, +0, +10, +10, -80, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front_1():
    Head     = [+2.2, +25]

    LeftArm  = [-90, +0, +0, +0, +0, +0]
    RightArm = [-90, +0, +0, +0, +0, +0]

    LeftLeg  = [+0, +0, +10, +10, -17.2, +0]
    RightLeg = [+0, +0, +10, +10, -17.0, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front_2():
    Head     = [+2.2, +25]

    LeftArm  = [-90, +0, +0, +0, +0, +0]
    RightArm = [-90, +0, +0, +0, +0, +0]

    LeftLeg  = [-65.6, +42.3, +5.1, +8.9, -6.0, +11.8]
    RightLeg = [-65.6, -42.3, +5.1, +8.9, -6.0, -11.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front_3():
    Head     = [+2.2, +25]

    LeftArm  = [-90, +0, +0, +0, +0, +0]
    RightArm = [-90, +0, +0, +0, +0, +0]

    LeftLeg  = [-65.6, +42.3, -91, +8.9, -6.0, +11.8]
    RightLeg = [-65.6, -42.3, -91, +8.9, -6.0, -11.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front_4():
    Head     = [+2.2, +25]

    LeftArm  = [-19.9, +0, +0, +0, +104.5, +0]
    RightArm = [-19.9, +0, +0, +0, -104.5, +0]

    LeftLeg  = [-65.6, -19.3, -91, +8.9, -6.0, +11.8]
    RightLeg = [-65.6, +19.3, -91, +8.9, -6.0, -11.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def step_up_front_5():
    Head     = [+2.2, +25]

    LeftArm  = [+0, +0, +0, +0, +104.5, +0]
    RightArm = [+0, +0, +0, +0, -104.5, +0]

    LeftLeg  = [-65.6, -19.3, -59.9, +8.9, -6.0, +11.8]
    RightLeg = [-65.6, +19.3, -59.9, +8.9, -6.0, -11.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles

def stand_up():  # Stand up from its back.
    config.stiffness_on()   # Turns the stiffness on.
    motionProxy.angleInterpolationWithSpeed("Body", stand(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", stand_1(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", stand_2(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", stand_3(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_4(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_5(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_6(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_7(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_8(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", stand_9(), 0.8)
    motionProxy.angleInterpolationWithSpeed("Body", pose_int(), 0.8)
    fallcheck.check_fall()
    print "standing back"

def stand_up_on_front(): # Stands up from its belly.
    config.stiffness_on()   # Turns the stiffness on.
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front(), 0.5)
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front_1(), 0.5)
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front_2(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front_3(), 0.1)
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front_4(), 0.1)
    motionProxy.angleInterpolationWithSpeed("Body", step_up_front_5(), 0.1)
    fallcheck.check_fall()
    stand_from_sit()
    print "standing front"

def sit_down():  # Sits down from standup position.
    config.stiffness_on()   # Turns the stiffness on.
    motionProxy.angleInterpolationWithSpeed("Body", pose_int(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", sit_2(), 1.0)
    motionProxy.angleInterpolationWithSpeed("Body", sit_1(), 0.4)
    motionProxy.angleInterpolationWithSpeed("Body", stand_6(), 0.7)
    motionProxy.angleInterpolationWithSpeed("Body", sit_4(), 0.4)
    motionProxy.angleInterpolationWithSpeed("Body", sit_5(), 0.4)
    motionProxy.angleInterpolationWithSpeed("Body", sit_3(), 1.0)
    fallcheck.check_fall()

def stand_from_sit(): # Stands from sit down position.
    config.stiffness_on()   # Turns the stiffness on.
    motionProxy.angleInterpolationWithSpeed("Body", sit_3(), 0.3)
    motionProxy.angleInterpolationWithSpeed("Body", sit_4(), 0.3)
    motionProxy.angleInterpolationWithSpeed("Body", stand_6(), 0.65)
    motionProxy.angleInterpolationWithSpeed("Body", sit_1(), 0.4)
    motionProxy.angleInterpolationWithSpeed("Body", sit_2(), 0.2)
    motionProxy.angleInterpolationWithSpeed("Body", pose_int(), 1.0)
    fallcheck.check_fall()
