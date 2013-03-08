import config

videodeviceProxy = config.loadProxy("ALVideoDevice")

def topCamera(): # Activate top camera.
    kCameraSelectID = 18
    videodeviceProxy.setParam(kCameraSelectID, 0)

def bottomCamera(): # Activate bottom camera.
    kCameraSelectID = 18
    videodeviceProxy.setParam(kCameraSelectID, 1)