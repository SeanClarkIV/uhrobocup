import kick
import config
from naoqi import ALProxy

#This function kicks the ball, y being an input of what to say right before he
#kicks the ball.

#rightkick kicks with right foot
def rightkick(y):

    proxy = config.loadProxy("ALMotion")

    #Turns the stiffness on.
    config.StiffnessOn(proxy)

    pNames = "Body"
    
    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

    proxy.angleInterpolationWithSpeed(pNames, kick.step2(), 1.0)

    proxy.angleInterpolationWithSpeed(pNames, kick.step3(), 0.9)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say(y)

    proxy.angleInterpolationWithSpeed(pNames, kick.step4(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step1(), 0.1)

#leftkick kicks with left foot
def leftkick(y):
    proxy = config.loadProxy("ALMotion")

    #Turns the stiffness on.
    config.StiffnessOn(proxy)

    pNames = "Body"

    proxy.angleInterpolationWithSpeed(pNames, kick.step5(), 0.1)

    proxy.angleInterpolationWithSpeed(pNames, kick.step6(), 1.0)

    proxy.angleInterpolationWithSpeed(pNames, kick.step7(), 0.9)

    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say(y)

    proxy.angleInterpolationWithSpeed(pNames, kick.step8(), 0.6)

    proxy.angleInterpolationWithSpeed(pNames, kick.step5(), 0.1)