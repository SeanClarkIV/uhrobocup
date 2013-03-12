import time

from PIL import Image, ImageDraw
import numpy

import config

def redballdetection():
    # Get image from NAO Robot
    origImage = getImage()

    # Function returns a matrix with 0s and 1s where 1s represent red pixels
    (imgWidth, imgHeight, matrix) = pixelMatrix(origImage)

    # Identify ball from filtered image and Calculate diameter and center of ball
    (ballStart, ballEnd, ballCenter, ballDiameter) = findandanalyseBall(imgWidth, imgHeight, matrix)

    #TODO: Calculate distance and angle

    return

def getImage():
  ''' First get an image from Nao, then show it on the screen with PIL '''

  camProxy = config.loadProxy("ALVideoDevice")
  resolution = 1    # 320x240
  colorSpace = 11   # RGB

  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

  t0 = time.time()

  # Get a camera image.
  # image[6] contains the image data passed as an array of ASCII chars.
  naoImage = camProxy.getImageRemote(videoClient)

  t1 = time.time()

  # Time the image transfer.
  print "acquisition delay ", t1 - t0

  camProxy.unsubscribe(videoClient)


  # Now we work with the image returned and save it as a PNG  using ImageDraw
  # package.

  # Get the image size and pixel array.
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]

  # Create a PIL Image from our pixel array.
  origImage = Image.fromstring("RGB", (imageWidth, imageHeight), array)

  # Save the image.
  # im.save( str(colorSpace) + ".png", "PNG")

  return origImage

def pixelMatrix(origIm):
    outfile = open('file.txt', 'w') # Open original image

    origWidth = origIm.size[0]      # Get original image's width.
    origHeight = origIm.size[1]     # Get original image's height.
    print "Dimensions - w:", imgWidth, "h:", imgHeight

#    analysedIm = Image.new("RGB", (origWidth,origHeight), "white")  # Create blank image with same dimendions as original image

#    draw = ImageDraw.Draw(analysedIm)   # Set wich image to draw pixels to.

    matrix = numpy.zeros(shape=(origHeight,origWidth))
    for height in range(0, (origHeight), 1):    # Iterate up to down on image through each pixel.
        if height > 0:
            outfile.write("\n")
        for width in range (0, (origWidth), 1): # Iterate left to righ on image through each pixel.
            r, g, b = origIm.getpixel((width,height)) # Save each pixel color to variables r,g,b.

            if (r >= 85) and (g <= ((r/4)*3)):  # Find all pixels that have a red hue.
                matrix[height][width] = 1
                outfile.write("1")
            else:
                outfile.write("0")

    return (imgWidth, imgHeight, matrix)

def findandanalyseBall(collumns, rows, matrix):
    ''' List of variables we want to find '''
    ballStart = [0,0]   # Setting quadrant where image of ball starts at zero using [y,x] format
    ballEnd = [0,0]     # Setting quadrant where image of ball ends at zero using [y,x] format
    ballDiameter = 0    # Setting Diameter variable to zero
    ballCenter = [0,0]  # Setting quadrant of center of ball at zero using [y,x] format

    ''' Function to find variables '''
    for row in range(0, (rows), 1):                         # Iterate up to down on image through each pixel represented by number in matrix
        for collumn in range (0, (collumns), 1):            # Iterate left to righ on image through each pixel represented by number in matrix
            if collumn < collumns-1:                        # Parameter used in order to not do the foloowing for the last collumn
                iniPixel = int(matrix[row][collumn])        # Setting variable for current pixel being checked
                nextPixel = int(matrix[row][collumn+1])     # Setting variable for the pixel adjacent to the current one being checked
                if (iniPixel - nextPixel) == -1:            # If pixel pattern is [0,1] we found the start of the red pixels
                    foundballStart =  [row+1, collumn+2]    # Setting array variable containing location of the start of the red pixels
#                    print foundballStart                    # Print array variable for DEBUGING purposes
                elif (iniPixel - nextPixel) == 1:           # If pixel pattern is [1,0] we found the end of the red pixels
                    foundballEnd = [row+1, collumn+1]       # Setting array variable containing location of the end of the red pixels
#                    print foundballEnd                      # Print array variable for DEBUGING purposes

                    foundDiameter = (int(foundballEnd[1]) - ((int(foundballStart[1]))+1))   # Checking how many red pixels wide were found together
#                    print foundDiameter                     # Print variable for DEBUGING purposes

                    if foundDiameter > ballDiameter:        # Comparing if the number of red pixels found is bigger than what was found before
                        ballDiameter = foundDiameter        # Setting Diameter variable to new found diameter
                        ballStart = foundballStart          # Setting quadrant where image of ball starts at to found quadrant using [y,x] format
                        ballEnd = foundballEnd              # Setting quadrant where image of ball ends at to found quadrant using [y,x] format
                        ballCenter = [int(foundballEnd[0]),(int(foundballStart[1]))+(foundDiameter/2)]  # Setting quadrant of center of ball at calculated quadrant using [y,x] format

    ''' Output '''
    return "Biggest Diameter:", ballStart, ballEnd, ballCenter, ballDiameter
