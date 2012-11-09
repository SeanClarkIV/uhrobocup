import config

videodeviceProxy = config.load_proxy("ALVideoDevice")

def top_camera(): # Activate top camera.
    kCameraSelectID = 18
    videodeviceProxy.setParam(kCameraSelectID, 0)

def bottom_camera(): # Activate bottom camera.
    kCameraSelectID = 18
    videodeviceProxy.setParam(kCameraSelectID, 1)