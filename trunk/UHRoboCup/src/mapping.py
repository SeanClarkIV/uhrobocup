from PIL import Image, ImageDraw
import os
import math

import localization
import config

def map():
    config.StiffnessOn()
    config.PoseInit()
    maplocation(localization.getnaolocation(),localization.getlocation())


def maplocation((naoX, naoY, naoZ, naoID), (ballX, ballY)):
    currentFolder = (os.getcwd() + "\\")
    field = Image.open(currentFolder + "robocupfield.jpg")  # Open field image
    draw = ImageDraw.Draw(field)    # Select field image to draw to

    offset = 76.45489365

    naoX = ((naoX * offset) + 70)
    naoY = ((naoY * -offset) + 70)

    draw.point([naoX, naoY])   # Draw point based on location received
    print (naoX, naoY, naoZ, naoID)

    print (naoX, naoY, naoZ, naoID)
    radius = 8  # Radius of NAO based on foot length
    box = ((naoX - radius), (naoY - radius), (naoX + radius), (naoY + radius)) # Formulates the size of the box to crop in pixels (left, upper, right, bottom)
    draw.ellipse(box)    # Daw circle around point received

    ballX = naoX + (ballX * offset)
    ballY = naoY + (ballY * -offset)
    draw.point([ballX, ballY])   # Draw point based on location received
    print ("ball", ballX, ballY)

    radius = 3.25  # Radius of ball based on 65mm diameter
    box = ((ballX - radius), (ballY - radius), (ballX + radius), (ballY + radius)) # Foradiusmulates the size of the box to crop in pixels (left, upper, right, bottom)
    draw.ellipse(box, fill=128)    # Daw circle around point received

    pixelDistance = math.sqrt(((ballX - naoX) * (ballX - naoX)) + ((ballY - naoY) * (ballY - naoY)))

    realDistance = (pixelDistance * 10)

    print realDistance
    print (1-((1500-realDistance)/1500)), "percent error"


    # TODO: Draw direction robot is moving to
    # TODO: Draw visual angle of robot
    del draw    # Stop draw process.
    field.save("mappedobjects.jpg", "JPEG")
    field.show()