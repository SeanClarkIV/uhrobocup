import config
import kick
from naoqi import ALProxy
import walkfor

def main():

    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)

    #puts him in pose initial at half the max speed.
    config.PoseInit(proxy, .5)

    #walkfor is walkfor(y) y being the seconds you want it to sleep (walk)
    walkfor.walkfor(5.5)

    #kick is defined as kick(y) making the robot kick but y is an input
    #that is a string he says right before kicking so if you want to do a battle
    #cry of messi!!! you would put kick.kick("Messi!!!")
    kick.kickLeftFoot("one!")

    walkfor.walkfor(5.5)

    #Kicking section

    kick.kickRightFoot("two!")

    walkfor.walkfor(5.5)

    #Kicking section

    kick.kickLeftFoot("three!")

    config.PoseInit(proxy, .5)

    #tts.say makes the robot convert the string to speech.
    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("game over!")

if __name__ == "__main__":
    main()