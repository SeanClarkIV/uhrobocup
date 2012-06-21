import config
from naoqi import ALProxy

videodevice = ALProxy("ALVideoDevice", config.IP, 9559)

def topCamera(): # Activate top camera.
    kCameraSelectID = 18
    videodevice.setParam(kCameraSelectID, 0)

def bottomCamera(): # Activate bottom camera.
    kCameraSelectID = 18
    videodevice.setParam(kCameraSelectID, 1)