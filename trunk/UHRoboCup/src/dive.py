import stand
import config
import motion
motionProxy = config.load_proxy("ALMotion")
pNames = "Body"
def goalie_position():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-10, +0, -50, +121, -68, +0]
    RightLeg = [-10, 00, -50, +121, -68, +0]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def goalie_sit():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-50.3, -1, -89, +97.5, +38, +15.7]
    RightLeg = [-50.3, +1, -89, +97.5, +38, -15.7]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive_left_1():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-65.6, 38, -38.3, -5.3, +52.9, -3.8]
    RightLeg = [-65.6, -79.1, -83.4, +66.6, 53.4, +2.2]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def dive_right_1():
    Head     = [+0, +0]

    LeftArm  = [+115.5, +18.5, +2, -18, +5.5, +0]
    RightArm = [+115.50, -18.5, -2, +18, +5.5, +0]

    LeftLeg  = [-65.6, 79.1, -83.4, 66.6, +53.4, 2.2]
    RightLeg = [-65.6, -38, -38.3, -5.3, 52.9,-3.8]

    pTargetAngles = (Head + LeftArm + LeftLeg + RightLeg + RightArm)
    pTargetAngles = [x * motion.TO_RAD for x in pTargetAngles]
    return pTargetAngles
def goalie_pose():
    config.stiffness_on()
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_position(), 0.3)
def dive_left():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_position(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_sit(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, dive_left_1(), .1)
    motionProxy.setFallManagerEnabled(True)
    stand.stand_from_sit()
    goalie_pose()
def dive_right():
    config.stiffness_on()
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_position(), 0.1)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_sit(), .5)
    motionProxy.angleInterpolationWithSpeed(pNames, dive_right_1(), .1)
    motionProxy.setFallManagerEnabled(True)
    stand.stand_from_sit()
    goalie_pose()
def dive_left_goal():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_sit(), .8)
    motionProxy.angleInterpolationWithSpeed(pNames, dive_left_1(), .7)
    motionProxy.setFallManagerEnabled(True)
    stand.stand_from_sit()
    goalie_pose()
def dive_right_goal():
    motionProxy.setFallManagerEnabled(False)
    motionProxy.angleInterpolationWithSpeed(pNames, goalie_sit(), .8)
    motionProxy.angleInterpolationWithSpeed(pNames, dive_right_1(), .7)
    motionProxy.setFallManagerEnabled(True)
    stand.stand_from_sit()
    goalie_pose()