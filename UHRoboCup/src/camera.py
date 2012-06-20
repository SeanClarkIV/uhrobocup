import config
from naoqi import ALProxy

videodevice = ALProxy("ALVideoDevice", config.IP, 9559)

def topCamera():
    kCameraSelectID = 18
    videodevice.setParam(kCameraSelectID, 0)

def bottomCamera():
    kCameraSelectID = 18
    videodevice.setParam(kCameraSelectID, 1)