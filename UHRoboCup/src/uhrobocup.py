import config
import walkfor
import kickball
from naoqi import ALProxy

def main():

    proxy = config.loadProxy("ALMotion")

    # Turn Stiffness On in order to have the robot do moves.
    config.StiffnessOn(proxy)

    #puts him in pose initial at half the max speed.
    config.PoseInit(proxy, .5)

    #walkfor is walkfor(y) y being the seconds you want it to sleep (walk)
    walkfor.walkfor(5.5)

    #kickball is defined as kickball(y) making the robot kick but y is an input
    #that is a string he says right before kicking so if you want to do a battle
    #cry of messi!!! you would put kickball.kickball("Messi!!!")
    kickball.leftkick("one!")

    walkfor.walkfor(5.5)

    #Kicking section

    kickball.rightkick("two!")

    walkfor.walkfor(5.5)

    #Kicking section

    kickball.leftkick("three!")

    config.PoseInit(proxy, .5)

    #tts.say makes the robot convert the string to speech.
    tts = ALProxy("ALTextToSpeech", config.IP, 9559)
    tts.say("game over!")

if __name__ == "__main__":
    main()