import config

motionProxy = config.loadProxy("ALMotion")

def ewalk():

    #This walk walks for a walkTime amount of time and then stops.
    useSensors = True
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    angles = motionProxy.getAngles("Head", useSensors)
    X = 1.0
    Y = 0.0
    Theta = angles[0]/2.1
    Frequency = 1

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)
def stop():

    #This walk walks for a walkTime amount of time and then stops.
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    X = 0
    Y = 0.0
    Theta = 0
    Frequency = 0

    motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

def ultimatewalkto(x, y, z):
    # Set NAO in stiffness On
    config.StiffnessOn(motionProxy)

    # This example show customization for the both foot
    # with all the possible gait parameters
    motionProxy.walkTo(x, y, z,
        [ ["MaxStepX", 0.08],         # step of x cm in front
          ["MaxStepY", 0.2],         # default value
          ["MaxStepTheta", 0.4],      # default value
          ["MaxStepFrequency", 3.0],  # low frequency
          ["StepHeight", 0.015],       # step height of x cm
          ["TorsoWx", 0],           # default value
          ["TorsoWy", -0.1] ])         # torso bend 0.1 rad in front