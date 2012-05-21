import config
import kickcarpet
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
    walk.walkTimed(5.5)
    config.PoseInit(proxy, .5)
    # Kicking Left Foot while saying specified text.
    kickcarpet.kickLeftFoot("one!")
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)

    # Walk for specified time in seconds.
    walk.walkTimed(5.5)
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)
    # Kicking Right Foot while saying specified text.
    kickcarpet.kickRightFoot("two!")
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)
    # Walk for specified time in seconds.
    walk.walkTimed(5.5)
    config.StiffnessOn(proxy)
    config.PoseInit(proxy, .5)
    # Kicking Left Foot while saying specified text.
    kickcarpet.kickLeftFoot("three!")
    config.StiffnessOn(proxy)

    # Switch pose to initial at half the max speed.
    config.PoseInit(proxy, .2)

    # Say specified text.
    tts.say("game over!")

def main2():
    proxy = config.loadProxy("ALMotion")
    tts = ALProxy("ALTextToSpeech", config.IP, 9559)

    # Turn Stiffness On in order to have the robot do moves and not fall.
    config.StiffnessOn(proxy)
    # throws ball
    throw.throwright("haya!")
if __name__ == "__main__":
    main2()