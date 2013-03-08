import config

motionProxy = config.loadProxy("ALMotion")
redballtracker = config.loadProxy("ALRedBallTracker")

def getNaoLocation():
    naoID = "goalie"
    (naoX, naoY, naoZ) = motionProxy.getRobotPosition(False)
    return (naoX, naoY, naoZ, naoID)
