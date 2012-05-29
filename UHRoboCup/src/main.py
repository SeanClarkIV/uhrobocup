import config
import kick
from naoqi import ALProxy
import walk
import throw

def main():

    # Common Variables
    proxy = config.loadProxy("ALMotion")
    tts = ALProxy("ALTextToSpeech", config.IP, 9559)

    # Turn Stiffness On in order to have the robot do moves and not fall.
    config.StiffnessOn(proxy)
    # Switch pose to initial at half the max speed.
    config.PoseInit(proxy, .5)

    # Walk for specified time in seconds.

    # Kicking Left Foot while saying specified text.
    kick.kickLeftFoot()
    kick.kickRightFoot()
    # Walk for specified time in seconds.
    config.PoseInit(proxy, .2)

    # Say specified text.
    tts.say("Team. maqena, erektous. University of Houston. Go cougars")

def main2():
    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves and not fall.
    config.StiffnessOn(proxy)
    # throws ball
    throw.throwstrait()
if __name__ == "__main__":
    main()