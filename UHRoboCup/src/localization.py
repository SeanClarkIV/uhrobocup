import config

motionProxy = config.load_proxy("ALMotion")
redballtracker = config.load_proxy("ALRedBallTracker")

def get_nao_location():
    naoID = "goalie"
    (naoX, naoY, naoZ) = motionProxy.getRobotPosition(False)
    return (naoX, naoY, naoZ, naoID)
